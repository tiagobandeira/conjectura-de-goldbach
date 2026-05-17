#!/usr/bin/env python3
"""
crivo_geometrico_v2.py
─────────────────────────────────────────────────────────────────
Verificação computacional do Crivo Geométrico (Bandeira 2026)

NOVIDADE v2: testa em paralelo dois pesos geométricos:

  ΩN(n)  — original, oracle-based:
    conta vizinhos primos de n na grade (usa is_prime diretamente).

  Ω*N(n) — NOVO, oracle-free:
    usa o Invariante Âncora da janela Wi:
      S(i) = 3(2N + 2i + 3)   [0-indexado]
      C(n,i) = S(i) - n        [sempre par, pois S e n são ímpares]
      𝔖(C) = ∏_{p|C, p>2} (p-1)/(p-2)   [Série Singular de Hardy-Littlewood]
    Ω*N(n) = média de 𝔖(C(n,i)) sobre janelas contendo n.
    
    Ω*N(n) NÃO usa primalidade de nenhum vizinho — só aritmética
    de C, que é determinado pela posição de n na grade.

Hipótese testada:
  Ω*N(n) preserva o poder discriminante de ΩN(n) (P1 vs P2),
  mesmo sem oracle de primalidade.

  Se verdadeiro: o invariante âncora é suficiente para construir
  um crivo parity-free computável a priori.

Uso:
  python crivo_geometrico_v2.py              # N=1000
  python crivo_geometrico_v2.py --N 30030   # primorial p6#
  python crivo_geometrico_v2.py --N 200 --show_grid
  python crivo_geometrico_v2.py --decay
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
# 1. TEORIA DOS NÚMEROS
# ══════════════════════════════════════════════════════════════

def sieve_eratosthenes(limit):
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            is_prime[p * p :: p] = False
    return is_prime


def spf_sieve(limit):
    """Menor fator primo — fatoração em O(log n)."""
    spf = list(range(limit + 1))
    for p in range(2, int(limit**0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, limit + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def count_prime_factors_with_mult(n, spf):
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
# 2. INVARIANTE ÂNCORA E SÉRIE SINGULAR
# ══════════════════════════════════════════════════════════════

def anchor_sum(N, i_code):
    """
    S(i) = soma constante das 3 configurações na janela i (0-indexado).
    Do Lema 1 do paper da soma constante:
      S = 3(2N + 2i + 1)  [i 1-indexado]
    Em 0-indexado (i_code = i_paper - 1):
      S = 3(2N + 2*i_code + 3)
    
    Propriedade central: f(2, i_code+1) = (2N + 2*i_code + 3) = S/3.
    O elemento da Row 2 é exatamente 1/3 da soma — o âncora.
    """
    return 3 * (2 * N + 2 * i_code + 3)


def singular_series(C, spf, spf_limit):
    """
    𝔖(C) = ∏_{p | C, p > 2} (p-1)/(p-2)

    Série Singular de Hardy-Littlewood — fator local para Goldbach em C.
    Computável apenas da fatoração de C, sem oracle de primalidade.

    Propriedade chave de paridade:
      𝔖(C) é MULTIPLICATIVO em C, não em n.
      Logo não herda a cegueira do crivo de Selberg (que é multiplicativo em n).
      Um P1 e um P2 que somam a mesma coisa têm 𝔖 diferentes pelos fatores distintos.
    """
    if C <= 2 or C >= spf_limit:
        return 1.0  # fallback neutro

    result = 1.0
    temp = abs(int(C))
    seen = set()
    while temp > 1:
        p = spf[temp]
        if p > 2 and p not in seen:
            result *= (p - 1) / (p - 2)
            seen.add(p)
        while temp % p == 0:
            temp //= p
    return result


# ══════════════════════════════════════════════════════════════
# 3. GRADE G_{3,N} E JANELAS 3×3
# ══════════════════════════════════════════════════════════════

def build_grid(N):
    r_idx = np.arange(3).reshape(3, 1)
    c_idx = np.arange(N).reshape(1, N)
    return (2 * (r_idx * N + c_idx + 1) - 1).astype(np.int64)


def detect_prime_triples(grid, is_prime):
    N = grid.shape[1]
    successes = 0
    trios = []
    for i in range(N - 2):
        d1 = [grid[0, i], grid[1, i+1], grid[2, i+2]]
        d2 = [grid[2, i], grid[1, i+1], grid[0, i+2]]
        cv = [grid[0, i+1], grid[1, i+1], grid[2, i+1]]
        hit = False
        for config, name in [(d1,'D1'), (d2,'D2'), (cv,'Cv')]:
            if all(is_prime[v] for v in config):
                trios.append((i, name, tuple(config)))
                hit = True
        if hit:
            successes += 1
    return successes, trios


# ══════════════════════════════════════════════════════════════
# 4. PESOS GEOMÉTRICOS
# ══════════════════════════════════════════════════════════════

def compute_omega(grid, is_prime):
    """
    ΩN(n) — ORIGINAL, oracle-based.
    Fração média de vizinhos primos nas janelas de n.
    Usa is_prime diretamente: não é computável a priori.
    """
    N = grid.shape[1]
    omega = np.zeros((3, N), dtype=float)
    prime_mask = is_prime[grid]

    for c in range(N):
        i_min = max(0, c - 2)
        i_max = min(N - 3, c)
        for r in range(3):
            fractions = []
            for i in range(i_min, i_max + 1):
                win_primes = prime_mask[:, i:i+3]
                n_in_win = prime_mask[r, c]
                prime_neighbors = int(win_primes.sum()) - int(n_in_win)
                fractions.append(prime_neighbors / 8)
            omega[r, c] = np.mean(fractions)
    return omega


def compute_omega_star(grid, spf, spf_limit, N):
    """
    Ω*N(n) — NOVO, oracle-free.

    Para cada célula n em (r, c) e cada janela i contendo n:
      C(n, i) = S(i) - n    onde S(i) = âncora da janela i
      peso(i) = 𝔖(C(n,i))  — Série Singular de Hardy-Littlewood

    Ω*N(n) = média de 𝔖(C) sobre janelas contendo n.

    Por que C é sempre par (necessário para 𝔖 ser não-trivial):
      S(i) = 3*(ímpar) = ímpar
      n ∈ grade = ímpar
      C = ímpar - ímpar = PAR  ✓

    Por que isso não é oracle:
      S(i) depende só de N e i (posição).
      n é conhecido (posição na grade).
      𝔖(C) depende só da fatoração de C — sem checar primalidade de vizinhos.
    """
    omega_star = np.zeros((3, N), dtype=float)

    for c in range(N):
        i_min = max(0, c - 2)
        i_max = min(N - 3, c)
        for r in range(3):
            n = int(grid[r, c])
            weights = []
            for i in range(i_min, i_max + 1):
                S = anchor_sum(N, i)
                C = S - n
                # C deve ser par e positivo
                if C > 0 and C % 2 == 0:
                    weights.append(singular_series(C, spf, spf_limit))
                else:
                    weights.append(1.0)  # neutro
            omega_star[r, c] = np.mean(weights) if weights else 0.0
    return omega_star


# ══════════════════════════════════════════════════════════════
# 5. ANÁLISE ESTATÍSTICA
# ══════════════════════════════════════════════════════════════

def collect_by_class(grid, omega, labels):
    result = defaultdict(list)
    for r in range(3):
        for c in range(grid.shape[1]):
            n = int(grid[r, c])
            cls = labels.get(n)
            if cls in ('P1', 'P2', 'composite'):
                result[cls].append(omega[r, c])
    return {k: np.array(v) for k, v in result.items()}


def run_tests(by_class, label=""):
    """Roda KS + Mann-Whitney para P1 vs P2. Retorna dict com resultados."""
    p1 = by_class.get('P1', np.array([]))
    p2 = by_class.get('P2', np.array([]))
    out = {'label': label, 'n_p1': len(p1), 'n_p2': len(p2)}

    if len(p1) > 1 and len(p2) > 1:
        ks, ks_p = stats.ks_2samp(p1, p2)
        _, mw_p = stats.mannwhitneyu(p1, p2, alternative='two-sided')
        out.update({
            'ks': ks, 'ks_p': ks_p, 'mw_p': mw_p,
            'mean_p1': p1.mean(), 'mean_p2': p2.mean(),
            'median_p1': np.median(p1), 'median_p2': np.median(p2),
            'significant_ks': ks_p < 0.05,
            'significant_mw': mw_p < 0.05,
        })
    else:
        out.update({'ks': None, 'ks_p': None, 'mw_p': None,
                    'significant_ks': False, 'significant_mw': False})
    return out


def print_report(N, n_successes, trios, t_elapsed,
                 by_omega, by_omega_star, res_orig, res_star):
    SEP = '═' * 70
    print(f"\n{SEP}")
    print(f"  CRIVO GEOMÉTRICO v2 — G_{{3,{N}}}  (n ≤ {6*N-1})")
    print(SEP)
    print(f"  Tempo total: {t_elapsed:.1f}s")
    print(f"  Janelas: {N-2}  |  Com trio primo: {n_successes}"
          f"  |  Taxa: {n_successes/(N-2):.4f}")
    ku_teo = 8 * N / (np.log(N) ** 3)
    print(f"  Ku teórico ≈ {ku_teo:.1f}  (8N/(ln N)³)")

    if trios:
        print(f"\n  Primeiros 3 trios primos:")
        for win_i, name, vals in trios[:3]:
            S = anchor_sum(N, win_i)
            print(f"    i={win_i:4d}  {name}: {vals}  |  S(i)={S}  âncora={S//3}")

    # Tabela comparativa
    print(f"\n{'─'*70}")
    print(f"  {'':12} {'ΩN (oracle)':>20}  {'Ω*N (oracle-free)':>20}")
    print(f"  {'Classe':<12} {'Média':>8} {'Mediana':>8} {'Std':>6}  "
          f"{'Média':>8} {'Mediana':>8} {'Std':>6}")
    print(f"{'─'*70}")
    for cls in ('P1', 'P2', 'composite'):
        v  = by_omega.get(cls, np.array([]))
        vs = by_omega_star.get(cls, np.array([]))
        def fmt(arr):
            if len(arr):
                return f"{arr.mean():8.4f} {np.median(arr):8.4f} {arr.std():6.4f}"
            return f"{'—':>8} {'—':>8} {'—':>6}"
        print(f"  {cls:<12} {fmt(v)}  {fmt(vs)}")

    # Testes
    print(f"\n{'─'*70}")
    print(f"  TESTES DE HIPÓTESE — P1 vs P2")
    print(f"{'─'*70}")
    for res in [res_orig, res_star]:
        tag = f"[{res['label']}]"
        if res['ks_p'] is not None:
            sig_ks = "✓" if res['significant_ks'] else "✗"
            sig_mw = "✓" if res['significant_mw'] else "✗"
            print(f"  {tag:<22} KS={res['ks']:.4f}  p={res['ks_p']:.2e} {sig_ks}"
                  f"  |  MW p={res['mw_p']:.2e} {sig_mw}")
            if res['significant_ks'] or res['significant_mw']:
                d = res['mean_p1'] - res['mean_p2']
                print(f"    → Distribuições distinguíveis  |  Δmédias={d:+.5f}")
            else:
                print(f"    → Sem separação detectada para este N")
        else:
            print(f"  {tag}: dados insuficientes")

    # Diagnóstico comparativo
    print(f"\n{'─'*70}")
    print("  DIAGNÓSTICO COMPARATIVO")
    print(f"{'─'*70}")
    orig_ok = res_orig.get('significant_ks') or res_orig.get('significant_mw')
    star_ok = res_star.get('significant_ks') or res_star.get('significant_mw')

    if orig_ok and star_ok:
        print("  ✓✓ AMBOS os pesos discriminam P1 de P2.")
        print("     → Ω*N preserva o poder discriminante sem oracle.")
        print("     → Evidência favorável à computabilidade do crivo geométrico.")
    elif orig_ok and not star_ok:
        print("  ✓✗ Apenas ΩN (oracle) discrimina.")
        print("     → 𝔖(C) não capta o sinal neste N.")
        print("     → Possível obstrução modular — tente N com fator primo ≥ 7.")
    elif not orig_ok and star_ok:
        print("  ✗✓ Apenas Ω*N (oracle-free) discrimina.")
        print("     → Resultado inesperado — investigar.")
    else:
        print("  ✗✗ Nenhum peso discrimina para este N.")
        print("     → Provávelmente obstrução modular (N com só fatores 2,3,5).")
        print("     → Tente N=21000, N=30030 ou N=100000.")
    print(SEP)


# ══════════════════════════════════════════════════════════════
# 6. VISUALIZAÇÃO
# ══════════════════════════════════════════════════════════════

COLORS = {
    'P1':        '#27ae60',
    'P2':        '#e74c3c',
    'composite': '#7f8c8d',
}


def plot_results(N, by_omega, by_omega_star, omega, omega_star,
                 grid, labels, trios, res_orig, res_star):
    fig = plt.figure(figsize=(18, 13))
    fig.suptitle(
        f'Crivo Geométrico v2  —  $G_{{3,{N}}}$\n'
        f'Comparação: $\\Omega_N$ (oracle) vs $\\Omega^*_N$ (oracle-free via $\\mathfrak{{S}}(C)$)',
        fontsize=13, fontweight='bold', y=0.99
    )
    gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.50, wspace=0.35)

    def _title_with_pval(base, res):
        if res['ks_p'] is not None:
            sig = "✓ sig." if res['significant_ks'] else "✗ n.s."
            return f"{base}\nKS p={res['ks_p']:.1e}  {sig}"
        return base

    # ── Row 0: histogramas ────────────────────────────────────
    for col, (by_cls, res, name) in enumerate([
        (by_omega,      res_orig, '$\\Omega_N$ (oracle)'),
        (by_omega_star, res_star, '$\\Omega^*_N$ (oracle-free)'),
    ]):
        ax = fig.add_subplot(gs[0, col*1:(col+1)*1 + (1 if col==1 else 0)])
        for cls in ('P1', 'P2', 'composite'):
            v = by_cls.get(cls, [])
            if len(v):
                ax.hist(v, bins=40, alpha=0.55, color=COLORS[cls],
                        label=f'{cls} (n={len(v)})', density=True)
        ax.set_xlabel('peso geométrico', fontsize=10)
        ax.set_ylabel('Densidade', fontsize=10)
        ax.set_title(_title_with_pval(name, res), fontsize=10)
        ax.legend(fontsize=8)
        ax.grid(alpha=0.25)

    # ── Row 0 col 2: KDE comparando ambos para P1 ────────────
    ax_kde = fig.add_subplot(gs[0, 2])
    for by_cls, lbl, ls in [(by_omega, '$\\Omega_N$ P1', '-'),
                             (by_omega_star, '$\\Omega^*_N$ P1', '--')]:
        v = np.array(by_cls.get('P1', []))
        if len(v) > 20:
            kde = stats.gaussian_kde(v, bw_method='scott')
            x = np.linspace(0, max(v)*1.05, 400)
            ax_kde.plot(x, kde(x), lw=2, ls=ls, label=lbl, color='#27ae60',
                        alpha=0.5 if ls=='--' else 1.0)
    for by_cls, lbl, ls in [(by_omega, '$\\Omega_N$ P2', '-'),
                             (by_omega_star, '$\\Omega^*_N$ P2', '--')]:
        v = np.array(by_cls.get('P2', []))
        if len(v) > 20:
            kde = stats.gaussian_kde(v, bw_method='scott')
            x = np.linspace(0, max(v)*1.05, 400)
            ax_kde.plot(x, kde(x), lw=2, ls=ls, label=lbl, color='#e74c3c',
                        alpha=0.5 if ls=='--' else 1.0)
    ax_kde.set_title('KDE: P1 vs P2\nsólido=oracle, tracejado=oracle-free', fontsize=9)
    ax_kde.legend(fontsize=7)
    ax_kde.grid(alpha=0.25)

    # ── Row 1: boxplots ───────────────────────────────────────
    for col, (by_cls, name) in enumerate([
        (by_omega,      '$\\Omega_N$'),
        (by_omega_star, '$\\Omega^*_N$'),
    ]):
        ax = fig.add_subplot(gs[1, col])
        data_box = [by_cls.get(c, [np.nan]) for c in ('P1','P2','composite')]
        bp = ax.boxplot(data_box, labels=['P1','P2','comp.'],
                        patch_artist=True, notch=True,
                        medianprops=dict(color='black', lw=2))
        for patch, cls in zip(bp['boxes'], ('P1','P2','composite')):
            patch.set_facecolor(COLORS[cls])
            patch.set_alpha(0.65)
        ax.set_ylabel('peso', fontsize=10)
        ax.set_title(f'Boxplot — {name}', fontsize=10)
        ax.grid(alpha=0.25)

    # ── Row 1 col 2: scatter 𝔖(C) vs n para Row 2 (âncora) ──
    ax_anc = fig.add_subplot(gs[1, 2])
    N_grid = grid.shape[1]
    for cls in ('composite', 'P2', 'P1'):
        ns, ws = [], []
        for c in range(N_grid):
            n = int(grid[1, c])  # Row 2 = âncora
            if labels.get(n) == cls:
                ns.append(n)
                ws.append(omega_star[1, c])
        if ns:
            ax_anc.scatter(ns, ws, c=COLORS[cls], alpha=0.3, s=4,
                           label=cls, rasterized=True)
    ax_anc.set_xlabel('n (Row 2 = âncora)', fontsize=9)
    ax_anc.set_ylabel('$\\Omega^*_N(n)$', fontsize=9)
    ax_anc.set_title('Ω*N na Row 2\n(elemento âncora = S(i)/3)', fontsize=9)
    ax_anc.legend(markerscale=4, fontsize=8)
    ax_anc.grid(alpha=0.2)

    # ── Row 2: correlação ΩN vs Ω*N por classe ───────────────
    ax_corr = fig.add_subplot(gs[2, :2])
    for cls in ('P1', 'P2'):
        xs, ys = [], []
        for r in range(3):
            for c in range(N_grid):
                n = int(grid[r, c])
                if labels.get(n) == cls:
                    xs.append(omega[r, c])
                    ys.append(omega_star[r, c])
        if xs:
            ax_corr.scatter(xs, ys, c=COLORS[cls], alpha=0.15, s=3,
                            label=cls, rasterized=True)
            corr = np.corrcoef(xs, ys)[0,1]
            print(f"  Correlação ΩN × Ω*N para {cls}: r={corr:.4f}")
    ax_corr.set_xlabel('$\\Omega_N$ (oracle)', fontsize=10)
    ax_corr.set_ylabel('$\\Omega^*_N$ (oracle-free)', fontsize=10)
    ax_corr.set_title('Correlação entre pesos\n(ideal: separação por classe)', fontsize=10)
    ax_corr.legend(markerscale=4, fontsize=9)
    ax_corr.grid(alpha=0.2)

    # ── Row 2 col 2: trios e Goldbach witnesses ───────────────
    ax_wit = fig.add_subplot(gs[2, 2])
    if trios:
        somas = []
        for win_i, name, vals in trios:
            for a, b in [(vals[0],vals[1]), (vals[0],vals[2]), (vals[1],vals[2])]:
                somas.append(a + b)
        somas = np.array(somas)
        ax_wit.hist(somas, bins=min(50, len(set(somas))),
                    color='#2980b9', alpha=0.7, edgecolor='white')
        ax_wit.set_xlabel('Soma p_i + p_j', fontsize=9)
        ax_wit.set_ylabel('Freq.', fontsize=9)
        ax_wit.set_title(f'Representações Goldbach\nde {len(trios)} trios primos', fontsize=9)
        ax_wit.grid(alpha=0.2)

    fname = f'omega_v2_N{N}.png'
    plt.savefig(fname, dpi=150, bbox_inches='tight')
    plt.show()
    print(f"\n  Gráfico salvo em: {fname}")


def plot_density_decay(N_values=(200, 500, 1000, 2000, 5000)):
    print("\n  Computando decaimento de Ku para múltiplos N...")
    ku_emp, ku_teo = [], []
    for N in N_values:
        limit = 6 * N
        is_prime = sieve_eratosthenes(limit)
        grid = build_grid(N)
        n_succ, _ = detect_prime_triples(grid, is_prime)
        ku_emp.append(n_succ)
        ku_teo.append(8 * N / (np.log(N) ** 3))
        print(f"    N={N:6d}: Ku_emp={n_succ:5d}  Ku_teo={ku_teo[-1]:.1f}")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(N_values, ku_teo, 'k--', lw=2, label='$K_u$ teórico: $8N/(\\ln N)^3$')
    ax.plot(N_values, ku_emp, 'o-', color='#2980b9', lw=2, ms=7, label='$K_u$ empírico')
    ax.set_xlabel('N'); ax.set_ylabel('$K_u$')
    ax.set_title('Crescimento de $K_u$ — empírico vs teórico')
    ax.legend(); ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('ku_decay_v2.png', dpi=150)
    plt.show()
    print("  Salvo: ku_decay_v2.png")


# ══════════════════════════════════════════════════════════════
# 7. MAIN
# ══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='Crivo Geométrico v2 — ΩN oracle vs Ω*N oracle-free (Bandeira 2026)'
    )
    parser.add_argument('--N', type=int, default=1000)
    parser.add_argument('--show_grid', action='store_true')
    parser.add_argument('--decay', action='store_true')
    args = parser.parse_args()

    N = args.N
    t0 = time.time()

    # Limite do crivo: 6N para a grade, ~12N para os complementos C(n,i)
    limit_grid = 6 * N
    limit_spf  = 13 * N   # margem para C = S(i) - n_min ≈ 10N

    print(f"\n  Construindo G_{{3,{N}}} — valores até {limit_grid - 1}")
    print(f"  Crivo de Eratóstenes até {limit_grid}...")
    is_prime = sieve_eratosthenes(limit_grid)

    print(f"  SPF sieve até {limit_spf} (para 𝔖(C))...")
    spf = spf_sieve(limit_spf)

    grid = build_grid(N)

    if args.show_grid and N <= 20:
        print(f"\n  Grade G_{{3,{N}}}:")
        for r in range(3):
            row = [f"{grid[r,c]:4d}" for c in range(N)]
            print(f"  Linha {r+1}: {' '.join(row)}")

    all_vals = set(int(v) for v in grid.flatten())
    labels = classify_all(all_vals, is_prime, spf)

    print("  Detectando trios primos...")
    n_successes, trios = detect_prime_triples(grid, is_prime)

    print("  Computando ΩN(n) [oracle]...")
    omega = compute_omega(grid, is_prime)

    print("  Computando Ω*N(n) [oracle-free via 𝔖(C)]...")
    omega_star = compute_omega_star(grid, spf, limit_spf, N)

    by_omega      = collect_by_class(grid, omega,      labels)
    by_omega_star = collect_by_class(grid, omega_star, labels)

    res_orig = run_tests(by_omega,      label="ΩN  oracle      ")
    res_star = run_tests(by_omega_star, label="Ω*N oracle-free ")

    t_elapsed = time.time() - t0
    print_report(N, n_successes, trios, t_elapsed,
                 by_omega, by_omega_star, res_orig, res_star)

    plot_results(N, by_omega, by_omega_star, omega, omega_star,
                 grid, labels, trios, res_orig, res_star)

    if args.decay:
        plot_density_decay()


if __name__ == '__main__':
    main()
