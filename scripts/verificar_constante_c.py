# -*- coding: utf-8 -*-
"""
Verificação computacional da constante c ≈ 21
Motor de Herança Estrutural — Tiago Bandeira, Maio 2026

Calcula:
1. Média empírica de S(6C) sobre os C testados
2. Densidade de âncoras por eixo (fração de E1 que funcionam)
3. Fração de janelas Wi ativas (pelo menos um eixo bom)
4. Verifica se c ≈ 16 * C2 * <S> com C2 = 0.6602

Saída: CSV com os resultados por faixa de C + síntese final
"""

import math
import numpy as np
import csv

# ── Parâmetros ────────────────────────────────────────────────────────────────
N_MAX = 500_000       # testa C pares de 4 até N_MAX (rápido; aumente se quiser)
BLOCO = 50_000        # tamanho dos blocos para análise por faixa
C2 = 0.6601618        # constante dos primos gêmeos

# ── Crivo ─────────────────────────────────────────────────────────────────────
def crivo(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[0:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    return sieve

# ── Série singular S(6C) ──────────────────────────────────────────────────────
def serie_singular(m, primos_pequenos):
    """
    S(m) = prod_{p | m, p > 2} (p-1)/(p-2)
    m deve ser par.
    """
    s = 1.0
    for p in primos_pequenos:
        if p * p > m:
            break
        if m % p == 0:
            s *= (p - 1) / (p - 2)
    return s

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print(f"Gerando crivo até {6 * N_MAX:,}...")
    ip = crivo(6 * N_MAX + 10)

    # Primos pequenos para série singular (até raiz de 6*N_MAX)
    raiz = int((6 * N_MAX)**0.5) + 1
    primos_pequenos = [p for p in range(3, raiz, 2) if ip[p]]

    print(f"Crivo pronto. Analisando C pares de 4 a {N_MAX:,}...\n")

    # Resultados por bloco
    resultados = []

    C_vals = np.arange(4, N_MAX + 1, 2)

    for bloco_ini in range(4, N_MAX + 1, BLOCO):
        bloco_fim = min(bloco_ini + BLOCO - 2, N_MAX)
        Cs = np.arange(bloco_ini, bloco_fim + 1, 2)
        if len(Cs) == 0:
            continue

        C_mid = int(np.median(Cs))
        logC = math.log(C_mid)
        log2C = logC ** 2

        # ── 1. Média de S(6C) no bloco ────────────────────────────────────────
        S_vals = [serie_singular(6 * C, primos_pequenos) for C in Cs[:500]]
        S_med = np.mean(S_vals)

        # ── 2. Densidade de âncoras por eixo ──────────────────────────────────
        # Para cada C, conta quantos E1 ímpares em [3, 3C] têm E1 primo e 6C-E1 primo
        # Amostra sobre primeiros 200 C do bloco para não ser lento
        n_ancora_total = 0
        n_eixos_total = 0
        n_janelas_total = 0
        n_janelas_ativas = 0

        for C in Cs[:200]:
            M = 6 * C
            if M + 1 >= len(ip):
                continue

            # Todos os E1 ímpares de 3 até M-3 (excluindo 1)
            E1s = np.arange(3, M - 2, 2)

            # Filtro: E1 primo e E2 = M - E1 primo
            mask_E1 = ip[E1s]
            E2s = M - E1s
            mask_E2 = (E2s >= 2) & (E2s < len(ip)) & ip[np.minimum(E2s, len(ip)-1)]
            mask_E2[E2s >= len(ip)] = False

            bons = mask_E1 & mask_E2
            n_bons = int(np.sum(bons))

            n_eixos = len(E1s)
            n_eixos_total += n_eixos
            n_ancora_total += n_bons

            # Janelas: grupos de 4 E1 consecutivos (ímpares consecutivos)
            # Janela j tem E1 in {2k-1, 2k+1, 2k+3, 2k+5}
            # Número de janelas = ceil(len(E1s) / 4)
            n_jan = (n_eixos + 3) // 4
            n_janelas_total += n_jan

            # Janela ativa se pelo menos um dos seus 4 eixos é bom
            ativa = 0
            for j in range(n_jan):
                ini = j * 4
                fim = min(ini + 4, len(bons))
                if np.any(bons[ini:fim]):
                    ativa += 1
            n_janelas_ativas += ativa

        # Densidades
        dens_ancora = n_ancora_total / n_eixos_total if n_eixos_total > 0 else 0
        frac_janelas = n_janelas_ativas / n_janelas_total if n_janelas_total > 0 else 0

        # c empírico = frac_janelas * log^2(C)
        c_emp = frac_janelas * log2C

        # c previsto = 16 * C2 * S_med
        c_prev = 16 * C2 * S_med

        # c via densidade de âncoras * 4 * log^2(C)
        c_ancora = dens_ancora * 4 * log2C

        resultados.append({
            'C_mid': C_mid,
            'logC': round(logC, 4),
            'S_med': round(S_med, 4),
            'dens_ancora': round(dens_ancora, 6),
            'frac_janelas': round(frac_janelas, 6),
            'c_empirico': round(c_emp, 4),
            'c_previsto_16C2S': round(c_prev, 4),
            'c_via_ancora_x4': round(c_ancora, 4),
        })

        print(f"C_mid={C_mid:>7,}  logC={logC:.3f}  "
              f"<S>={S_med:.4f}  "
              f"c_emp={c_emp:.3f}  "
              f"c_prev(16C2S)={c_prev:.3f}  "
              f"c_ancora*4={c_ancora:.3f}")

    # ── Síntese ───────────────────────────────────────────────────────────────
    print("\n" + "="*70)
    print("SÍNTESE")
    print("="*70)
    c_emps = [r['c_empirico'] for r in resultados if r['c_empirico'] > 0]
    c_prevs = [r['c_previsto_16C2S'] for r in resultados]
    c_ancoras = [r['c_via_ancora_x4'] for r in resultados if r['c_via_ancora_x4'] > 0]
    S_meds = [r['S_med'] for r in resultados]

    print(f"Média <S(6C)>         = {np.mean(S_meds):.4f}")
    print(f"Média c empírico      = {np.mean(c_emps):.4f}")
    print(f"Média c previsto      = {np.mean(c_prevs):.4f}  [16 * C2 * <S>]")
    print(f"Média c âncora*4      = {np.mean(c_ancoras):.4f}  [4 * dens_ancora * log^2 C]")
    print(f"Razão emp/previsto    = {np.mean(c_emps)/np.mean(c_prevs):.4f}")
    print(f"C2 usado              = {C2}")
    print(f"16 * C2 * <S_med>     = {16 * C2 * np.mean(S_meds):.4f}")

    # Salva CSV
    with open('verificacao_constante_c.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=resultados[0].keys())
        writer.writeheader()
        writer.writerows(resultados)
    print("\nResultados salvos em 'verificacao_constante_c.csv'")

if __name__ == "__main__":
    main()
