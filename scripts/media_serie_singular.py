# -*- coding: utf-8 -*-
"""
media_serie_singular.py
Calcula a média empírica da série singular 𝔖(6C) para C em [4, N].
Uso: python media_serie_singular.py --N 10000000 --step 1000
"""

import math
import argparse
import numpy as np

def singular_series(C):
    """Retorna 𝔖(6C) = ∏_{p|6C, p>2} (p-1)/(p-2)."""
    n = 6 * C
    s = 1.0
    temp = n
    # Remove fator 2
    while temp % 2 == 0:
        temp //= 2
    p = 3
    while p * p <= temp:
        if temp % p == 0:
            s *= (p - 1) / (p - 2)
            while temp % p == 0:
                temp //= p
        p += 2
    if temp > 2:
        s *= (temp - 1) / (temp - 2)
    return s

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=10_000_000, help="Limite superior de C")
    parser.add_argument("--step", type=int, default=1000, help="Passo de amostragem")
    parser.add_argument("--full", action="store_true", help="Varrer todos C (ignora step)")
    args = parser.parse_args()

    if args.full:
        C_vals = range(4, args.N + 1, 2)  # apenas C pares
    else:
        C_vals = range(4, args.N + 1, args.step)  # amostra C pares

    print(f"Calculando 𝔖(6C) para {len(C_vals)} valores de C...")
    s_vals = []
    for i, C in enumerate(C_vals):
        s_vals.append(singular_series(C))
        if (i+1) % 10000 == 0:
            print(f"Processados {i+1} C")
    mean_s = np.mean(s_vals)
    std_s = np.std(s_vals)
    print(f"Média empírica = {mean_s:.4f}  (±{std_s:.4f})")
    print(f"Valor esperado para c = 16*C2*⟨𝔖⟩: 16*0.66016*{mean_s:.4f} = {16*0.66016*mean_s:.2f}")


if __name__ == "__main__":
    main()