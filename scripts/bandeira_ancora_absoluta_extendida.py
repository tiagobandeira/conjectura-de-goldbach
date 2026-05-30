# -*- coding: utf-8 -*-
"""
Versão estendida para investigar a deriva de A_abs e k*
"""

import math
import numpy as np
import time
import pickle   # para salvar resultados

LIMITES_N = [1_000_000, 2_000_000, 5_000_000,
             10_000_000, 20_000_000, 50_000_000, 100_000_000]
ANCORA_MAX_BUSCA = 5_000

def crivo(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[0:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    return sieve

def forma_8j5(p):
    return p != 3 and (p + 5) % 8 == 0

def acumular(ancora, limite_C, ip, cobertos_arr):
    FATIA = 10_000_000
    q_min = max(2, 6*4 - ancora)
    q_max = min(6*limite_C - ancora, len(ip)-1)
    if q_max < q_min:
        return
    pos = q_min
    while pos <= q_max:
        fim = min(pos + FATIA, q_max + 1)
        qs = np.where(ip[pos:fim])[0] + pos
        num = qs + ancora
        mask = (num % 6 == 0)
        Cs = (num[mask] // 6).astype(np.int64)
        mask2 = (Cs % 2 == 0) & (Cs >= 4) & (Cs <= limite_C)
        cobertos_arr[Cs[mask2]] = True
        pos = fim

def gap_max_cobertura(cobertos_arr, limite_C):
    indices = np.where(cobertos_arr[4:limite_C+1])[0] + 4
    indices = indices[indices % 2 == 0]
    if len(indices) < 2:
        return None
    return int(np.diff(indices).max())

def rodar_saturacao(limite_C, ip, ancoras, label, registra_cobertura=False):
    cobertos = np.zeros(limite_C + 2, dtype=bool)
    logN = math.log(limite_C)
    llogN = math.log(logN)

    historico = []  # para guardar (k, p, A, gap_max) se quisermos

    for idx, p in enumerate(ancoras):
        acumular(p, limite_C, ip, cobertos)
        k = idx + 1
        if k % 5 == 0 or k <= 10:
            gm = gap_max_cobertura(cobertos, limite_C)
            if gm is not None:
                A = p / (logN * llogN)
                historico.append((k, p, A, gm))
                if gm <= 2:
                    print(f"    [{label}] k={k:4d}  p_max={p:6d}  A={A:.4f}  (gap_max=2 ✓)")
                    if registra_cobertura:
                        # Retorna também o vetor de cobertura
                        return k, p, A, cobertos
                    return k, p, A, None
    # Se não completou
    gm = gap_max_cobertura(cobertos, limite_C)
    print(f"    [{label}] cobertura incompleta após {len(ancoras)} âncoras (gap_max={gm})")
    return None, None, None, None

def main():
    t0 = time.time()
    resultados = []

    for N in LIMITES_N:
        print(f"\n=== N = {N:,} ===")
        tam = 6 * N + ANCORA_MAX_BUSCA + 10
        ip = crivo(tam)
        todos_primos = [p for p in range(5, ANCORA_MAX_BUSCA+1) if ip[p]]
        ancoras_abs = todos_primos

        logN = math.log(N)
        llogN = math.log(logN)
        print(f"logN·loglogN = {logN:.4f} × {llogN:.4f} = {logN*llogN:.4f}")

        # Regime absoluto (já sabemos que é o relevante)
        k_abs, p_abs, A_abs, cobertos = rodar_saturacao(N, ip, ancoras_abs, "abs", registra_cobertura=True)

        # Salva informações adicionais: quantos C estão cobertos?
        if cobertos is not None:
            total_C = N//2 + 1  # C pares de 4 a N
            cobertos_count = np.sum(cobertos[4:N+1:2])
            frac = cobertos_count / (total_C)
            print(f"    Cobertura final: {cobertos_count}/{total_C} = {frac:.6f}")
        else:
            frac = 0.0

        resultados.append({
            'N': N,
            'p_abs': p_abs,
            'A_abs': A_abs,
            'k_abs': k_abs,
            'frac_cobertura': frac
        })

        del ip   # libera memória

    # Síntese
    print("\n" + "="*70)
    print("SÍNTESE DA DERIVA DE A_abs")
    print("="*70)
    print(f"{'N':>12}  {'p_abs':>6}  {'A_abs':>8}  {'k_abs':>6}  {'frac_cobertura':>12}")
    for r in resultados:
        print(f"{r['N']:>12,}  {r['p_abs']:>6}  {r['A_abs']:>8.4f}  {r['k_abs']:>6}  {r['frac_cobertura']:>12.6f}")

    # Salva os dados para análise posterior
    with open('resultados_deriva_Aabs.pkl', 'wb') as f:
        pickle.dump(resultados, f)
    print(f"\nResultados salvos em 'resultados_deriva_Aabs.pkl'")
    print(f"Tempo total: {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()