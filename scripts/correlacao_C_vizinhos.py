# -*- coding: utf-8 -*-
"""
Script: correlacao_C_vizinhos.py
Objetivo: Calcular a correlação entre eventos de não cobertura para C e C+2,
para diferentes números de âncoras k.
Autor: Tiago Bandeira
Data: Maio 2026
"""

import numpy as np
import csv
import os
from collections import defaultdict

# Parâmetros
LIMITES_N = [1_000_000, 10_000_000]   # 100_000_000 opcional
K_VALS = [50, 70, 90, 105]            # números de âncoras a testar
ANCORA_MAX_BUSCA = 5000

def crivo(n):
    sieve = np.ones(n+1, dtype=bool)
    sieve[0:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    return sieve

def cobertura_apos_k_ancoras(ancoras, k, N, ip):
    """Retorna um array booleano covered[0..n_C-1] para as primeiras k âncoras."""
    n_C = N // 2 - 1
    covered = np.zeros(n_C, dtype=bool)
    for p in ancoras[:k]:
        q_min = max(2, 6*4 - p)
        q_max = min(6*N - p, len(ip)-1)
        if q_max < q_min:
            continue
        pos = q_min
        while pos <= q_max:
            fim = min(pos + 10_000_000, q_max + 1)
            qs = np.where(ip[pos:fim])[0] + pos
            num = qs + p
            mask = (num % 6 == 0)
            Cs = (num[mask] // 6).astype(np.int64)
            Cs = Cs[(Cs % 2 == 0) & (Cs >= 4) & (Cs <= N)]
            idx = (Cs - 4) // 2
            covered[idx] = True
            pos = fim
    return covered

def correlacao_vizinhos(covered):
    """Calcula a correlação de Pearson entre covered[i] e covered[i+1] (i e i+1 representam C e C+2)."""
    n = len(covered) - 1
    # eventos de não cobertura: 1 - covered
    not_covered = 1 - covered.astype(np.float32)
    # Pares consecutivos
    x = not_covered[:-1]
    y = not_covered[1:]
    # Pearson
    corr = np.corrcoef(x, y)[0,1]
    # Covariância amostral
    cov = np.cov(x, y)[0,1]
    return corr, cov

def main():
    resultados = []
    for N in LIMITES_N:
        print(f"\n=== N = {N:,} ===")
        # Carregar âncoras absolutas (já salvas)
        ancoras_file = f"resultados_correlacao_abs_compacta/ancoras_N{N}.csv"
        if not os.path.exists(ancoras_file):
            print(f"  Arquivo de âncoras não encontrado: {ancoras_file}")
            continue
        ancoras = []
        with open(ancoras_file, 'r') as f:
            next(f)
            for line in f:
                _, p = line.strip().split(',')
                ancoras.append(int(p))
        print(f"  Âncoras carregadas: {len(ancoras)}")
        # Construir crivo
        tam = 6 * N + ANCORA_MAX_BUSCA + 10
        ip = crivo(tam)
        for k in K_VALS:
            if k > len(ancoras):
                continue
            covered = cobertura_apos_k_ancoras(ancoras, k, N, ip)
            corr, cov = correlacao_vizinhos(covered)
            # Fração de C não cobertos
            frac_uncovered = 1 - np.mean(covered)
            resultados.append({
                'N': N,
                'k': k,
                'frac_uncovered': frac_uncovered,
                'corr_neighbors': corr,
                'cov_neighbors': cov
            })
            print(f"  k={k}: frac_uncovered={frac_uncovered:.6f}, corr_vizinhos={corr:.6f}, cov={cov:.6f}")
    # Salvar
    with open("resultados_correlacao_abs_compacta/correlacao_vizinhos.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['N', 'k', 'frac_uncovered', 'corr_neighbors', 'cov_neighbors'])
        for r in resultados:
            writer.writerow([r['N'], r['k'], f"{r['frac_uncovered']:.6f}",
                             f"{r['corr_neighbors']:.6f}", f"{r['cov_neighbors']:.6f}"])
    print("\nResultados salvos em resultados_correlacao_abs_compacta/correlacao_vizinhos.csv")

if __name__ == "__main__":
    os.makedirs("resultados_correlacao_abs_compacta", exist_ok=True)
    main()