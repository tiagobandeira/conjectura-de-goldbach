/-
  Goldbach/Cadeia.lean
  --------------------
  O limite estrutural do mecanismo de herança.

  ## Resultado

  A cadeia de transporte `(p,q) → (p+2,q) → …` desloca uma coordenada de `2`
  em `2`.  Mas três ímpares consecutivos de passo 2 nunca são todos primos:
  um deles é múltiplo de 3.  Logo:

  * uma coordenada pode avançar **no máximo uma vez** (para `> 3`);
  * uma cadeia certificada tem comprimento **no máximo 2** (3 se uma das
    coordenadas começar em `3`, o caso degenerado `3, 5, 7`).

  Consequência: o «motor» não transporta pares ao longo dos pares; ele avança
  um ou dois passos a partir de cada par base e tem de **recomeçar**.  Ou seja:
  o mecanismo é de *cobertura*, não de *herança* — e uma cobertura é, por
  definição, Goldbach ponto a ponto.
-/
import Goldbach.Basico

namespace Goldbach

/-! ## Três ímpares consecutivos de passo 2 -/

/-- Entre `p`, `p+2` e `p+4`, um é divisível por 3. -/
theorem tres_consecutivos_multiplo (p : Nat) :
    3 ∣ p ∨ 3 ∣ p + 2 ∨ 3 ∣ p + 4 := by
  have h : p % 3 = 0 ∨ p % 3 = 1 ∨ p % 3 = 2 := by omega
  rcases h with h | h | h
  · exact Or.inl (Nat.dvd_of_mod_eq_zero h)
  · right; left
    apply Nat.dvd_of_mod_eq_zero
    rw [Nat.add_mod, h]
  · right; right
    apply Nat.dvd_of_mod_eq_zero
    rw [Nat.add_mod, h]

/-- **Nenhum primo `> 3` inicia uma corrida de três.**  `p`, `p+2` e `p+4` não
    podem ser todos primos quando `p > 3`. -/
theorem nao_tres_primos (p : Nat) (hp3 : 3 < p)
    (h1 : Primo p) (h2 : Primo (p + 2)) (h3 : Primo (p + 4)) : False := by
  rcases tres_consecutivos_multiplo p with h | h | h
  · have := h1.2 3 h
    omega
  · have := h2.2 3 h
    omega
  · have := h3.2 3 h
    omega

/-- Se `p, p+2, p+4` são primos, então `p = 3`. -/
theorem corrida_tres_implica_tres (p : Nat)
    (h1 : Primo p) (h2 : Primo (p + 2)) (h3 : Primo (p + 4)) : p ≤ 3 := by
  by_cases h : 3 < p
  · exact (nao_tres_primos p h h1 h2 h3).elim
  · omega

/-! ## O limite da cadeia -/

/-- **Cada coordenada avança no máximo uma vez.**  Numa cadeia certificada que
    parta de `(p,q)` com `p > 3`, não é possível deslocar a primeira
    coordenada duas vezes: isso exigiria `p`, `p+2` e `p+4` primos.  O mesmo
    para a segunda coordenada.

    Segue-se que uma cadeia certificada tem comprimento `≤ 2`: com três passos,
    uma das coordenadas teria de avançar duas vezes.  (Com `p = 3` ou `q = 3`
    o caso `3, 5, 7` permite um passo extra, nunca mais do que isso.) -/
theorem cadeia_limite (p q : Nat) (hp3 : 3 < p) (hq3 : 3 < q)
    (hp : Primo p) (hq : Primo q) :
    (¬ (Primo (p + 2) ∧ Primo (p + 4))) ∧
    (¬ (Primo (q + 2) ∧ Primo (q + 4))) := by
  constructor
  · rintro ⟨h2, h4⟩
    exact nao_tres_primos p hp3 hp h2 h4
  · rintro ⟨h2, h4⟩
    exact nao_tres_primos q hq3 hq h2 h4

end Goldbach
