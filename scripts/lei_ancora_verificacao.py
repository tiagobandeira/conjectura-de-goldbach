# -*- coding: utf-8 -*-
"""Verificação independente da lei da âncora (Papers 10 e 11).

Define, para n par,

    g(n) = min{ p primo : n - p primo }

(o menor membro de uma partição de Goldbach) e mede

    M(N)   = max_{n <= N}          g(n)     (todos os pares)
    M12(N) = max_{n <= 6N, n=0(12)} g(n)    (domínio real do script de cobertura)

Este script reproduz a Subsecção 3.5 do Paper 10:

  * no domínio n = 0 (mod 12), as leis 11,8 log N log log N batem com a tabela
    do paper (dentro de um passo de âncora);
  * fora do domínio, a lei falha: g(60 119 912) = 1093, contra 578 previstos;
  * sobre todos os pares, a ordem observada é log^2 N log log N (~1), não
    log N log log N.

Uso:
    python lei_ancora_verificacao.py [N_MAX]      (default: 10^7)
"""
import math
import sys

import numpy as np


def crivo(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            s[i * i :: i] = False
    return s


def g_de(n, s):
    """Menor primo p com n - p primo (n par)."""
    for p in range(3, n):
        if s[p] and s[n - p]:
            return p
    return None


def maximo_em(s, alvo_max, passo, resto):
    """max g(n) para n <= alvo_max com n % passo == resto."""
    inicio = resto if resto else passo
    mx, arg = 0, 0
    for n in range(inicio, alvo_max + 1, passo):
        if n < 4 or n % 2:
            continue
        v = g_de(n, s)
        if v is not None and v > mx:
            mx, arg = v, n
    return mx, arg


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000_000
    L = max(6 * N + 10, 60119912 + 2)
    s = crivo(L)

    print(f"crivo ate {L:,}")
    print()
    print("=== 1. todos os pares: M(N) = max g(n), n <= N ===")
    print(f"{'N':>12} {'M(N)':>7} {'M/(logN*llogN)':>16} {'M/(log2N*llogN)':>17}")
    for k in range(3, int(math.log10(N)) + 1):
        Nk = 10**k
        if Nk > N:
            break
        mx, _ = maximo_em(s, Nk, 1, 0)
        ln, lln = math.log(Nk), math.log(math.log(Nk))
        print(f"{Nk:>12,} {mx:>7} {mx/(ln*lln):>16.2f} {mx/(ln*ln*lln):>17.2f}")

    print()
    print("=== 2. dominio do script de cobertura: n = 6C, C par, C <= N ===")
    print(f"{'N':>12} {'M12(N)':>7} {'A efetivo':>10}")
    for k in range(6, int(math.log10(N)) + 1):
        Nk = 10**k
        if 6 * Nk > L:
            break
        mx, _ = maximo_em(s, 6 * Nk, 12, 0)
        ln, lln = math.log(Nk), math.log(math.log(Nk))
        print(f"{Nk:>12,} {mx:>7} {mx/(ln*lln):>10.2f}")

    print()
    print("=== 3. contraexemplo fora do dominio ===")
    n = 60119912
    if n <= L:
        v = g_de(n, s)
        pred = 11.8 * math.log(n / 2) * math.log(math.log(n / 2))
        print(f"n = {n:,} = {n % 12} (mod 12),  g(n) = {v},  11.8*logM*loglogM ~ {pred:.0f}")
        print(f"razao = {v/pred:.2f}")


if __name__ == "__main__":
    main()
