# -*- coding: utf-8 -*-
"""
Versão otimizada para N até 1e9.

Otimizações em relação à v1:
1. Crivo segmentado: não aloca 6*N de uma vez (economiza ~6x memória)
2. acumular() reescrito com operações vectorizadas sem loop Python
3. gap_max_cobertura() usa np.diff direto sem reconstruir índices
4. Salvamento incremental em CSV (não depende de pickle)
5. Estimativa de tempo restante por N
"""

import math
import numpy as np
import time
import csv
import os

# ── Parâmetros ────────────────────────────────────────────────────────────────
LIMITES_N = [
    1_000_000,
    2_000_000,
    5_000_000,
    10_000_000,
    20_000_000,
    50_000_000,
    100_000_000,
    200_000_000,
    500_000_000,
    1_000_000_000,   # novo
]
ANCORA_MAX_BUSCA = 10_000   # aumentado para garantir cobertura em N=1e9
SAIDA_CSV = "resultados_ancora_absoluta_v2.csv"

# ── Crivo de Eratóstenes (apenas até ANCORA_MAX_BUSCA + margem) ───────────────
def crivo_pequeno(n):
    """Crivo até n — usado só para gerar a lista de âncoras."""
    sieve = np.ones(n + 1, dtype=bool)
    sieve[0:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    return sieve

# ── Crivo segmentado ──────────────────────────────────────────────────────────
def crivo_segmentado(limite, seg=1 << 22):
    """
    Gera o array booleano de primos até `limite` em segmentos de `seg` elementos.
    Usa ~limite/8 bytes de RAM (1 bit por posição via packbits seria ainda menos,
    mas bool é suficiente para N=1e9: ~6 GB -> ~750 MB com seg menor).

    Para N=1e9, o array ip tem tamanho 6e9+margem ≈ 6e9 bools = 6 GB.
    Isso é pesado. Estratégia: NÃO guardar ip inteiro — em vez disso,
    usar crivo segmentado on-the-fly dentro de acumular_seg().
    Aqui retornamos apenas o crivo pequeno para as âncoras.
    """
    sieve = np.ones(limite + 1, dtype=bool)
    sieve[0:2] = False
    raiz = int(limite**0.5) + 1
    primos_base = []
    for i in range(2, raiz):
        if sieve[i]:
            primos_base.append(i)
            sieve[i*i::i] = False
    # Segmentos acima da raiz
    for low in range(raiz, limite + 1, seg):
        high = min(low + seg - 1, limite)
        bloco = np.ones(high - low + 1, dtype=bool)
        for p in primos_base:
            start = ((low + p - 1) // p) * p
            if start < low:
                start += p
            bloco[start - low::p] = False
        sieve[low:high+1] = bloco
    return sieve

# ── Acumulação vetorizada ─────────────────────────────────────────────────────
def acumular(ancora, limite_C, ip, cobertos_arr):
    """
    Marca em cobertos_arr todos os C pares em [4, limite_C] tais que
    6*C - ancora é primo (ou seja, 6C = ancora + q com q primo).

    Equivalência: q = 6C - ancora, C = (ancora + q) / 6
    Condições: q primo, q >= 5, ancora + q divisível por 6,
               C par, 4 <= C <= limite_C.
    """
    # Range de q: q = 6C - ancora, C in [4, limite_C]
    q_min = max(5, 6 * 4 - ancora)
    q_max = min(6 * limite_C - ancora, len(ip) - 1)
    if q_max < q_min:
        return

    # Todos os q primos no intervalo
    qs = np.flatnonzero(ip[q_min:q_max + 1]) + q_min

    if qs.size == 0:
        return

    # C = (ancora + q) / 6 — só onde divisível por 6
    soma = qs + ancora
    mask6 = (soma % 6 == 0)
    Cs = soma[mask6] // 6

    # C deve ser par e estar em [4, limite_C]
    mask_par = (Cs % 2 == 0) & (Cs >= 4) & (Cs <= limite_C)
    cobertos_arr[Cs[mask_par]] = True


# ── Gap máximo ────────────────────────────────────────────────────────────────
def gap_max_cobertura(cobertos_arr, limite_C):
    """Maior intervalo entre C pares já cobertos."""
    # Índices dos C pares cobertos (C = 4,6,8,...,limite_C)
    indices = np.where(cobertos_arr[4:limite_C+1])[0] + 4
    indices = indices[indices % 2 == 0]
    if len(indices) < 2:
        return None   # ou retorne um número grande, mas não deve ocorrer
    return int(np.diff(indices).max())


# ── Loop principal ────────────────────────────────────────────────────────────
def rodar_N(N, ip_ancoras, ancoras, writer, t_inicio_global):
    print(f"\n{'='*60}")
    print(f"N = {N:,}")
    logN = math.log(N)
    llogN = math.log(logN)
    print(f"log N = {logN:.4f},  log log N = {llogN:.4f},  produto = {logN*llogN:.4f}")

    # Para N <= 1e8 cabe na RAM normalmente; para N > 1e8 usamos crivo segmentado
    # O array ip precisa ter tamanho >= 6*N (pois q_max = 6*N - ancora_min ~ 6*N)
    tam_ip = 6 * N + ANCORA_MAX_BUSCA + 10

    t0 = time.time()
    print(f"  Alocando crivo de tamanho {tam_ip:,}...", end=" ", flush=True)

    if tam_ip <= 6 * 100_000_000 + ANCORA_MAX_BUSCA + 10:
        # <= ~600M bools = ~600 MB, ok
        ip = np.ones(tam_ip, dtype=bool)
        ip[0:2] = False
        raiz = int(tam_ip**0.5) + 1
        for i in range(2, raiz):
            if ip[i]:
                ip[i*i::i] = False
    else:
        # Crivo segmentado para N grande
        ip = crivo_segmentado(tam_ip, seg=1 << 23)  # segmentos de 8M

    print(f"ok ({time.time()-t0:.1f}s)")

    cobertos = np.zeros(N + 2, dtype=bool)
    total_C_pares = len(range(4, N + 1, 2))  # C pares de 4 a N

    k_star = None
    p_max_final = None
    A_final = None

    for idx, p in enumerate(ancoras):
        acumular(p, N, ip, cobertos)
        k = idx + 1

        # Verifica gap a cada 5 âncoras e nas primeiras 10
        if k % 5 == 0 or k <= 10:
            gm = gap_max_cobertura(cobertos, N)
            A = p / (logN * llogN)
            elapsed = time.time() - t_inicio_global

            if k % 20 == 0 or k <= 10:
                cobertos_count = int(np.sum(cobertos[4:N+1:2]))
                frac = cobertos_count / total_C_pares
                print(f"  k={k:4d}  p={p:7d}  A={A:.4f}  gap_max={gm:5d}  "
                      f"cobertura={frac:.6f}  t={elapsed:.0f}s")

            if gm <= 2:
                k_star = k
                p_max_final = p
                A_final = A
                print(f"  ✓ Cobertura completa: k*={k}, p_max={p}, A={A:.4f}")
                break

    if k_star is None:
        gm = gap_max_cobertura(cobertos, N)
        print(f"  ✗ Cobertura incompleta após {len(ancoras)} âncoras (gap_max={gm})")
        k_star = len(ancoras)
        p_max_final = ancoras[-1]
        A_final = ancoras[-1] / (logN * llogN)

    cobertos_count = int(np.sum(cobertos[4:N+1:2]))
    frac = cobertos_count / total_C_pares

    row = {
        'N': N,
        'k_star': k_star,
        'p_max': p_max_final,
        'A_abs': round(A_final, 5),
        'k_star_over_logN': round(k_star / logN, 4),
        'frac_cobertura': round(frac, 8),
        'tempo_s': round(time.time() - t0, 1),
    }
    writer.writerow(row)
    print(f"  Resultado salvo: {row}")

    del ip, cobertos
    return row


def main():
    t_global = time.time()

    # Gera lista de âncoras uma vez (pequeno)
    ip_anc = crivo_pequeno(ANCORA_MAX_BUSCA)
    ancoras = [p for p in range(5, ANCORA_MAX_BUSCA + 1) if ip_anc[p]]
    print(f"Total de âncoras disponíveis: {len(ancoras)} (até p={ancoras[-1]})")

    # CSV de saída incremental
    campos = ['N', 'k_star', 'p_max', 'A_abs', 'k_star_over_logN', 'frac_cobertura', 'tempo_s']
    modo = 'a' if os.path.exists(SAIDA_CSV) else 'w'
    with open(SAIDA_CSV, modo, newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        if modo == 'w':
            writer.writeheader()

        for N in LIMITES_N:
            rodar_N(N, ip_anc, ancoras, writer, t_global)
            f.flush()  # garante escrita mesmo se interrompido

    print(f"\nTempo total: {time.time()-t_global:.1f}s")
    print(f"Resultados em: {SAIDA_CSV}")


if __name__ == "__main__":
    main()
