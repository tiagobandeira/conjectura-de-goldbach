# -*- coding: utf-8 -*-
"""
Script: correlacao_absoluta_compacta.py
Objetivo: Calcular a matriz de correlação entre as ativações de âncoras absolutas
(primos >=5) para diferentes escalas N, usando representação compacta (bits).
Autor: Tiago Bandeira
Data: Maio 2026
"""

import math
import time
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

# ============================================================
# CONFIGURAÇÃO
# ============================================================
LIMITES_N = [1_000_000, 10_000_000]   # Adicione 100_000_000 com cuidado
MAX_ANCORAS = 100                     # Número de âncoras (primos) a considerar
ANCORA_MAX_BUSCA = 5000
# ============================================================

def crivo(n):
    """Crivo de Eratóstenes."""
    sieve = np.ones(n + 1, dtype=bool)
    sieve[0:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    return sieve

def cobertura_para_bits(ancora, limite_C, ip):
    """
    Retorna um array de bytes (bits) onde cada bit indica se o C correspondente
    é coberto por esta âncora. Usa packbits: cada byte representa 8 C's.
    """
    # Número de C pares: C = 4,6,8,...,limite_C
    n_C = limite_C // 2 - 1   # pois começa em 4
    # Criar array de bytes inicializado com zero (tamanho: ceil(n_C/8))
    n_bytes = (n_C + 7) // 8
    bits = bytearray(n_bytes)

    q_min = max(2, 6*4 - ancora)
    q_max = min(6*limite_C - ancora, len(ip)-1)
    if q_max < q_min:
        return bits

    FATIA = 10_000_000
    pos = q_min
    while pos <= q_max:
        fim = min(pos + FATIA, q_max + 1)
        qs = np.where(ip[pos:fim])[0] + pos
        num = qs + ancora
        mask = (num % 6 == 0)
        Cs = (num[mask] // 6).astype(np.int64)
        # Filtra C pares e dentro do limite
        Cs = Cs[(Cs % 2 == 0) & (Cs >= 4) & (Cs <= limite_C)]
        for c in Cs:
            # índice do C: (c - 4)//2
            idx = (c - 4) // 2
            byte_idx = idx // 8
            bit_idx = idx % 8
            bits[byte_idx] |= (1 << bit_idx)
        pos = fim
    return bits

def correlacao_entre_bits(bits1, bits2):
    """
    Calcula a correlação de Pearson entre dois vetores binários representados
    como arrays de bits (bytearrays de mesmo tamanho).
    """
    n_bytes = len(bits1)
    n_C = n_bytes * 8  # aproximado, mas o último byte pode ter bits inúteis
    # Contar quantos 1's em cada
    count1 = sum(bin(b).count('1') for b in bits1)
    count2 = sum(bin(b).count('1') for b in bits2)
    # Contar interseção (AND bit a bit)
    inter = 0
    for b1, b2 in zip(bits1, bits2):
        inter += bin(b1 & b2).count('1')
    p1 = count1 / n_C
    p2 = count2 / n_C
    p12 = inter / n_C
    cov = p12 - p1 * p2
    var1 = p1 * (1 - p1)
    var2 = p2 * (1 - p2)
    if var1 * var2 == 0:
        return 0.0
    return cov / math.sqrt(var1 * var2)

def main():
    os.makedirs("resultados_correlacao_abs_compacta", exist_ok=True)
    resultados = []

    for N in LIMITES_N:
        print(f"\n=== Processando N = {N:,} ===")
        t0 = time.time()

        # Prepara crivo
        tam = 6 * N + ANCORA_MAX_BUSCA + 10
        ip = crivo(tam)
        print(f"  Crivo pronto em {time.time()-t0:.1f}s")

        # Gera lista de âncoras absolutas (primos >=5)
        ancoras = [p for p in range(5, ANCORA_MAX_BUSCA+1) if ip[p]]
        ancoras = ancoras[:MAX_ANCORAS]
        print(f"  Âncoras consideradas: {len(ancoras)}")

        # Gerar representação compacta para cada âncora
        bits_list = []
        for i, p in enumerate(ancoras):
            bits = cobertura_para_bits(p, N, ip)
            bits_list.append(bits)
            if (i+1) % 20 == 0:
                print(f"    Processadas {i+1} âncoras...")
        print(f"  Representação gerada em {time.time()-t0:.1f}s")

        # Calcular matriz de correlação (simétrica)
        n = len(ancoras)
        corr = np.zeros((n, n))
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    corr[i,i] = 1.0
                else:
                    r = correlacao_entre_bits(bits_list[i], bits_list[j])
                    corr[i,j] = r
                    corr[j,i] = r
            if (i+1) % 10 == 0:
                print(f"    Correlações calculadas para {i+1} âncoras...")

        print(f"  Matriz de correlação concluída em {time.time()-t0:.1f}s")

        # Estatísticas
        mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
        off_diag = corr[mask]
        mean_corr = np.mean(off_diag)
        max_corr = np.max(off_diag)
        min_corr = np.min(off_diag)
        std_corr = np.std(off_diag)

        # Autovalores
        eigvals = np.linalg.eigvalsh(corr)
        max_eig = np.max(eigvals)

        resultados.append({
            'N': N,
            'n_ancoras': n,
            'mean_corr': mean_corr,
            'max_corr': max_corr,
            'min_corr': min_corr,
            'std_corr': std_corr,
            'max_eigenvalue': max_eig
        })

        print(f"  Média (off-diag): {mean_corr:.6f}")
        print(f"  Máx: {max_corr:.6f}, Mín: {min_corr:.6f}")
        print(f"  Maior autovalor: {max_eig:.4f}")

        # Salvar matriz (opcional)
        np.save(f"resultados_correlacao_abs_compacta/corr_N{N}.npy", corr)
        # Salvar âncoras
        with open(f"resultados_correlacao_abs_compacta/ancoras_N{N}.csv", "w") as f:
            f.write("idx,ancora\n")
            for i, p in enumerate(ancoras):
                f.write(f"{i},{p}\n")

        # Plotar espectro
        plt.figure()
        plt.hist(eigvals, bins=30, density=True, alpha=0.7, label='Espectro')
        # Limites de Marchenko-Pastur (q = n / n_C)
        n_C = N // 2 - 1
        q = n / n_C
        lambda_plus = (1 + np.sqrt(q))**2
        lambda_minus = (1 - np.sqrt(q))**2
        plt.axvline(lambda_minus, color='r', linestyle='--', label=f'MP min ({lambda_minus:.2f})')
        plt.axvline(lambda_plus, color='r', linestyle='--', label=f'MP max ({lambda_plus:.2f})')
        plt.xlabel('Autovalor')
        plt.ylabel('Densidade')
        plt.title(f'Espectro da correlação (N={N}) - âncoras absolutas')
        plt.legend()
        plt.savefig(f"resultados_correlacao_abs_compacta/espectro_N{N}.png", dpi=150)
        plt.close()

    # Resumo
    with open("resultados_correlacao_abs_compacta/resumo.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["N", "n_ancoras", "mean_corr", "max_corr", "min_corr", "std_corr", "max_eigenvalue"])
        for r in resultados:
            writer.writerow([r['N'], r['n_ancoras'], r['mean_corr'], r['max_corr'],
                             r['min_corr'], r['std_corr'], r['max_eigenvalue']])

    if len(LIMITES_N) > 1:
        plt.figure()
        plt.semilogx([r['N'] for r in resultados], [r['mean_corr'] for r in resultados], 'o-')
        plt.xlabel('N (escala)')
        plt.ylabel('Correlação média entre âncoras')
        plt.title('Evolução da anticorrelação com a escala (âncoras absolutas)')
        plt.grid(True)
        plt.savefig("resultados_correlacao_abs_compacta/evolucao.png", dpi=150)
        plt.close()

    print("\nAnálise concluída. Resultados em 'resultados_correlacao_abs_compacta/'.")

if __name__ == "__main__":
    main()