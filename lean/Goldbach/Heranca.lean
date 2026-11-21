/-
  Goldbach/Heranca.lean
  ---------------------
  O mecanismo de **herança** entre pares, e o diagnóstico de por que a
  formulação actual de `HR⁻` colapsa na Conjectura de Goldbach.

  ## Conteúdo

  1. `parDiagonal` — a fita enumera *todos* os pares de ímpares que somam `4N`.
     Este é o facto que esvazia o conteúdo de `HR⁻`: «estar na fita» não
     restringe nada (`parDiagonal_sobrejetiva`).

  2. `Passo` / `cadeia_certificada` — a herança geométrica de facto: um par
     certificado para `2M` dá um candidato a par para `2M+2` deslocando **uma**
     coordenada em `+2`.  A certificação do elo seguinte exige `p+2` primo
     (`transporte_certificado`), hipótese que não decorre de `p` primo.

  3. `eixo_extremos_soma` / `eixo_goldbach` — a leitura por janelas 3×3: os
     extremos de qualquer dos três eixos de `W_i` somam `2·f(2,i+1)`, o dobro
     da âncora.  Dois primos num eixo certificam Goldbach para `2·âncora`.

  4. `alvo_mod_quatro` — a certificação por âncora só atinge `n ≡ 2 (mod 4)`.

  5. `leitura_dupla` — a janela `W_i` como submatriz (soma `2·âncora`) e a
     janela como recipiente do scanner (soma `6C`) só coincidem quando
     `C = 2i+1`.
-/
import Goldbach.Grade
import Goldbach.Acoplamento

namespace Goldbach

/-! ## 1. A fita não restringe nada -/

/-- O `k`-ésimo par diagonal da fita `F_N^1`: `(a_{k+1}, b_k^{(1)})`. -/
def parDiagonal (N k : Nat) : Nat × Nat :=
  (2 * k + 1, 4 * N - 2 * k - 1)

/-- Todo par diagonal soma o par alvo `4N`. -/
theorem parDiagonal_soma (N k : Nat) (hk : 1 ≤ k) (hkN : k ≤ N) :
    (parDiagonal N k).1 + (parDiagonal N k).2 = 4 * N := by
  simp only [parDiagonal]
  omega

/-- **A fita enumera todos os pares.**  Para todo ímpar `x` com `3 ≤ x ≤ 2N-1`
    existe um `k` tal que `x` é a primeira coordenada do `k`-ésimo par
    diagonal.  Consequentemente, «o par está na fita» não impõe restrição
    alguma sobre o par: qualquer representação de `4N` por dois ímpares aparece
    na fita.  É por isso que `HR⁻`, tal como enunciada, coincide com Goldbach. -/
theorem parDiagonal_sobrejetiva (N x : Nat) (hx : Impar x) (h3 : 3 ≤ x)
    (hxN : x ≤ 2 * N - 1) :
    ∃ k, 1 ≤ k ∧ k ≤ N - 1 ∧ (parDiagonal N k).1 = x := by
  obtain ⟨m, hm⟩ := hx
  refine ⟨m, by omega, by omega, ?_⟩
  simp only [parDiagonal]
  omega

/-! ## 2. O passo de herança -/

/-- Um passo de herança: deslocar **uma** coordenada em `+2`, o que somam `+2`
    ao total.  É o único passo que a geometria da fita oferece. -/
def Passo (a b : Nat × Nat) : Prop :=
  b = (a.1 + 2, a.2) ∨ b = (a.1, a.2 + 2)

/-- O passo de herança acrescenta exactamente `2` à soma. -/
theorem passo_soma {a b : Nat × Nat} (h : Passo a b) :
    b.1 + b.2 = a.1 + a.2 + 2 := by
  rcases h with h | h <;> rw [h] <;> simp <;> omega

/-- A certificação do elo seguinte é **exactamente** `p+2` primo: o passo de
    herança troca a hipótese «`p` primo» por «`p+2` primo», e nada garante a
    segunda.  É aqui que a herança perde informação. -/
theorem transporte_certificado (p q : Nat) :
    (Primo ((p + 2, q) : Nat × Nat).1 ↔ Primo (p + 2)) ∧
    (Primo ((p + 2, q) : Nat × Nat).2 ↔ Primo q) :=
  ⟨Iff.rfl, Iff.rfl⟩

/-- A soma dos pares ao longo de uma cadeia de herança cresce `+2` por passo. -/
theorem cadeia_soma (f : Nat → Nat × Nat) (hpasso : ∀ j, Passo (f j) (f (j + 1))) :
    ∀ j, (f j).1 + (f j).2 = (f 0).1 + (f 0).2 + 2 * j := by
  intro j
  induction j with
  | zero => simp
  | succ j ih =>
    have hs := passo_soma (hpasso j)
    omega

/-- **Motor por herança genuína.**  Se existe uma cadeia
    `(p₀,q₀) → (p₁,q₁) → …` em que cada elo é um `Passo` e em que **todas** as
    coordenadas de todos os elos são primas, então os pares
    `p₀+q₀, p₀+q₀+2, p₀+q₀+4, …` são todos de Goldbach.

    Note-se a diferença face a `teorema_motor` (Paper 07): a hipótese aqui é
    uma **cadeia relacionada**, não uma escolha arbitrária de par por par.  É
    mais fraca em extensão (cobre só pares atingíveis por transporte) e mais
    forte em conteúdo (exige coerência entre elos consecutivos). -/
theorem cadeia_certificada (f : Nat → Nat × Nat)
    (hpasso : ∀ j, Passo (f j) (f (j + 1)))
    (hcert : ∀ j, Primo (f j).1 ∧ Primo (f j).2) :
    ∀ j, TemRepGoldbach ((f 0).1 + (f 0).2 + 2 * j) := by
  intro j
  have hs := cadeia_soma f hpasso j
  exact ⟨(f j).1, (f j).2, (hcert j).1, (hcert j).2, hs⟩

/-! ## 3. A leitura por janelas 3×3 -/

/-- **Os três eixos de `W_i`.**  Os extremos de `D₁`, `D₂` e `C_v` somam todos
    `2·f(2,i+1)` — o dobro da âncora da janela.  (Na indexação 1-based do
    artigo: `f(1,i)+f(3,i+2) = f(3,i)+f(1,i+2) = f(1,i+1)+f(3,i+1) = 2f(2,i+1)`.) -/
theorem eixo_extremos_soma (N i : Nat) (hi : 1 ≤ i) :
    grade N 0 (i - 1) + grade N 2 (i + 1) = 2 * grade N 1 i ∧
    grade N 2 (i - 1) + grade N 0 (i + 1) = 2 * grade N 1 i ∧
    grade N 0 i + grade N 2 i = 2 * grade N 1 i := by
  refine ⟨?_, ?_, ?_⟩ <;>
    simp only [grade] <;>
    omega

/-- **Certificação por janela.**  Se os dois extremos de um eixo de `W_i` são
    primos, então `2·âncora` é soma de dois primos.  Este é o conteúdo preciso
    da «extensão de `HR⁺` a três números»: a janela não procura um par
    qualquer — prescreve três pares concretos. -/
theorem eixo_goldbach (N i : Nat) (hi : 1 ≤ i)
    (hp : Primo (grade N 0 (i - 1))) (hq : Primo (grade N 2 (i + 1))) :
    TemRepGoldbach (2 * grade N 1 i) := by
  refine ⟨grade N 0 (i - 1), grade N 2 (i + 1), hp, hq, ?_⟩
  exact (eixo_extremos_soma N i hi).1

/-- D2 dá a mesma conclusão. -/
theorem eixo_goldbach' (N i : Nat) (hi : 1 ≤ i)
    (hp : Primo (grade N 2 (i - 1))) (hq : Primo (grade N 0 (i + 1))) :
    TemRepGoldbach (2 * grade N 1 i) := by
  refine ⟨grade N 2 (i - 1), grade N 0 (i + 1), hp, hq, ?_⟩
  exact (eixo_extremos_soma N i hi).2.1

/-- `C_v` dá a mesma conclusão. -/
theorem eixo_goldbach'' (N i : Nat) (hi : 1 ≤ i)
    (hp : Primo (grade N 0 i)) (hq : Primo (grade N 2 i)) :
    TemRepGoldbach (2 * grade N 1 i) := by
  refine ⟨grade N 0 i, grade N 2 i, hp, hq, ?_⟩
  exact (eixo_extremos_soma N i hi).2.2

/-! ## 4. Limite de cobertura da certificação por âncora -/

/-- **A certificação por janela só atinge `n ≡ 2 (mod 4)`.**  A âncora é ímpar,
    logo o dobro é `2 (mod 4)`.  Os pares `≡ 0 (mod 4)` (que são os que a fita
    fornece, com soma `4N`) têm de ser certificados pela fita, não pela janela.

    Consequência: um «motor» que use só janelas nunca cobre metade dos pares. -/
theorem alvo_mod_quatro (N i : Nat) : (2 * grade N 1 i) % 4 = 2 := by
  simp only [grade]
  omega

/-! ## 5. As duas leituras de `W_i` -/

/-- A janela como **submatriz** dá soma `2·âncora`; a janela como **recipiente do
    scanner** dá soma `6C`.  As duas leituras coincidem para uma única janela
    em cada grade: `C = 2i+1`. -/
theorem leitura_dupla (C i : Nat) :
    2 * grade C 1 i = 6 * C ↔ C = 2 * i + 1 := by
  simp only [grade]
  omega

/-! ## 6. Compostos: o concreto que falta ao teste -/

/-- `n` é composto quando tem um divisor próprio `≥ 2`. -/
def Composto (n : Nat) : Prop :=
  ∃ m, 2 ≤ m ∧ m < n ∧ m ∣ n

/-- Um composto nunca é primo. -/
theorem nao_primo_de_composto {n : Nat} (h : Composto n) : ¬ Primo n := by
  rintro ⟨_, hdiv⟩
  obtain ⟨m, hm2, hmn, hmdvd⟩ := h
  have := hdiv m hmdvd
  omega

/-- `9 = grade 3 0 4` é composto: o extremo de `D₁` na janela `N=3, i=5`. -/
theorem composto_9 : Composto 9 :=
  ⟨3, by omega, by omega, ⟨3, by omega⟩⟩

/-- Em particular, o extremo `9` da janela `N=3, i=5` não certifica nada. -/
theorem nao_primo_nove : ¬ Primo 9 :=
  nao_primo_de_composto composto_9

end Goldbach
