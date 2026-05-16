#!/usr/bin/env python3
"""
crivo_geometrico.py
─────────────────────────────────────────────────────────────────
Verificação computacional do Crivo Geométrico (Bandeira 2026)

Hipótese central testada:
  Primos (P1) e semiprimos (P2) induzem distribuições distintas
  do peso geométrico ΩN(n) na grade G_{3,N}.

  Se verdadeiro: a grade consegue discriminar P1 de P2 sem usar
  primalidade diretamente — o que seria a propriedade essencial
  de um crivo parity-free.

Uso:
  python crivo_geometrico.py           # N=1000 (rápido, ~5s)
  python crivo_geometrico.py --N 3000  # N=3000 (moderado, ~30s)
  python crivo_geometrico.py --N 200 --show_grid  # grade pequena + diagnóstico
─────────────────────────────────────────────────────────────────
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import stats
from collections import defaultdict
import argparse
import time


# ══════════════════════════════════════════════════════════════
# 1. TEORIA DOS NÚMEROS — crivo e classificação
# ══════════════════════════════════════════════════════════════

def sieve_eratosthenes(limit):
    """Crivo de Eratóstenes. Retorna is_prime[i] para i in 0..limit."""
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            is_prime[p * p :: p] = False
    return is_prime


def spf_sieve(limit):
    """
    Menor fator primo (Smallest Prime Factor).
    spf[n] = menor primo que divide n.
    Permite fatorar n em O(log n) sem divisão de tentativa.
    """
    spf = list(range(limit + 1))
    for p in range(2, int(limit**0.5) + 1):
        if spf[p] == p:          # p é primo
            for m in range(p * p, limit + 1, p):
                if spf[m] == m:  # ainda não tem fator menor
                    spf[m] = p
    return spf


def count_prime_factors_with_mult(n, spf):
    """
    Conta fatores primos de n com multiplicidade (Omega(n)).
    Exemplos: 4=2² → 2, 6=2·3 → 2, 12=2²·3 → 3, 30=2·3·5 → 3
    """
    if n <= 1:
        return 0
    count = 0
    while n > 1:
        p = spf[n]
        while n % p == 0:
            n //= p
            count += 1
    return count


def classify_all(values, is_prime, spf):
    """
    Classifica cada inteiro em:
      'P1'        — primo
      'P2'        — exatamente 2 fatores primos (com mult.): semiprimo ou p²
      'composite' — 3+ fatores primos
      'other'     — n < 2 (inclui 1)
    """
    labels = {}
    for n in values:
        n = int(n)
        if n < 2:
            labels[n] = 'other'
        elif is_prime[n]:
            labels[n] = 'P1'
        elif count_prime_factors_with_mult(n, spf) == 2:
            labels[n] = 'P2'
        else:
            labels[n] = 'composite'
    return labels


# ══════════════════════════════════════════════════════════════
# 2. GRADE G_{3,N} e JANELAS 3×3
# ══════════════════════════════════════════════════════════════

def build_grid(N):
    """
    Constrói G_{3,N}: matriz 3×N de ímpares consecutivos.

    Fórmula (0-indexado): grid[r][c] = 2*(r*N + c + 1) - 1
      Linha 0: 1,  3,  ..., 2N-1
      Linha 1: 2N+1, ..., 4N-1
      Linha 2: 4N+1, ..., 6N-1
    """
    r_idx = np.arange(3).reshape(3, 1)
    c_idx = np.arange(N).reshape(1, N)
    return (2 * (r_idx * N + c_idx + 1) - 1).astype(np.int64)


def detect_prime_triples(grid, is_prime):
    """
    Conta janelas Wi com pelo menos uma configuração totalmente prima.
    Configurações (0-indexado em colunas i, i+1, i+2):
      D1: (0,i), (1,i+1), (2,i+2)   — diagonal principal
      D2: (2,i), (1,i+1), (0,i+2)   — diagonal secundária
      Cv: (0,i+1), (1,i+1), (2,i+1) — coluna central
    Retorna (n_successes, trio_list)
    """
    N = grid.shape[1]
    successes = 0
    trios = []

    for i in range(N - 2):
        d1 = [grid[0, i], grid[1, i+1], grid[2, i+2]]
        d2 = [grid[2, i], grid[1, i+1], grid[0, i+2]]
        cv = [grid[0, i+1], grid[1, i+1], grid[2, i+1]]

        hit = False
        for config, name in [(d1, 'D1'), (d2, 'D2'), (cv, 'Cv')]:
            if all(is_prime[v] for v in config):
                trios.append((i, name, tuple(config)))
                hit = True
        if hit:
            successes += 1

    return successes, trios


# ══════════════════════════════════════════════════════════════
# 3. PESO GEOMÉTRICO ΩN(n)
# ══════════════════════════════════════════════════════════════

def compute_omega(grid, is_prime):
    """
    Computa ΩN(n) para cada célula da grade.

    Definição (Eq. 6 do paper):
      Para cada janela Wi contendo n, conta quantos dos 8 vizinhos
      na janela são primos, e normaliza por 8.
      ΩN(n) = média dessas frações sobre todas as janelas contendo n.

    ΩN(n) ∈ [0, 1].
    Intuitivamente: "campo gravitacional primo" ao redor de n — medido
    sem usar a primalidade do próprio n.
    """
    N = grid.shape[1]
    omega = np.zeros((3, N), dtype=float)

    # Pré-computa primalidade de cada célula para acesso O(1)
    prime_mask = is_prime[grid]  # shape (3, N), dtype bool

    for c in range(N):
        # Janelas que contêm a coluna c: i ∈ [c-2, c] ∩ [0, N-3]
        i_min = max(0, c - 2)
        i_max = min(N - 3, c)

        for r in range(3):
            fractions = []
            for i in range(i_min, i_max + 1):
                # 9 células da janela Wi, colunas i..i+2
                win_primes = prime_mask[:, i:i+3]   # shape (3,3)
                total_neighbors = 8

                # Remove a contribuição do próprio n
                n_in_win = prime_mask[r, c]
                prime_count_with_n = win_primes.sum()
                prime_neighbors = int(prime_count_with_n) - int(n_in_win)

                fractions.append(prime_neighbors / total_neighbors)

            omega[r, c] = np.mean(fractions)

    return omega


# ══════════════════════════════════════════════════════════════
# 4. ANÁLISE ESTATÍSTICA
# ══════════════════════════════════════════════════════════════

def collect_by_class(grid, omega, labels):
    """Agrupa valores de ΩN(n) por classe."""
    result = defaultdict(list)
    for r in range(3):
        for c in range(grid.shape[1]):
            n = int(grid[r, c])
            cls = labels.get(n)
            if cls in ('P1', 'P2', 'composite'):
                result[cls].append(omega[r, c])
    return {k: np.array(v) for k, v in result.items()}


def print_report(by_class, N, n_successes, trios, t_elapsed):
    SEP = '═' * 65
    print(f"\n{SEP}")
    print(f"  CRIVO GEOMÉTRICO — G_{{3,{N}}}  (n ≤ {6*N-1})")
    print(SEP)

    print(f"\n  Tempo de execução: {t_elapsed:.1f}s")
    print(f"  Janelas totais: {N-2}  |  Janelas com trio primo: {n_successes}")
    print(f"  Taxa de sucesso empírica: {n_successes/(N-2):.4f}")
    ku_teorico = 8 * N / (np.log(N) ** 3)
    print(f"  Ku teórico ≈ {ku_teorico:.1f}  (fórmula 8N/(ln N)³)")

    if trios:
        print(f"\n  Primeiros 5 trios primos encontrados:")
        for i, (win_i, name, vals) in enumerate(trios[:5]):
            print(f"    janela i={win_i:4d}  {name}: {vals}")

    print(f"\n{'─'*65}")
    print(f"  {'Classe':<12} {'Contagem':<10} {'Média ΩN':<12} {'Mediana':<12} {'Std'}")
    print(f"{'─'*65}")
    for cls in ('P1', 'P2', 'composite'):
        v = by_class.get(cls, np.array([]))
        if len(v):
            print(f"  {cls:<12} {len(v):<10} {v.mean():<12.5f} "
                  f"{np.median(v):<12.5f} {v.std():.5f}")

    # Testes estatísticos
    p1 = by_class.get('P1', np.array([]))
    p2 = by_class.get('P2', np.array([]))
    comp = by_class.get('composite', np.array([]))

    print(f"\n{'─'*65}")
    print("  TESTES DE HIPÓTESE")
    print(f"{'─'*65}")

    if len(p1) > 1 and len(p2) > 1:
        ks, pval = stats.ks_2samp(p1, p2)
        mw_stat, mw_p = stats.mannwhitneyu(p1, p2, alternative='two-sided')
        print(f"  P1 vs P2  |  KS={ks:.4f}  p={pval:.2e}  "
              f"|  Mann-Whitney p={mw_p:.2e}")
        if pval < 0.05:
            print("  ✓ Distribuições significativamente diferentes (p < 0.05)")
            print("  → Consistente com a hipótese do crivo geométrico")
            if p1.mean() > p2.mean():
                delta = (p1.mean() - p2.mean()) / p2.std() if p2.std() > 0 else 0
                print(f"  → P1 tem ΩN médio maior que P2 (Cohen d ≈ {delta:.3f})")
        else:
            print("  ✗ Sem diferença significativa detectada para este N")

    if len(p1) > 1 and len(comp) > 1:
        ks2, pval2 = stats.ks_2samp(p1, comp)
        print(f"  P1 vs comp|  KS={ks2:.4f}  p={pval2:.2e}")

    print(SEP)


# ══════════════════════════════════════════════════════════════
# 5. VISUALIZAÇÃO
# ══════════════════════════════════════════════════════════════

COLORS = {
    'P1':        '#27ae60',   # verde — primos
    'P2':        '#e74c3c',   # vermelho — semiprimos
    'composite': '#7f8c8d',   # cinza — compostos
}

def plot_results(by_class, N, omega, grid, labels, trios):
    fig = plt.figure(figsize=(17, 11))
    fig.suptitle(
        f'Crivo Geométrico  —  $G_{{3,{N}}}$,  $n \\leq {6*N-1}$',
        fontsize=14, fontweight='bold', y=0.98
    )
    gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.42, wspace=0.35)

    # ── Plot 1: Histogramas sobrepostos ──────────────────────
    ax1 = fig.add_subplot(gs[0, :2])
    for cls in ('P1', 'P2', 'composite'):
        v = by_class.get(cls, [])
        if len(v):
            ax1.hist(v, bins=45, alpha=0.55, color=COLORS[cls],
                     label=f'{cls} (n={len(v)})', density=True)
    ax1.set_xlabel('$\\Omega_N(n)$', fontsize=11)
    ax1.set_ylabel('Densidade', fontsize=11)
    ax1.set_title('Distribuição de $\\Omega_N$ por classe')
    ax1.legend(fontsize=9)
    ax1.grid(alpha=0.25)

    # ── Plot 2: KDE P1 vs P2 ─────────────────────────────────
    ax2 = fig.add_subplot(gs[0, 2])
    for cls in ('P1', 'P2'):
        v = np.array(by_class.get(cls, []))
        if len(v) > 20:
            kde = stats.gaussian_kde(v, bw_method='scott')
            x = np.linspace(0, max(v) * 1.05, 400)
            ax2.plot(x, kde(x), color=COLORS[cls], lw=2.2, label=cls)
            ax2.axvline(v.mean(), color=COLORS[cls], lw=1, ls='--', alpha=0.7)
    ax2.set_xlabel('$\\Omega_N(n)$', fontsize=11)
    ax2.set_title('KDE suavizado: P1 vs P2\n(tracejado = média)')
    ax2.legend(fontsize=10)
    ax2.grid(alpha=0.25)

    # ── Plot 3: Boxplot ──────────────────────────────────────
    ax3 = fig.add_subplot(gs[1, 0])
    data_box = [by_class.get(c, []) for c in ('P1', 'P2', 'composite')]
    bp = ax3.boxplot(data_box, labels=['P1', 'P2', 'comp.'],
                     patch_artist=True, notch=True,
                     medianprops=dict(color='black', lw=2))
    for patch, cls in zip(bp['boxes'], ('P1', 'P2', 'composite')):
        patch.set_facecolor(COLORS[cls])
        patch.set_alpha(0.65)
    ax3.set_ylabel('$\\Omega_N(n)$', fontsize=11)
    ax3.set_title('Boxplot por classe\n(entalhe = IC mediana 95%)')
    ax3.grid(alpha=0.25)

    # ── Plot 4: ΩN vs magnitude de n ─────────────────────────
    ax4 = fig.add_subplot(gs[1, 1:])
    for cls in ('composite', 'P2', 'P1'):  # P1 por cima
        ns, ws = [], []
        for r in range(3):
            for c in range(grid.shape[1]):
                n = int(grid[r, c])
                if labels.get(n) == cls:
                    ns.append(n)
                    ws.append(omega[r, c])
        if ns:
            ax4.scatter(ns, ws, c=COLORS[cls], alpha=0.25, s=3, label=cls, rasterized=True)

    # Marca os trios encontrados
    for win_i, name, vals in trios[:50]:
        ax4.axvline(vals[0], color='gold', alpha=0.15, lw=0.8)

    ax4.set_xlabel('Valor de $n$', fontsize=11)
    ax4.set_ylabel('$\\Omega_N(n)$', fontsize=11)
    ax4.set_title('$\\Omega_N(n)$ vs magnitude\n(linhas douradas = trios primos)')
    ax4.legend(markerscale=4, fontsize=9)
    ax4.grid(alpha=0.2)

    fname = f'omega_N{N}.png'
    plt.savefig(fname, dpi=150, bbox_inches='tight')
    plt.show()
    print(f"\n  Gráfico salvo em: {fname}")


def plot_density_decay(N_values=(200, 500, 1000, 2000)):
    """
    Plot adicional: decaimento de Ku empírico vs teórico 8N/(ln N)³
    para verificar a ordem de crescimento assintótico.
    """
    print("\n  Computando decaimento de Ku para múltiplos N...")
    ku_emp, ku_teo = [], []

    for N in N_values:
        limit = 6 * N
        is_prime = sieve_eratosthenes(limit)
        grid = build_grid(N)
        n_succ, _ = detect_prime_triples(grid, is_prime)
        ku_emp.append(n_succ)
        ku_teo.append(8 * N / (np.log(N) ** 3))
        print(f"    N={N:5d}: Ku_emp={n_succ:5d}  Ku_teo={ku_teo[-1]:.1f}")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(N_values, ku_teo, 'k--', lw=2, label='Ku teórico: $8N/(\\ln N)^3$')
    ax.plot(N_values, ku_emp, 'o-', color='#2980b9', lw=2, ms=7, label='Ku empírico')
    ax.set_xlabel('N', fontsize=12)
    ax.set_ylabel('Ku', fontsize=12)
    ax.set_title('Crescimento assintótico de $K_u$ — empírico vs teórico')
    ax.legend(fontsize=11)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('ku_decay.png', dpi=150)
    plt.show()
    print("  Gráfico salvo em: ku_decay.png")


# ══════════════════════════════════════════════════════════════
# 6. MAIN
# ══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='Crivo Geométrico — verificação computacional (Bandeira 2026)'
    )
    parser.add_argument('--N', type=int, default=1000,
        help='Colunas da grade G_{3,N} (default: 1000, máx recomendado: 5000)')
    parser.add_argument('--show_grid', action='store_true',
        help='Imprime a grade completa (use apenas para N pequeno, ≤ 20)')
    parser.add_argument('--decay', action='store_true',
        help='Plota curva de decaimento de Ku para N em {200,500,1000,2000}')
    args = parser.parse_args()

    N = args.N
    t0 = time.time()
    limit = 6 * N

    print(f"\n  Construindo G_{{3,{N}}} — valores até {limit - 1}")
    print(f"  Crivo de Eratóstenes até {limit}...")
    is_prime = sieve_eratosthenes(limit)
    spf = spf_sieve(limit)

    grid = build_grid(N)

    if args.show_grid and N <= 20:
        print(f"\n  Grade G_{{3,{N}}}:")
        for r in range(3):
            row = [f"{grid[r,c]:4d}" for c in range(N)]
            print(f"  Linha {r+1}: {' '.join(row)}")

    all_vals = set(int(v) for v in grid.flatten())
    labels = classify_all(all_vals, is_prime, spf)

    print("  Detectando trios primos nas janelas 3×3...")
    n_successes, trios = detect_prime_triples(grid, is_prime)

    print("  Computando ΩN(n) para todas as células...")
    omega = compute_omega(grid, is_prime)

    by_class = collect_by_class(grid, omega, labels)

    t_elapsed = time.time() - t0
    print_report(by_class, N, n_successes, trios, t_elapsed)
    plot_results(by_class, N, omega, grid, labels, trios)

    if args.decay:
        plot_density_decay()


if __name__ == '__main__':
    main()
