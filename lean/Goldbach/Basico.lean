/-
  Goldbach/Basico.lean
  --------------------
  Camada zero: primalidade, paridade e a noção de representação de Goldbach.

  O núcleo do Lean 4 (sem Mathlib) não fornece `Nat.Prime`, `Even` nem `Odd`,
  por isso o projecto define as suas próprias noções, o que tem a vantagem de
  tornar explícito exactamente o que está a ser usado em cada demonstração.

  Nenhum módulo desta pasta depende de Mathlib.
-/
import Init

namespace Goldbach

/-! ## Primalidade -/

/-- `n` é primo: `n ≥ 2` e os únicos divisores de `n` são `1` e `n`. -/
def Primo (n : Nat) : Prop :=
  2 ≤ n ∧ ∀ m, m ∣ n → m = 1 ∨ m = n

/-- `1` não é primo. -/
theorem nao_primo_um : ¬ Primo 1 := by
  rintro ⟨h, _⟩
  omega

/-- Todo primo é `≥ 2`. -/
theorem primo_ge_dois {p : Nat} (h : Primo p) : 2 ≤ p := h.1

/-! ## Paridade -/

/-- `n` é par. -/
def Par (n : Nat) : Prop :=
  ∃ k, n = 2 * k

/-- `n` é ímpar. -/
def Impar (n : Nat) : Prop :=
  ∃ k, n = 2 * k + 1

/-- Todo número da forma `2m + 1` é ímpar. -/
theorem impar_forma (m : Nat) : Impar (2 * m + 1) :=
  ⟨m, rfl⟩

/-- Todo número da forma `2m` é par. -/
theorem par_forma (m : Nat) : Par (2 * m) :=
  ⟨m, rfl⟩

/-- Soma de dois ímpares é par. -/
theorem par_soma_impares {a b : Nat} (ha : Impar a) (hb : Impar b) : Par (a + b) := by
  obtain ⟨x, rfl⟩ := ha
  obtain ⟨y, rfl⟩ := hb
  exact ⟨x + y + 1, by omega⟩

/-- `3` é ímpar. -/
theorem impar_tres : Impar 3 :=
  ⟨1, rfl⟩

/-! ## Representação de Goldbach -/

/-- `n` admite uma representação de Goldbach (conjectura forte):
    `n = p + q` com `p` e `q` primos. -/
def TemRepGoldbach (n : Nat) : Prop :=
  ∃ p q : Nat, Primo p ∧ Primo q ∧ p + q = n

end Goldbach
