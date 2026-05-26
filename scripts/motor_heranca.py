"""
Motor de Herança Estrutural — Código Unificado de Simulação
Tiago Bandeira, 2026

Organização:
  Módulo 1 — Geração das Matrizes (Fita 2xN e Grade 3xC)
  Módulo 2 — Gabarito Geométrico (Janela 3x3 canônica)
  Módulo 3 — Scanner de Janelas (Detecção HR- e HR+)
  Módulo 4 — Simulação Caos → Ordem (Transição de Fase)
  Módulo 5 — Bancada de Testes
"""

import math
import random
import numpy as np

# ─────────────────────────────────────────────────────────────
# UTILITÁRIOS
# ─────────────────────────────────────────────────────────────

def is_prime(n):
    """Verificação de primalidade."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# ─────────────────────────────────────────────────────────────
# MÓDULO 1 — GERAÇÃO DAS MATRIZES
# ─────────────────────────────────────────────────────────────

def gerar_matrizes(par):
    """
    Dado um número par, gera:
      - Matriz 2xN (Fita-Dobra): linha 1 cresce →, linha 2 é complemento ←
      - Matriz 3xC (Grade em ZigZag com centro espelhado)

    A condição de acoplamento 3C = 2N é mantida pelo ajuste de
    repetições centrais conforme o módulo de (total de elementos) por 3.

    Retorna: (matriz_2xN, matriz_3xC, repeticoes_adicionadas, N, C)
    """
    metade = par // 2
    # Maior ímpar ≤ metade (exclui o 1 implicitamente na construção)
    m = metade if metade % 2 != 0 else metade - 1

    # Linha 1: ímpares crescentes de 1 até m
    L1 = list(range(1, m + 1, 2))
    # Linha 2: complementos (cada coluna soma 'par')
    L2 = [par - x for x in L1]

    N = len(L1)  # número de colunas da fita

    # Lista ordenada de todos os elementos para montar a grade 3xC
    elementos = sorted(L1 + L2)
    total = len(elementos)

    # Ajuste central para satisfazer 3C = 2N
    resto = total % 3
    faltantes = (3 - resto) % 3
    idx_centro = total // 2

    if faltantes == 2:
        # Duplica os dois elementos do encontro central
        e1 = elementos[idx_centro - 1]
        e2 = elementos[idx_centro]
        elementos.insert(idx_centro, e2)
        elementos.insert(idx_centro, e1)
    elif faltantes == 1:
        # Duplica o elemento central único
        e_centro = elementos[idx_centro]
        elementos.insert(idx_centro, e_centro)

    C = len(elementos) // 3  # número de colunas da grade

    # Distribuição ZigZag na grade 3xC:
    # Linha A → crescente, Linha B ← decrescente (vai-e-vem), Linha C → crescente
    LA = elementos[0:C]
    LB = elementos[C:2*C][::-1]
    LC = elementos[2*C:3*C]

    matriz_2xN = [L1, L2]
    matriz_3xC = [LA, LB, LC]

    return matriz_2xN, matriz_3xC, faltantes, N, C


def exibir_matrizes(par):
    """Imprime as duas matrizes para um par dado."""
    mat2, mat3, reps, N, C = gerar_matrizes(par)
    print(f"\n{'='*54}")
    print(f"  PAR: {par}   (repetições centrais adicionadas: {reps})")
    print(f"{'='*54}")
    print(f"Matriz 2x{N} (Fita-Dobra):")
    print(f"  L1 →  {mat2[0]}")
    print(f"  L2 ←  {mat2[1]}")
    print(f"\nMatriz 3x{C} (Grade ZigZag):")
    print(f"  LA →  {mat3[0]}")
    print(f"  LB ←  {mat3[1]}")
    print(f"  LC →  {mat3[2]}")


# ─────────────────────────────────────────────────────────────
# MÓDULO 2 — GABARITO GEOMÉTRICO (JANELA 3x3 CANÔNICA)
# ─────────────────────────────────────────────────────────────

def criar_gabarito_3x3(par_alvo, pares_fita, pivo_central=None):
    """
    Monta a janela 3x3 como gabarito estrutural rígido.
    Distribui 4 pares da fita nos 4 eixos de simetria da matriz:
      - Diagonal Principal (D1): [0,0] ↔ [2,2]
      - Diagonal Secundária (D2): [0,2] ↔ [2,0]
      - Coluna Central (Cv):     [0,1] ↔ [2,1]
      - Linha Central (Lc):      [1,0] ↔ [1,2]
    O menor elemento de cada par fica na entrada, o maior no oposto.
    """
    if len(pares_fita) < 4:
        raise ValueError("São necessários pelo menos 4 pares da fita.")

    janela = np.zeros((3, 3), dtype=int)
    janela[1, 1] = pivo_central if pivo_central is not None else par_alvo // 2

    pares = [sorted(p) for p in pares_fita[:4]]

    # D1 — Diagonal Principal
    janela[0, 0] = pares[0][0]
    janela[2, 2] = pares[0][1]

    # D2 — Diagonal Secundária
    janela[0, 2] = pares[1][0]
    janela[2, 0] = pares[1][1]

    # Cv — Coluna Central
    janela[0, 1] = pares[2][0]
    janela[2, 1] = pares[2][1]

    # Lc — Linha Central
    janela[1, 0] = pares[3][0]
    janela[1, 2] = pares[3][1]

    return janela


def validar_gabarito(janela, par_alvo):
    """
    Verifica que a soma de cada par de extremos opostos resulta em par_alvo.
    Retorna True se o gabarito for geometricamente válido.
    """
    eixos = {
        "Diagonal Principal": (janela[0, 0], janela[2, 2]),
        "Diagonal Secundária": (janela[0, 2], janela[2, 0]),
        "Coluna Central":      (janela[0, 1], janela[2, 1]),
        "Linha Central":       (janela[1, 0], janela[1, 2]),
    }
    print(f"\n--- Validação do Gabarito 3x3 (alvo: {par_alvo}) ---")
    valido = True
    for nome, (a, b) in eixos.items():
        soma = a + b
        ok = soma == par_alvo
        status = "✓" if ok else "✗"
        print(f"  {status} {nome}: {a} + {b} = {soma}")
        if not ok:
            valido = False
    return valido


def exibir_gabarito(par_alvo, pares_fita, pivo_central=None):
    """Cria, exibe e valida o gabarito para um par alvo."""
    janela = criar_gabarito_3x3(par_alvo, pares_fita, pivo_central)
    print(f"\n=== GABARITO 3x3 — PAR ALVO: {par_alvo} ===")
    print(janela)
    valido = validar_gabarito(janela, par_alvo)
    if valido:
        print("  → Gabarito geometricamente consistente.\n")
    else:
        print("  → ATENÇÃO: gabarito com inconsistência.\n")
    return janela


# ─────────────────────────────────────────────────────────────
# MÓDULO 3 — SCANNER DE JANELAS (DETECÇÃO HR- E HR+)
# ─────────────────────────────────────────────────────────────

def escanear_janelas(elementos):
    """
    Percorre a lista de elementos com dois pivôs marchando das extremidades
    para o centro (ziguezague ótimo), simulando as janelas 3x3.

    HR- (Fraca): ambos os extremos são primos.
    HR+ (Forte): extremos e centro (pivô) são todos primos.

    Retorna: (hr_menos, hr_mais)
    """
    esq = 0
    dir_ = len(elementos) - 1
    hr_menos = False
    hr_mais = False

    while esq < dir_:
        E1 = elementos[esq]
        E2 = elementos[dir_]
        meio = (esq + dir_) // 2
        centro = elementos[meio]

        if is_prime(E1) and is_prime(E2):
            hr_menos = True
            if is_prime(centro):
                hr_mais = True

        esq += 1
        dir_ -= 1

    return hr_menos, hr_mais


# ─────────────────────────────────────────────────────────────
# MÓDULO 4 — SIMULAÇÃO CAOS → ORDEM (TRANSIÇÃO DE FASE)
# ─────────────────────────────────────────────────────────────

def simular_transicao(N, verbose=True):
    """
    Experimento de transição de fase: Caos Puro → Ordenação Canônica.

    Exige N múltiplo de 3 para manter o acoplamento 3C = 2N.

    Povoa a fita com ímpares (excluindo 1), embaralha (entropia máxima),
    e ordena gradualmente via Bubble Sort, monitorando o Tempo de
    Primeira Passagem (primeiro swap que ativa HR- ou HR+).

    Retorna: dicionário com métricas do experimento.
    """
    assert N % 3 == 0, "N deve ser múltiplo de 3 para manter o acoplamento 3C = 2N."
    C = (2 * N) // 3
    total = 2 * N

    # Ímpares a partir de 3 (exclui o 1)
    fita = [2 * i + 3 for i in range(total)]

    # Estado inicial: Caos Puro
    random.shuffle(fita)
    arr = fita.copy()

    if verbose:
        print(f"\n{'='*54}")
        print(f"  EXPERIMENTO: TRANSIÇÃO CAOS → ORDEM")
        print(f"  Fita 2×{N}  |  Grade 3×{C}  |  {total} partículas")
        print(f"{'='*54}")

    total_swaps = 0
    passo_hr_menos = None
    passo_hr_mais = None

    # Verificação no estado inicial (caos puro pode ativar por acaso)
    hr_inf, hr_sup = escanear_janelas(arr)
    if hr_inf:
        passo_hr_menos = 0
    if hr_sup:
        passo_hr_mais = 0

    # Ordenação total — Bubble Sort para granularidade máxima de observação
    for i in range(total):
        for j in range(0, total - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                total_swaps += 1

                hr_inf, hr_sup = escanear_janelas(arr)

                if hr_inf and passo_hr_menos is None:
                    passo_hr_menos = total_swaps
                if hr_sup and passo_hr_mais is None:
                    passo_hr_mais = total_swaps

    # Relatório
    if verbose:
        print(f"\n  Total de swaps até ordenação canônica: {total_swaps}")

        if passo_hr_menos is not None:
            pct = (passo_hr_menos / total_swaps) * 100
            print(f"  HR- ativado no swap {passo_hr_menos}  ({pct:.2f}% do percurso)")
        else:
            print(f"  HR- NÃO ativado (inesperado para N grande).")

        if passo_hr_mais is not None:
            pct = (passo_hr_mais / total_swaps) * 100
            print(f"  HR+ ativado no swap {passo_hr_mais}  ({pct:.2f}% do percurso)")
        else:
            print(f"  HR+ não ativado antes da ordenação total.")

    return {
        "N": N, "C": C, "total_swaps": total_swaps,
        "passo_hr_menos": passo_hr_menos,
        "passo_hr_mais": passo_hr_mais,
    }


# ─────────────────────────────────────────────────────────────
# MÓDULO 5 — BANCADA DE TESTES
# ─────────────────────────────────────────────────────────────

def bancada_matrizes():
    print("\n" + "─"*54)
    print("  BANCADA 1 — Geração de Matrizes")
    print("─"*54)
    for par in [30, 32, 48]:
        exibir_matrizes(par)


def bancada_gabaritos():
    print("\n" + "─"*54)
    print("  BANCADA 2 — Gabaritos 3x3")
    print("─"*54)

    # Exemplo do Artigo 5: C=8, N=12, par alvo 2M+ = 48
    par_alvo = 48
    pares = [(7, 41), (11, 37), (13, 35), (17, 31)]
    pivo = 25
    exibir_gabarito(par_alvo, pares, pivo)

    # Exemplo adicional: par alvo 58 (do caso C=10, N=15)
    par_alvo_2 = 58
    pares_2 = [(11, 47), (13, 45), (17, 41), (19, 39)]
    exibir_gabarito(par_alvo_2, pares_2)


def bancada_scanner():
    print("\n" + "─"*54)
    print("  BANCADA 3 — Scanner de Janelas HR-/HR+")
    print("─"*54)
    casos = [
        ("Ordenado (canônico)", sorted([2*i+3 for i in range(30)])),
        ("Aleatório pequeno",   random.sample(range(3, 62, 2), 30)),
    ]
    for nome, elementos in casos:
        hr_m, hr_M = escanear_janelas(elementos)
        print(f"\n  [{nome}]")
        print(f"    HR-: {'✓ SIM' if hr_m else '✗ NÃO'}   HR+: {'✓ SIM' if hr_M else '✗ NÃO'}")


def bancada_transicao():
    print("\n" + "─"*54)
    print("  BANCADA 4 — Transição de Fase (Caos → Ordem)")
    print("─"*54)
    for N in [3*5, 3*7, 3*11]:
        simular_transicao(N, verbose=True)


# ─────────────────────────────────────────────────────────────
# EXECUÇÃO PRINCIPAL
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    bancada_matrizes()
    bancada_gabaritos()
    bancada_scanner()
    bancada_transicao()
