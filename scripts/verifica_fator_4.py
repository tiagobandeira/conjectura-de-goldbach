# -*- coding: utf-8 -*-
"""
verifica_fator_4.py
Para um N fixo, calcula good_axes_count e active_windows para C = N//2.
Uso: python verifica_fator_4.py --N 10000000
"""

import math
import numpy as np
import time
import argparse

def crivo_ate(limite):
    """Crivo de Eratóstenes até limite."""
    sieve = np.ones(limite + 1, dtype=bool)
    sieve[0:2] = False
    for i in range(2, int(limite**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    return sieve

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=10_000_000, help="Limite superior de C")
    args = parser.parse_args()

    N = args.N
    C = N // 2   # escolhe um C típico
    print(f"Verificando para N = {N:,} (C = {C})")

    # Crivo para primos até 6*C + margem
    max_q = 6 * C + 1000
    print(f"Construindo crivo até {max_q:,}...")
    t0 = time.time()
    is_prime = crivo_ate(max_q)
    print(f"Crivo pronto em {time.time()-t0:.1f}s")

    # Lista de âncoras (primos >=5 até 6*C)
    ancoras = [p for p in range(5, max_q+1) if is_prime[p]]
    print(f"Total de âncoras: {len(ancoras)}")

    # Para o C fixo, vamos coletar as âncoras que funcionam
    good_axes = []  # lista de p que funcionam
    for p in ancoras:
        q = 6 * C - p
        if q > 1 and is_prime[q]:
            good_axes.append(p)

    good_axes_count = len(good_axes)
    print(f"Número de eixos bons (âncoras) para C={C}: {good_axes_count}")

    # Mapear cada boa âncora para a janela W_j
    # j = ceil((p+1)/8)
    windows = set()
    for p in good_axes:
        j = (p + 7) // 8   # ceil((p+1)/8)
        windows.add(j)
    active_windows = len(windows)

    total_windows = (N // 4) - (1 if N % 4 != 0 else 0)  # número de janelas até C=N
    total_axes = 4 * total_windows

    print(f"Janelas ativas: {active_windows} de {total_windows} (fração = {active_windows/total_windows:.6f})")
    print(f"Densidade de eixos bons: {good_axes_count}/{total_axes} = {good_axes_count/total_axes:.6f}")
    print(f"Razão (janelas ativas)/(densidade de eixos) = {active_windows} / ({good_axes_count/total_axes}) = {active_windows / (good_axes_count/total_axes):.2f}")
    print(f"Razão esperada (se cada janela tivesse no máximo um eixo bom) ≈ 4 * total_windows = {4*total_windows}")
    print(f"good_axes_count ≈ {good_axes_count}, active_windows ≈ {active_windows} (diferença = {good_axes_count - active_windows})")

if __name__ == "__main__":
    main()