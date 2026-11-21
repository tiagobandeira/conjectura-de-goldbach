/-
  Goldbach/Projecao.lean
  ----------------------
  Até onde as janelas `W_i` alcançam: a caracterização exacta do conjunto de
  pares que a geometria da grade pode produzir.

  ## Resultado central

  Uma janela `W_i` da grade `G_{3,C}` tem alvo `n = 2·âncora = 4C + 4i + 2`.
  Os três eixos produzem três pares `(x, n - x)` com

      D₁ : x = 2i - 1 ,    D₂ : x = 2i + 3 ,    C_v : x = 2i + 1 .

  O eixo `D₂` é o mais generoso, e o limite é

      4x ≤ n + 6      isto é      x ≤ n/4 + 3/2 .

  Ou seja: **a geometria restringe o membro menor do par a um quarto do alvo.**
  Nada mais.  Este é o conteúdo exacto do «evento restritivo» — e é também a
  razão pela qual ele tem, heuristicamente, a mesma dificuldade do enunciado
  clássico: um factor 2 no conjunto de candidatos não muda a ordem de grandeza.
-/
import Goldbach.Heranca

namespace Goldbach

/-! ## Cobertura: todo par com membro menor `≤ n/4 + 1` é alcançado -/

/-- **A janela alcança todos os pares pequenos.**  Para `n = 4s + 2` e todo
    ímpar `x = 2j + 3` com `2j + 1 ≤ s` (i.e. `x ≤ n/4 + 3/2`), existe uma
    janela `(C, i) = (s - j, j)` cujo eixo `D₂` tem extremos exactamente `x` e
    `n - x`. -/
theorem janela_alcanca (s j : Nat) (hj : 1 ≤ j) (hjs : 2 * j + 1 ≤ s) :
    1 ≤ j ∧ j + 1 ≤ s - j ∧
    2 * grade (s - j) 1 j = 4 * s + 2 ∧
    grade (s - j) 0 (j + 1) = 2 * j + 3 := by
  refine ⟨by omega, by omega, ?_, ?_⟩ <;>
    simp only [grade] <;>
    omega

/-- O par produzido soma o alvo: os dois extremos de `D₂` somam `2·âncora`. -/
theorem janela_alcanca_soma (s j : Nat) (hj : 1 ≤ j) :
    grade (s - j) 2 (j - 1) + grade (s - j) 0 (j + 1) = 2 * grade (s - j) 1 j := by
  simp only [grade]
  omega

/-! ## Limite: nenhuma janela alcança par com membro menor `> n/4` -/

/-- **A janela não alcança além de `n/4`.**  Em qualquer janela `(C, i)`, o
    membro menor do par do eixo `D₂` satisfaz `4x ≤ n + 6`.  Como `D₁` e `C_v`
    são ainda mais restritivos, este é o alcance máximo da grade. -/
theorem janela_limite (C i : Nat) (hiC : i + 1 ≤ C) :
    4 * grade C 0 (i + 1) ≤ 2 * grade C 1 i + 6 := by
  simp only [grade]
  omega

/-- Versão para `D₁`, mais restritiva: `4x ≤ n - 10`. -/
theorem janela_limite_d1 (C i : Nat) (hi : 1 ≤ i) (hiC : i + 1 ≤ C) :
    4 * grade C 0 (i - 1) ≤ 2 * grade C 1 i - 10 := by
  simp only [grade]
  omega

/-- Versão para `C_v`: `4x ≤ n - 2`. -/
theorem janela_limite_cv (C i : Nat) (hiC : i + 1 ≤ C) :
    4 * grade C 0 i ≤ 2 * grade C 1 i - 2 := by
  simp only [grade]
  omega

/-- Todo alvo de janela é `≡ 2 (mod 4)`. -/
theorem alvo_par_quatro (C i : Nat) : (2 * grade C 1 i) % 4 = 2 := by
  simp only [grade]
  omega

/-! ## Consistência com a fita: a classe de resíduo forçada -/

/-- **A janela auto-consistente só atinge `n ≡ 6 (mod 12)`.**  Exigir que a
    janela contenha um par completo de `Φ` (i.e. que as duas leituras de `W_i`
    coincidam, `C = 2i+1`) força o alvo para a classe `6 (mod 12)` — um sexto
    dos inteiros, um terço dos pares.

    É este o tipo de restrição que a geometria *pode* dar: consistência entre
    descrições ⇒ classes de resíduo.  O preço é cobertura. -/
theorem central_mod_doze (i : Nat) :
    (2 * grade (2 * i + 1) 1 i) % 12 = 6 := by
  simp only [grade]
  omega

/-! ## `HR⁺` falha onde a âncora é composta -/

/-- Em `n = 18` só há uma janela, e a sua âncora é `9`. -/
theorem ancora_18 (C i : Nat)
    (h : 2 * grade C 1 i = 18) : grade C 1 i = 9 := by
  simp only [grade] at *
  omega

/-- Logo `HR⁺` **falha em `18`**: qualquer tripla de qualquer janela com alvo
    `18` contém a âncora `9`, que não é prima.  E no entanto `HR⁻` verifica-se
    (`5 + 13 = 18`).  É exactamente a assimetria intuída: `HR⁻` sempre ocorre,
    `HR⁺` não. -/
theorem hrmais_falha_18 (C i : Nat)
    (h : 2 * grade C 1 i = 18) : ¬ Primo (grade C 1 i) := by
  have h9 := ancora_18 C i h
  rw [h9]
  exact nao_primo_nove

end Goldbach
