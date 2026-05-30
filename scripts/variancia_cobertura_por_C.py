# -*- coding: utf-8 -*-
"""
Script: variancia_cobertura_por_C.py
Objetivo: Calcular a variância empírica do número de âncoras que cobrem cada C
e comparar com a variância teórica sob independência e com a variância derivada
da matriz de correlação.
Autor: Tiago Bandeira
Data: Maio 2026
"""

import numpy as np
import time
import csv
import os
from collections import Counter

# Parâmetros
LIMITES_N = [1_000_000, 10_000_000]
ANCORA_MAX_BUSCA = 5000

def crivo(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[0:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    return sieve

def coberturas_por_C(ancoras, N, ip):
    """Retorna um array counts[0..n_C-1] onde cada entrada é o número de âncoras que cobrem aquele C."""
    n_C = N // 2 - 1   # C = 4,6,8,...,N
    counts = np.zeros(n_C, dtype=np.int32)
    # Para cada âncora, determinar os C cobertos e incrementar
    for p in ancoras:
        q_min = max(2, 6*4 - p)
        q_max = min(6*N - p, len(ip)-1)
        if q_max < q_min:
            continue
        pos = q_min
        FATIA = 10_000_000
        while pos <= q_max:
            fim = min(pos + FATIA, q_max + 1)
            qs = np.where(ip[pos:fim])[0] + pos
            num = qs + p
            mask = (num % 6 == 0)
            Cs = (num[mask] // 6).astype(np.int64)
            Cs = Cs[(Cs % 2 == 0) & (Cs >= 4) & (Cs <= N)]
            idx = (Cs - 4) // 2
            counts[idx] += 1
            pos = fim
    return counts

def main():
    os.makedirs("resultados_correlacao_abs_compacta", exist_ok=True)
    # Arquivo CSV para salvar resultados (cria cabeçalho se não existir)
    csv_path = "resultados_correlacao_abs_compacta/variancia_cobertura.csv"
    file_exists = os.path.isfile(csv_path)
    
    for N in LIMITES_N:
        print(f"\n=== N = {N:,} ===")
        t0 = time.time()

        # Carregar âncoras (absolutas)
        ancoras_file = f"resultados_correlacao_abs_compacta/ancoras_N{N}.csv"
        if not os.path.exists(ancoras_file):
            print(f"  Arquivo de âncoras não encontrado: {ancoras_file}")
            continue
        ancoras = []
        with open(ancoras_file, 'r') as f:
            next(f)  # cabeçalho
            for line in f:
                _, p = line.strip().split(',')
                ancoras.append(int(p))
        print(f"  Âncoras carregadas: {len(ancoras)}")

        # Construir crivo
        tam = 6 * N + ANCORA_MAX_BUSCA + 10
        ip = crivo(tam)

        # Obter contagens por C
        counts = coberturas_por_C(ancoras, N, ip)
        n_C = len(counts)
        print(f"  Total de C pares: {n_C}")

        # Estatísticas empíricas
        mean_emp = np.mean(counts)
        var_emp = np.var(counts, ddof=1)  # amostral
        print(f"  Média empírica: {mean_emp:.6f}")
        print(f"  Variância empírica: {var_emp:.6f}")

        # Calcular probabilidades individuais p_i para cada âncora
        print("  Calculando probabilidades individuais das âncoras...")
        p_i_emp = np.zeros(len(ancoras))
        for idx, p in enumerate(ancoras):
            q_min = max(2, 6*4 - p)
            q_max = min(6*N - p, len(ip)-1)
            if q_max < q_min:
                continue
            n_covered = 0
            pos = q_min
            while pos <= q_max:
                fim = min(pos + 10_000_000, q_max + 1)
                qs = np.where(ip[pos:fim])[0] + pos
                num = qs + p
                mask = (num % 6 == 0)
                Cs = (num[mask] // 6).astype(np.int64)
                Cs = Cs[(Cs % 2 == 0) & (Cs >= 4) & (Cs <= N)]
                n_covered += len(Cs)
                pos = fim
            p_i_emp[idx] = n_covered / n_C
        print(f"  Média dos p_i: {np.mean(p_i_emp):.6f}")

        # Variância sob independência (cov=0)
        var_indep = np.sum(p_i_emp * (1 - p_i_emp))
        print(f"  Variância assumindo independência: {var_indep:.6f}")

        # Carregar matriz de correlação para calcular variância com covariâncias
        corr_file = f"resultados_correlacao_abs_compacta/corr_N{N}.npy"
        var_corr = None
        if os.path.exists(corr_file):
            corr_mat = np.load(corr_file)
            # Calcular desvios padrão
            std_i = np.sqrt(p_i_emp * (1 - p_i_emp))
            # Matriz de covariância
            cov_mat = corr_mat * np.outer(std_i, std_i)
            # Variância total: soma de todos os elementos
            var_corr = np.sum(cov_mat)
            print(f"  Variância a partir da matriz de correlação: {var_corr:.6f}")
            print(f"  Diferença (empírica - corr): {var_emp - var_corr:.6e}")
            print(f"  Razão empírica / corr: {var_emp/var_corr:.4f}")
        else:
            print("  Matriz de correlação não encontrada, pulando.")

        # Salvar resultados
        with open(csv_path, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["N", "n_ancoras", "n_C", "mean_emp", "var_emp", "var_indep", "var_corr"])
                file_exists = True
            writer.writerow([N, len(ancoras), n_C, mean_emp, var_emp, var_indep, var_corr if var_corr is not None else ''])

        print(f"  Tempo total: {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()