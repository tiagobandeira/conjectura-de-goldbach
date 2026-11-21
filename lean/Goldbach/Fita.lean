/-
  Goldbach/Fita.lean
  ------------------
  A fita-dobra `F_N^ε` do Paper 07 (Motor de Herança Estrutural), §2.

      a_k = 2k - 1 ,      b_k = 4N - (2k - 1) - 2ε ,      k = 1..N.
-/
import Goldbach.Basico

namespace Goldbach

/-- Linha 1 da fita: os ímpares em ordem crescente. -/
def fitaA (k : Nat) : Nat :=
  2 * k - 1

/-- Linha 2 da fita: os ímpares em ordem decrescente (percurso zigzag).
    `ε = 0` é o modo normal; `ε = 1` é o modo de repetição. -/
def fitaB (N k eps : Nat) : Nat :=
  4 * N - (2 * k - 1) - 2 * eps

/-- Propriedade 2.1 (soma constante das colunas): toda coluna soma `4N - 2ε`,
    independentemente da posição `k` e de qualquer informação de primalidade. -/
theorem fita_soma (N k eps : Nat) (hk : 1 ≤ k) (hkN : k ≤ N) (he : eps ≤ 1) :
    fitaA k + fitaB N k eps = 4 * N - 2 * eps := by
  simp only [fitaA, fitaB]
  omega

/-- Propriedade 2.3 (diagonais da fita — par alvo): no modo `ε = 1` (par base
    `4N - 2`), cada par diagonal soma o par alvo `4N`. -/
theorem fita_diagonal (N k : Nat) (hk : 1 ≤ k) (hkN : k + 1 ≤ N) :
    fitaA (k + 1) + fitaB N k 1 = 4 * N := by
  simp only [fitaA, fitaB]
  omega

/-- Propriedade 2.2 (dois pares por fita): a mesma fita representa
    simultaneamente `2M⁺ = 4N` e `2M⁻ = 4N - 2`. -/
theorem fita_dois_pares (N : Nat) :
    (∀ k, 1 ≤ k → k ≤ N → fitaA k + fitaB N k 0 = 4 * N) ∧
    (∀ k, 1 ≤ k → k ≤ N → fitaA k + fitaB N k 1 = 4 * N - 2) := by
  constructor
  · intro k hk hkN
    simpa using fita_soma N k 0 hk hkN (by omega)
  · intro k hk hkN
    simpa using fita_soma N k 1 hk hkN (by omega)

/-- **A fita é a mesma reflexão.**  No modo normal, `b_k` é o complemento de
    `a_k` em `4N`: a fita não contém mais informação do que o mapa
    `x ↦ 4N - x`.  Com `3C = 2N` isto coincide com o acoplamento `Φ`
    (ver `Acoplamento.acoplamento_e_reflexao`). -/
theorem fita_complemento (N k : Nat) :
    fitaB N k 0 = 4 * N - fitaA k := by
  simp only [fitaA, fitaB]
  omega

end Goldbach
