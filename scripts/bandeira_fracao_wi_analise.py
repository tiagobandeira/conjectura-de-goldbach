"""
Análise da Fração de Janelas Wi Ativas — Motor de Herança Estrutural
Tiago Bandeira, Maio 2026

Mede, para cada par base 2M, a fração de janelas Wi que ativam HR-
na configuração canônica da grade G(3xC), e compara com o modelo
de Poisson independente (1/log²(M+)).

Distinção fundamental:
  Par base  2M  = soma das colunas da fita (ak + bk = 2M)
  Par alvo  2M+ = soma das diagonais da fita (a_{k+1} + bk = 2M+)

O scanner opera sobre o par alvo. HR- ativa quando algum eixo
de alguma Wi tem ambos os extremos primos.

Experimentos:
  1. teste_falha_hr()     — verifica se HR- falha para algum par alvo
  2. analisar_par()       — métricas de Wi ativas/totais para um par
  3. taxa_decaimento()    — razão frac_Wi / (1/log²) por blocos de M+
"""

import math


# ─────────────────────────────────────────────────────────────
# UTILITÁRIOS
# ─────────────────────────────────────────────────────────────

def is_prime(n):
    """Verificação de primalidade por divisão por tentativa."""
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True


def sequencia_canonica(par_base):
    """
    Retorna a sequência canônica de ímpares da fita-dobra para par_base,
    sem o elemento 1 (que não forma diagonal válida no scanner).

    Par base  2M  : colunas da fita somam 2M
    Par alvo  2M+ : diagonais da fita somam 2M+ = 2M + 2
    """
    M = par_base // 2
    m = M if M % 2 != 0 else M - 1
    N = (m + 1) // 2
    L1 = [2*k - 1 for k in range(1, N+1)]          # ak = 2k-1
    L2 = [par_base - a for a in L1]                 # bk = 2M - ak
    return sorted(set(x for x in L1 + L2 if x > 1)), N


# ─────────────────────────────────────────────────────────────
# MÓDULO 1 — Verificação de falha de HR-
# ─────────────────────────────────────────────────────────────

def teste_falha_hr(limite=10002):
    """
    Testa se HR- falha (nenhuma Wi ativa) para algum par alvo
    até o limite especificado.

    HR- falha ⟺ nenhum par (E1, E2) com E1+E2=2M+ tem ambos primos
               ⟺ 2M+ não é soma de dois primos (contradiz Goldbach)
    """
    falhas = []
    for pb in range(20, limite, 2):
        seq, _ = sequencia_canonica(pb)
        par_alvo = pb + 2
        ativou = False
        esq, dir_ = 0, len(seq) - 1
        while esq < dir_:
            if is_prime(seq[esq]) and is_prime(seq[dir_]):
                ativou = True
                break
            esq += 1
            dir_ -= 1
        if not ativou:
            falhas.append(par_alvo)

    print(f"Pares alvo testados: 22 até {limite}")
    print(f"Falhas de HR- (nenhuma Wi ativa): {len(falhas)}")
    if falhas:
        print(f"Primeiros casos: {falhas[:20]}")
    else:
        print("NENHUMA FALHA — HR- ativa em 100% dos casos testados.")
    return falhas


# ─────────────────────────────────────────────────────────────
# MÓDULO 2 — Métricas de Wi para um par base
# ─────────────────────────────────────────────────────────────

def analisar_par(par_base):
    """
    Para um par base 2M, calcula:
      - total_wi       : número de janelas Wi geradas pelo scanner
      - wi_ativas      : Wi com pelo menos um eixo primo-primo (HR-)
      - frac_wi        : wi_ativas / total_wi
      - total_eixos    : total de eixos (E1, E2) capturados
      - eixos_par_primo: eixos com E1 e E2 ambos primos
      - eixos_um_primo : eixos com exatamente um primo
      - eixos_nenhum   : eixos sem nenhum primo
      - frac_eixos     : eixos_par_primo / total_eixos
    """
    seq, N = sequencia_canonica(par_base)
    par_alvo = par_base + 2

    total_wi = wi_ativas = total_eixos = 0
    eixos_par_primo = eixos_um_primo = eixos_nenhum = 0

    esq, dir_ = 0, len(seq) - 1
    buf = []

    while esq < dir_:
        buf.append((seq[esq], seq[dir_]))
        if len(buf) == 4:
            total_wi += 1
            if any(is_prime(a) and is_prime(b) for a, b in buf):
                wi_ativas += 1
            for a, b in buf:
                total_eixos += 1
                p1, p2 = is_prime(a), is_prime(b)
                if p1 and p2:   eixos_par_primo += 1
                elif p1 or p2:  eixos_um_primo  += 1
                else:           eixos_nenhum    += 1
            buf = []
        esq += 1
        dir_ -= 1

    # Janela parcial restante
    if buf:
        total_wi += 1
        if any(is_prime(a) and is_prime(b) for a, b in buf):
            wi_ativas += 1
        for a, b in buf:
            total_eixos += 1
            p1, p2 = is_prime(a), is_prime(b)
            if p1 and p2:   eixos_par_primo += 1
            elif p1 or p2:  eixos_um_primo  += 1
            else:           eixos_nenhum    += 1

    frac_wi    = wi_ativas      / total_wi    if total_wi    else 0
    frac_eixos = eixos_par_primo / total_eixos if total_eixos else 0
    log2_inv   = 1 / (math.log(par_alvo) ** 2)

    return {
        "par_alvo":        par_alvo,
        "N":               N,
        "total_wi":        total_wi,
        "wi_ativas":       wi_ativas,
        "frac_wi":         frac_wi,
        "total_eixos":     total_eixos,
        "eixos_par_primo": eixos_par_primo,
        "eixos_um_primo":  eixos_um_primo,
        "eixos_nenhum":    eixos_nenhum,
        "frac_eixos":      frac_eixos,
        "log2_inv":        log2_inv,
    }


# ─────────────────────────────────────────────────────────────
# MÓDULO 3 — Taxa de decaimento e razão Wi/Poisson
# ─────────────────────────────────────────────────────────────

def taxa_decaimento(limite=10002, tamanho_bloco=1000):
    """
    Computa, por blocos de par alvo, a fração média de Wi ativas
    e a razão com o modelo de Poisson independente 1/log²(M+).

    Razão Wi/Poisson > 1 indica que a estrutura geométrica de Wi
    detecta pares primo-primo mais eficientemente do que sensores
    independentes na reta numérica.
    """
    resultados = []
    for pb in range(20, limite, 2):
        r = analisar_par(pb)
        resultados.append(r)

    print(f"\n{'Bloco (M+)':>14}  {'Frac Wi':>10}  {'Frac Eixos':>12}"
          f"  {'1/log²(M+)':>12}  {'Razão Wi/Poisson':>18}")
    print("-" * 75)

    for lo in range(0, limite, tamanho_bloco):
        hi = lo + tamanho_bloco
        subset = [r for r in resultados if lo <= r["par_alvo"] < hi]
        if not subset:
            continue
        fw      = sum(r["frac_wi"]    for r in subset) / len(subset)
        fe      = sum(r["frac_eixos"] for r in subset) / len(subset)
        poisson = sum(r["log2_inv"]   for r in subset) / len(subset)
        razao   = fw / poisson if poisson > 0 else 0
        print(f"  {lo:>5}-{hi:<5}    {fw:>10.4f}  {fe:>12.4f}"
              f"  {poisson:>12.6f}  {razao:>18.2f}x")

    print()
    print("Interpretação:")
    print("  Razão Wi/Poisson ≈ 19 (estável para M+ ≳ 3000)")
    print("  A estrutura geométrica de Wi supera o modelo de Poisson")
    print("  independente por fator constante ≈ 19.")
    print("  Isso reflete que Wi emparelha primos de R1 (pequenos, densos)")
    print("  com complementos em R3, em vez de buscar na vizinhança de M+.")

    return resultados


# ─────────────────────────────────────────────────────────────
# EXECUÇÃO PRINCIPAL
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  EXPERIMENTO 1 — Verificação de falha de HR-")
    print("=" * 60)
    teste_falha_hr(limite=10002)

    print()
    print("=" * 60)
    print("  EXPERIMENTO 2 — Taxa de decaimento e razão Wi/Poisson")
    print("=" * 60)
    taxa_decaimento(limite=10002, tamanho_bloco=1000)
