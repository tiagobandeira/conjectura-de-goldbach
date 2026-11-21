/-
  Goldbach/Acoplamento.lean
  -------------------------
  O acoplamento `Φ` entre a grade `G_{3,C}` e a fita `F_N`, sob a condição
  `3C = 2N` (Paper 07, §3).

      Φ(k) = ( f(1,k), f(3,C+1-k) )              se 1 ≤ k ≤ C
      Φ(k) = ( f(2,2C+1-k), f(2,k-C) )           se C < k ≤ 3C/2

  Em indexação 0-based, as colunas `k` (1-based) do artigo correspondem a
  `k-1`, `C-k`, `2C-k` e `k-C-1`.
-/
import Goldbach.Grade

namespace Goldbach

/-! ## As duas metades de `Φ` -/

/-- Primeira coordenada de `Φ` para `k ≤ C`: linha 1, percorrida da esquerda
    para a direita. -/
def phiLinha1 (C k : Nat) : Nat :=
  grade C 0 (k - 1)

/-- Segunda coordenada de `Φ` para `k ≤ C`: linha 3, percorrida da direita
    para a esquerda. -/
def phiLinha3 (C k : Nat) : Nat :=
  grade C 2 (C - k)

/-- Primeira coordenada de `Φ` para `k > C`: extremidade esquerda da linha 2. -/
def phiMeioEsq (C k : Nat) : Nat :=
  grade C 1 (2 * C - k)

/-- Segunda coordenada de `Φ` para `k > C`: extremidade direita da linha 2. -/
def phiMeioDir (C k : Nat) : Nat :=
  grade C 1 (k - C - 1)

/-! ## Soma constante `6C = 4N` (Proposição 3.5) -/

/-- Metade externa (`k ≤ C`): `f(1,k) + f(3,C+1-k) = 6C`. -/
theorem phi_soma_externa (C k : Nat) (hk : 1 ≤ k) (hkC : k ≤ C) :
    phiLinha1 C k + phiLinha3 C k = 6 * C := by
  simp only [phiLinha1, phiLinha3, grade]
  omega

/-- Metade interna (`C < k ≤ 3C/2`): `f(2,2C+1-k) + f(2,k-C) = 6C`. -/
theorem phi_soma_meio (C k : Nat) (hk : C + 1 ≤ k) (hk2 : k ≤ 3 * C / 2) :
    phiMeioEsq C k + phiMeioDir C k = 6 * C := by
  simp only [phiMeioEsq, phiMeioDir, grade]
  omega

/-- Corolário principal: **todo** par `Φ(k)` soma `6C = 4N = 2M⁺`,
    independentemente de primalidade. -/
theorem phi_soma_total (C : Nat) :
    (∀ k, 1 ≤ k → k ≤ C → phiLinha1 C k + phiLinha3 C k = 6 * C) ∧
    (∀ k, C + 1 ≤ k → k ≤ 3 * C / 2 → phiMeioEsq C k + phiMeioDir C k = 6 * C) :=
  ⟨fun k hk hkC => phi_soma_externa C k hk hkC,
   fun k hk hk2 => phi_soma_meio C k hk hk2⟩

/-! ## Injetividade (a "bijeção" de `Φ`) -/

/-- A primeira coordenada é estritamente crescente em `k` (logo injetiva):
    as colunas `k ≤ C` cobrem a linha 1 sem repetição. -/
theorem phi_linha1_injetiva (C k₁ k₂ : Nat) (h1 : 1 ≤ k₁) (h2 : 1 ≤ k₂)
    (h : phiLinha1 C k₁ = phiLinha1 C k₂) : k₁ = k₂ := by
  simp only [phiLinha1, grade] at h
  omega

/-- A segunda coordenada é estritamente decrescente em `k`, logo injetiva. -/
theorem phi_linha3_injetiva (C k₁ k₂ : Nat) (h1 : k₁ ≤ C) (h2 : k₂ ≤ C)
    (h : phiLinha3 C k₁ = phiLinha3 C k₂) : k₁ = k₂ := by
  simp only [phiLinha3, grade] at h
  omega

/-- Sobrevivência da linha 1: toda célula `f(1,c)` aparece como primeira
    coordenada de algum `k ≤ C` (tome `k = c`). -/
theorem phi_linha1_sobrejetiva (C c : Nat) (hc : 1 ≤ c) (hcC : c ≤ C) :
    ∃ k, 1 ≤ k ∧ k ≤ C ∧ phiLinha1 C k = grade C 0 (c - 1) :=
  ⟨c, hc, hcC, rfl⟩

/-- Sobrevivência da linha 3: toda célula `f(3,c)` aparece como segunda
    coordenada de algum `k ≤ C` (tome `k = C + 1 - c`). -/
theorem phi_linha3_sobrejetiva (C c : Nat) (hc : 1 ≤ c) (hcC : c ≤ C) :
    ∃ k, 1 ≤ k ∧ k ≤ C ∧ phiLinha3 C k = grade C 2 (c - 1) :=
  ⟨C + 1 - c, by omega, by omega,
   by simp only [phiLinha3]; congr 1; omega⟩

/-! ## O acoplamento é a reflexão `x ↦ 6C - x`

Este é o resultado que fecha a via «usar `Φ` como passo não-translacional»:
`Φ` não tem estrutura própria.  Cada par de `Φ` é `{x, 6C - x}`, i.e. `Φ` é
simplesmente a reflexão em torno de `3C`.  Não há, portanto, nenhum passo
induzido por `Φ` além do complemento — e o complemento não preserva o
incremento da soma, logo não gera dinâmica ao longo dos pares.
-/

/-- Na metade externa, a segunda coordenada é o complemento da primeira. -/
theorem phi_complemento (C k : Nat) (hk : 1 ≤ k) (hkC : k ≤ C) :
    phiLinha3 C k = 6 * C - phiLinha1 C k := by
  simp only [phiLinha1, phiLinha3, grade]
  omega

/-- Na metade interna, o mesmo: `Φ` é a reflexão `x ↦ 6C - x`. -/
theorem phi_meio_complemento (C k : Nat) (hk : C + 1 ≤ k) (hk2 : k ≤ 3 * C / 2) :
    phiMeioDir C k = 6 * C - phiMeioEsq C k := by
  simp only [phiMeioEsq, phiMeioDir, grade]
  omega

/-- **O acoplamento é a reflexão.**  Em qualquer das duas metades, o par de `Φ`
    é `{x, 6C - x}`: não há conteúdo além do complemento em `G_{3,C}`. -/
theorem acoplamento_e_reflexao (C : Nat) :
    (∀ k, 1 ≤ k → k ≤ C → phiLinha1 C k + phiLinha3 C k = 6 * C) ∧
    (∀ k, C + 1 ≤ k → k ≤ 3 * C / 2 → phiMeioEsq C k + phiMeioDir C k = 6 * C) ∧
    (∀ k, 1 ≤ k → k ≤ C → phiLinha3 C k = 6 * C - phiLinha1 C k) ∧
    (∀ k, C + 1 ≤ k → k ≤ 3 * C / 2 → phiMeioDir C k = 6 * C - phiMeioEsq C k) :=
  ⟨fun k hk hkC => phi_soma_externa C k hk hkC,
   fun k hk hk2 => phi_soma_meio C k hk hk2,
   fun k hk hkC => phi_complemento C k hk hkC,
   fun k hk hk2 => phi_meio_complemento C k hk hk2⟩

end Goldbach
