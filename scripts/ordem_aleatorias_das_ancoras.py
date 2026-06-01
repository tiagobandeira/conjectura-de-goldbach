# -*- coding: utf-8 -*-
"""
Experimento 3 – Ordem aleatória das âncoras absolutas
Compara cobertura usando ordem crescente vs ordem aleatória.
"""

import math
import numpy as np
import time
import random
import csv

LIMITE_N = 10_000_000   # pode testar para 1M primeiro
ANCORA_MAX_BUSCA = 2000
NUM_ALEATORIOS = 10     # número de sementes aleatórias

def crivo(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[0:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    return sieve

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

def satura_com_ordem(ancoras, limite_C, ip):
    cobertos = np.zeros(limite_C + 2, dtype=bool)
    for idx, p in enumerate(ancoras):
        acumular(p, limite_C, ip, cobertos)
        if (idx+1) % 5 == 0 or idx < 10:
            gm = gap_max_cobertura(cobertos, limite_C)
            if gm is not None and gm <= 2:
                return idx+1, p
    return len(ancoras), ancoras[-1]

def main():
    print(f"Construindo crivo para N={LIMITE_N}...")
    tam = 6 * LIMITE_N + ANCORA_MAX_BUSCA + 10
    ip = crivo(tam)
    todos_primos = [p for p in range(5, ANCORA_MAX_BUSCA+1) if ip[p]]
    print(f"Total de âncoras disponíveis: {len(todos_primos)}")

    # Ordem crescente (original)
    k_crescente, p_crescente = satura_com_ordem(todos_primos, LIMITE_N, ip)
    print(f"\nOrdem crescente: k={k_crescente}, p_max={p_crescente}")

    # Ordens aleatórias
    resultados_aleatorios = []
    for seed in range(NUM_ALEATORIOS):
        random.seed(seed)
        aleatorio = todos_primos.copy()
        random.shuffle(aleatorio)
        k_rand, p_rand = satura_com_ordem(aleatorio, LIMITE_N, ip)
        resultados_aleatorios.append((k_rand, p_rand))
        print(f"Seed {seed:2d}: k={k_rand:3d}, p_max={p_rand:4d}")

    # Estatísticas
    ks = [r[0] for r in resultados_aleatorios]
    ps = [r[1] for r in resultados_aleatorios]
    print(f"\nAleatório: k médio = {np.mean(ks):.1f} ± {np.std(ks):.1f}")
    print(f"          p médio = {np.mean(ps):.1f} ± {np.std(ps):.1f}")
    print(f"Crescente: k = {k_crescente}, p = {p_crescente}")

    with open("experimento3_ordem_aleatoria.csv", "w") as f:
        f.write("seed,k,p\n")
        for seed, (k,p) in enumerate(resultados_aleatorios):
            f.write(f"{seed},{k},{p}\n")

if __name__ == "__main__":
    main()