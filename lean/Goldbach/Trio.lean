/-
  Goldbach/Trio.lean
  ------------------
  Paper 04, §6: uma configuração totalmente prima produz três representações
  binárias de Goldbach e uma representação ternária.

  Indexação: `i` é a coluna central da janela `W_i`, contada a partir de 1
  (como no artigo).  As células de `D₁` são `(1,i), (2,i+1), (3,i+2)` na
  indexação do artigo, i.e. `grade N 0 (i-1)`, `grade N 1 i`, `grade N 2 (i+1)`
  na indexação 0-based usada internamente.
-/
import Goldbach.Grade

namespace Goldbach

/-! ## Somas explícitas dos pares de `D₁` -/

/-- `f(1,i) + f(2,i+1) = 2(N + 2i)`. -/
theorem soma_d1_ab (N i : Nat) (hi : 1 ≤ i) :
    grade N 0 (i - 1) + grade N 1 i = 2 * (N + 2 * i) := by
  simp only [grade]
  omega

/-- `f(1,i) + f(3,i+2) = 2(2N + 2i + 1)` — o dobro da âncora. -/
theorem soma_d1_ac (N i : Nat) (hi : 1 ≤ i) :
    grade N 0 (i - 1) + grade N 2 (i + 1) = 2 * (2 * N + 2 * i + 1) := by
  simp only [grade]
  omega

/-- `f(2,i+1) + f(3,i+2) = 2(3N + 2i + 2)`. -/
theorem soma_d1_bc (N i : Nat) :
    grade N 1 i + grade N 2 (i + 1) = 2 * (3 * N + 2 * i + 2) := by
  simp only [grade]
  omega

/-! ## Teorema do trio -/

/-- **Teorema do trio.** Se os três elementos de `D₁` na janela `W_i` são
    primos, então os três pares que eles formam são representações de Goldbach
    para três números pares. -/
theorem trio_d1_goldbach (N i : Nat)
    (hpa : Primo (grade N 0 (i - 1)))
    (hpb : Primo (grade N 1 i))
    (hpc : Primo (grade N 2 (i + 1))) :
    TemRepGoldbach (grade N 0 (i - 1) + grade N 1 i) ∧
    TemRepGoldbach (grade N 0 (i - 1) + grade N 2 (i + 1)) ∧
    TemRepGoldbach (grade N 1 i + grade N 2 (i + 1)) :=
  ⟨⟨_, _, hpa, hpb, rfl⟩, ⟨_, _, hpa, hpc, rfl⟩, ⟨_, _, hpb, hpc, rfl⟩⟩

/-- As três somas são pares (soma de dois ímpares). -/
theorem trio_d1_pares (N i : Nat) :
    Par (grade N 0 (i - 1) + grade N 1 i) ∧
    Par (grade N 0 (i - 1) + grade N 2 (i + 1)) ∧
    Par (grade N 1 i + grade N 2 (i + 1)) :=
  ⟨par_soma_impares (grade_impar N _ _) (grade_impar N _ _),
   par_soma_impares (grade_impar N _ _) (grade_impar N _ _),
   par_soma_impares (grade_impar N _ _) (grade_impar N _ _)⟩

/-- As três somas são distintas duas a duas (para `N, i ≥ 1`). -/
theorem trio_d1_distintas (N i : Nat) (hN : 1 ≤ N) (hi : 1 ≤ i) :
    grade N 0 (i - 1) + grade N 1 i ≠ grade N 0 (i - 1) + grade N 2 (i + 1) ∧
    grade N 0 (i - 1) + grade N 1 i ≠ grade N 1 i + grade N 2 (i + 1) ∧
    grade N 0 (i - 1) + grade N 2 (i + 1) ≠ grade N 1 i + grade N 2 (i + 1) := by
  refine ⟨?_, ?_, ?_⟩ <;>
    simp only [grade] <;>
    omega

/-- **Corolário ternário.** O trio soma `S(i) = 3(2N + 2i + 1)`, um ímpar > 5
    para `N ≥ 3`: cada trio primo testemunha também a forma ternária. -/
theorem trio_d1_ternaria (N i : Nat) (hN : 3 ≤ N) (hi : 1 ≤ i) :
    diagPrincipal N i = somaJanela N i ∧ Impar (diagPrincipal N i) ∧ 5 < diagPrincipal N i := by
  have hS := lema_soma_constante N i hi
  refine ⟨hS.1, ?_, ?_⟩
  · rw [hS.1]
    exact somaJanela_impar N i
  · rw [hS.1]
    simp only [somaJanela]
    omega

end Goldbach
