/-
  Goldbach/Motor.lean
  -------------------
  Camada aritmética do Motor de Herança Estrutural (Paper 07, §8).

  Este módulo formaliza:

  * as Hipóteses Restritivas `HR⁻` e `HR⁺`;
  * a implicação `HR⁺ ⇒ HR⁻`;
  * o enunciado do Teorema do Motor e a sua verificação.

  A Observação E-1 do `TrustLedger.md` discute a força lógica de `HR⁻`:
  formalizada como abaixo, ela *é* a Conjectura de Goldbach ponto a ponto,
  de modo que o Teorema do Motor é contabilidade de cadeia, não progresso.
-/
import Goldbach.Basico

namespace Goldbach

/-! ## Hipóteses Restritivas -/

/-- **HR⁻** (fraca): existe um passo `t ∈ [1,K]` da varredura em que **ambos**
    os extremos do par diagonal são primos. -/
def HRmenos (K : Nat) (ext : Nat → Nat × Nat) : Prop :=
  ∃ t, 1 ≤ t ∧ t ≤ K ∧ Primo (ext t).1 ∧ Primo (ext t).2

/-- **HR⁺** (forte): existe um passo em que a tripla completa é prima. -/
def HRmais (K : Nat) (tri : Nat → Nat × Nat × Nat) : Prop :=
  ∃ t, 1 ≤ t ∧ t ≤ K ∧
    Primo (tri t).1 ∧ Primo (tri t).2.1 ∧ Primo (tri t).2.2

/-- `HR⁺` implica `HR⁻` (Paper 07, Observação 8.3): uma tripla totalmente
    prima fornece em particular dois extremos primos. -/
theorem hr_mais_implica_hr_menos (K : Nat) (tri : Nat → Nat × Nat × Nat) (h : HRmais K tri) :
    HRmenos K (fun t => ((tri t).1, (tri t).2.2)) := by
  obtain ⟨t, ht1, ht2, h1, h2, h3⟩ := h
  exact ⟨t, ht1, ht2, h1, h3⟩

/-! ## A cadeia do motor -/

/-- Uma cadeia de pares certificados: para cada `j`, o par `j` soma
    `base + 2j` e é formado por dois primos. -/
def Cadeia (base : Nat) (par : Nat → Nat × Nat) : Prop :=
  ∀ j, Primo (par j).1 ∧ Primo (par j).2 ∧ (par j).1 + (par j).2 = base + 2 * j

/-- **Teorema do Motor** (Paper 07, Teorema 8.4).  Dada uma cadeia de pares
    certificados a partir do par base `base`, todo par `base + 2j` é soma de
    dois primos.

    Nota: por construção, `Cadeia` já *contém* a certificação de primalidade de
    cada elo.  O conteúdo formal do teorema é portanto que a indexação da
    cadeia está correta — o trabalho matemático está inteiramente na obtenção
    de `Cadeia`, isto é, em `HR⁻`. -/
theorem teorema_motor (base : Nat) (par : Nat → Nat × Nat) (h : Cadeia base par) :
    ∀ j, TemRepGoldbach (base + 2 * j) := by
  intro j
  obtain ⟨h1, h2, h3⟩ := h j
  exact ⟨(par j).1, (par j).2, h1, h2, h3⟩

/-- Versão "ponto a ponto": se para cada `j` existe um par de primos somando
    `base + 2j`, então todos os pares a partir de `base` admitem Goldbach.
    Esta é exactamente a força de `HR⁻` aplicada iterativamente. -/
theorem hr_menos_implica_goldbach (base : Nat) (p₁ p₂ : Nat → Nat)
    (h1 : ∀ j, Primo (p₁ j)) (h2 : ∀ j, Primo (p₂ j))
    (hsum : ∀ j, p₁ j + p₂ j = base + 2 * j) :
    ∀ j, TemRepGoldbach (base + 2 * j) :=
  fun j => ⟨p₁ j, p₂ j, h1 j, h2 j, hsum j⟩

end Goldbach
