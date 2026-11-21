/-
  Goldbach/Espectral.lean
  -----------------------
  A reformulação espectral do Paper 08 (Teorema 6.4):

      HR⁻  ⟺  F(t₀) ≠ 0 para algum t₀  ⟺  Σ_t F(t) ≥ 1  ⟺  F̂(0) > 0 ,

  onde `F(t) = 1_ℙ(E₁(t)) · 1_ℙ(E₂(t))` é a função de colisão.

  Como o próprio artigo observa (Observação 6.5), isto é uma reescrita e não
  uma prova: `F̂(0) > 0` tem exactamente o mesmo conteúdo lógico que `HR⁻`.
  O que a formalização abaixo estabelece é que a cadeia de equivalências é
  correcta — nada mais, nada menos.
-/
import Goldbach.Basico

open Classical

namespace Goldbach

/-! ## Função de colisão -/

/-- Indicador de primalidade com valores em `{0,1}`.  `Primo` não é decidível
    computacionalmente (quantifica sobre todos os divisores), pelo que a
    definição é clássica (não computável) — o que é sem consequência aqui,
    já que só se usam propriedades lógicas do indicador. -/
noncomputable def indicador (n : Nat) : Nat :=
  if Primo n then 1 else 0

/-- Função de colisão de `ext` no passo `t` (Paper 08, Definição 6.1). -/
noncomputable def colisao (ext : Nat → Nat × Nat) (t : Nat) : Nat :=
  indicador (ext t).1 * indicador (ext t).2

theorem colisao_eq_one_iff (ext : Nat → Nat × Nat) (t : Nat) :
    colisao ext t = 1 ↔ Primo (ext t).1 ∧ Primo (ext t).2 := by
  unfold colisao indicador
  by_cases h1 : Primo (ext t).1 <;>
    by_cases h2 : Primo (ext t).2 <;>
    simp [h1, h2]

theorem colisao_eq_zero_iff (ext : Nat → Nat × Nat) (t : Nat) :
    colisao ext t = 0 ↔ ¬ (Primo (ext t).1 ∧ Primo (ext t).2) := by
  unfold colisao indicador
  by_cases h1 : Primo (ext t).1 <;>
    by_cases h2 : Primo (ext t).2 <;>
    simp [h1, h2]

theorem colisao_le_one (ext : Nat → Nat × Nat) (t : Nat) : colisao ext t ≤ 1 := by
  unfold colisao indicador
  by_cases h1 : Primo (ext t).1 <;>
    by_cases h2 : Primo (ext t).2 <;>
    simp [h1, h2]

/-! ## Hipótese Restritiva em forma de colisão -/

/-- `HR⁻` reindexada a partir de `0`: existe um passo com colisão prima. -/
def HRcol (K : Nat) (ext : Nat → Nat × Nat) : Prop :=
  ∃ t, t < K ∧ Primo (ext t).1 ∧ Primo (ext t).2

/-! ## A soma espectral -/

/-- Soma parcial de `F` em `t = 0, …, K-1`. -/
noncomputable def somaColisao : Nat → (Nat → Nat × Nat) → Nat
  | 0, _ => 0
  | K + 1, ext => somaColisao K ext + colisao ext K

/-- `F̂(0) = (1/K)·Σ F(t)`; como `K > 0`, a positividade de `F̂(0)` é a
    positividade da soma, que é o objecto puramente combinatório. -/
noncomputable def Fhat0 (K : Nat) (ext : Nat → Nat × Nat) : Nat :=
  somaColisao K ext

theorem somaColisao_eq_zero_iff (K : Nat) (ext : Nat → Nat × Nat) :
    somaColisao K ext = 0 ↔ ∀ t, t < K → colisao ext t = 0 := by
  induction K with
  | zero => simp [somaColisao]
  | succ K ih =>
    rw [somaColisao, Nat.add_eq_zero_iff, ih]
    constructor
    · rintro ⟨h1, h2⟩ t ht
      rcases Nat.lt_succ_iff_lt_or_eq.mp ht with h | h
      · exact h1 t h
      · subst h; exact h2
    · intro h
      exact ⟨fun t ht => h t (by omega), h K (by omega)⟩

/-- `HR⁻` ⟺ a soma das colisões é não nula. -/
theorem hrcol_iff_soma_ne_zero (K : Nat) (ext : Nat → Nat × Nat) :
    HRcol K ext ↔ somaColisao K ext ≠ 0 := by
  constructor
  · rintro ⟨t, ht, h1, h2⟩ hzero
    have h0 : colisao ext t = 0 := (somaColisao_eq_zero_iff K ext).mp hzero t ht
    have hpos : colisao ext t = 1 := (colisao_eq_one_iff ext t).mpr ⟨h1, h2⟩
    omega
  · intro hne
    apply Classical.byContradiction
    intro hc
    apply hne
    rw [somaColisao_eq_zero_iff]
    intro t ht
    rw [colisao_eq_zero_iff]
    rintro ⟨h1, h2⟩
    exact hc ⟨t, ht, h1, h2⟩

/-- **Teorema 6.4**: `HR⁻` ⟺ `F̂(0) > 0`. -/
theorem hrcol_iff_Fhat0_pos (K : Nat) (ext : Nat → Nat × Nat) :
    HRcol K ext ↔ 0 < Fhat0 K ext := by
  unfold Fhat0
  rw [Nat.pos_iff_ne_zero]
  exact hrcol_iff_soma_ne_zero K ext

/-- A "média espectral" está em `[0,1]`: `Σ F(t) ≤ K`, isto é, `F̂(0) ≤ 1`. -/
theorem somaColisao_le (K : Nat) (ext : Nat → Nat × Nat) : somaColisao K ext ≤ K := by
  induction K with
  | zero => simp [somaColisao]
  | succ K ih =>
    rw [somaColisao]
    have := colisao_le_one ext K
    omega

/-- Corolário: `F̂(0) > 0` força a existência de um passo com colisão prima —
    sem qualquer hipótese sobre a distribuição dos primos. -/
theorem Fhat0_pos_implica_HRcol (K : Nat) (ext : Nat → Nat × Nat) (h : 0 < Fhat0 K ext) :
    HRcol K ext :=
  (hrcol_iff_Fhat0_pos K ext).mpr h

end Goldbach
