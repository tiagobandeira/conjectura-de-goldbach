# -*- coding: utf-8 -*-
"""
Script: analise_correlacao_excluindo_ancoras.py
Objetivo: Carregar as matrizes de correlação já calculadas para N=1e6 e N=1e7,
e calcular estatísticas excluindo as primeiras k âncoras (k=10,20,30).
Autor: Tiago Bandeira
Data: Maio 2026
"""

import numpy as np
import csv
import os

# Diretório onde estão as matrizes e listas de âncoras
DATA_DIR = "resultados_correlacao_abs_compacta"

# Lista de N a processar
Ns = [1_000_000, 10_000_000]

# Número de âncoras a excluir do início
EXCLUIR_LIST = [0, 10, 20, 30]   # 0 significa matriz completa

def estatisticas_matriz(corr_mat):
    """Retorna média, max, min, std dos elementos off‑diagonal (triângulo superior)."""
    n = corr_mat.shape[0]
    mask = np.triu(np.ones_like(corr_mat, dtype=bool), k=1)
    off = corr_mat[mask]
    return np.mean(off), np.max(off), np.min(off), np.std(off)

def main():
    resultados = []
    for N in Ns:
        # Carregar matriz de correlação
        corr_file = os.path.join(DATA_DIR, f"corr_N{N}.npy")
        if not os.path.exists(corr_file):
            print(f"Arquivo não encontrado: {corr_file}")
            continue
        corr = np.load(corr_file)
        n_total = corr.shape[0]
        print(f"\nN = {N}: matriz {n_total}x{n_total} carregada.")

        for excl in EXCLUIR_LIST:
            if excl >= n_total:
                continue
            # Extrair submatriz excluindo as primeiras 'excl' linhas/colunas
            sub_corr = corr[excl:, excl:]
            n_sub = sub_corr.shape[0]
            if n_sub < 2:
                continue
            mean_off, max_off, min_off, std_off = estatisticas_matriz(sub_corr)
            # Calcular autovalores da submatriz
            eigvals = np.linalg.eigvalsh(sub_corr)
            max_eig = np.max(eigvals)
            resultados.append({
                'N': N,
                'excluir': excl,
                'n_restantes': n_sub,
                'mean_corr': mean_off,
                'max_corr': max_off,
                'min_corr': min_off,
                'std_corr': std_off,
                'max_eigenvalue': max_eig
            })
            print(f"  excluindo {excl} primeiras: n={n_sub}, mean_corr={mean_off:.6f}, "
                  f"max_eig={max_eig:.4f}")

    # Salvar resultados em CSV
    out_csv = os.path.join(DATA_DIR, "resumo_excluindo_ancoras.csv")
    with open(out_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['N', 'excluir', 'n_restantes', 'mean_corr', 'max_corr',
                         'min_corr', 'std_corr', 'max_eigenvalue'])
        for r in resultados:
            writer.writerow([r['N'], r['excluir'], r['n_restantes'],
                             f"{r['mean_corr']:.6f}", f"{r['max_corr']:.6f}",
                             f"{r['min_corr']:.6f}", f"{r['std_corr']:.6f}",
                             f"{r['max_eigenvalue']:.4f}"])

    print(f"\nResultados salvos em {out_csv}")

if __name__ == "__main__":
    main()