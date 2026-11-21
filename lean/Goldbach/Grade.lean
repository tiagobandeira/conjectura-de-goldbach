/-
  Goldbach/Grade.lean
  -------------------
  A grade `G_{k,N}` do Paper 04 ("Uma propriedade de soma constante na grade
  3×N"), formalizada sobre `Nat`.

  ## Convenção de indexação

  Internamente a grade é indexada a partir de **0**:

      grade N r c = 2 * (r * N + c) + 1 ,     r < k,  c < N ,

  ou seja, a célula `(r,c)` recebe o `(rN + c)`-ésimo ímpar positivo.

  É algebricamente idêntica a `f(r,c) = 2[(r-1)N + c] - 1` do artigo (que indexa
  a partir de 1): basta `r_artigo = r + 1` e `c_artigo = c + 1`.  A escolha
  0-based elimina todas as subtrações literais (`(2-1)*N`, …), que impedem o
  `omega` de reconhecer a linearidade das expressões.

  As *janelas* e os *enunciados* usam a indexação do artigo (a partir de 1),
  pelo que cada teorema abaixo corresponde literalmente ao seu homólogo no
  Paper 04.
-/
import Goldbach.Basico

namespace Goldbach

/-! ## Definições -/

/-- Célula `(r,c)` da grade `G_{k,N}` (indexação 0-based). -/
def grade (N r c : Nat) : Nat :=
  2 * (r * N + c) + 1

/-- Soma canônica da janela `W_i` (indexação 1-based, como no artigo):
    `S(i) = 3(2N + 2i + 1)`. -/
def somaJanela (N i : Nat) : Nat :=
  3 * (2 * N + 2 * i + 1)

/-- Diagonal principal de `W_i`: células 1-based `(1,i), (2,i+1), (3,i+2)`. -/
def diagPrincipal (N i : Nat) : Nat :=
  grade N 0 (i - 1) + grade N 1 i + grade N 2 (i + 1)

/-- Diagonal secundária de `W_i`: células 1-based `(3,i), (2,i+1), (1,i+2)`. -/
def diagSecundaria (N i : Nat) : Nat :=
  grade N 2 (i - 1) + grade N 1 i + grade N 0 (i + 1)

/-- Coluna central de `W_i`: células 1-based `(1,i+1), (2,i+1), (3,i+1)`. -/
def colunaCentral (N i : Nat) : Nat :=
  grade N 0 i + grade N 1 i + grade N 2 i

/-- Complemento oracle-free de `n` em relação à janela `W_i`: `C(n,i) = S(i) - n`. -/
def complemento (N i n : Nat) : Nat :=
  somaJanela N i - n

/-! ## Lema da Soma Constante (Paper 04, Lema 3.1) -/

theorem lema_soma_constante (N i : Nat) (hi : 1 ≤ i) :
    diagPrincipal N i = somaJanela N i ∧
    diagSecundaria N i = somaJanela N i ∧
    colunaCentral N i = somaJanela N i := by
  refine ⟨?_, ?_, ?_⟩ <;>
    simp only [diagPrincipal, diagSecundaria, colunaCentral, somaJanela, grade] <;>
    omega

/-! ## Corolário âncora (Paper 04, Corolário 3.2) -/

/-- O elemento mediano divide `S(i)` em três partes iguais: `3 · f(2,i+1) = S(i)`. -/
theorem corolario_ancora (N i : Nat) :
    3 * grade N 1 i = somaJanela N i := by
  simp only [grade, somaJanela]
  omega

/-- `S(i)` é sempre ímpar. -/
theorem somaJanela_impar (N i : Nat) : Impar (somaJanela N i) := by
  simp only [somaJanela]
  exact ⟨3 * N + 3 * i + 1, by omega⟩

/-- Proposição 3.4 (paridade do complemento): se `n` é ímpar e não excede
    `S(i)`, então `C(n,i)` é par. -/
theorem complemento_par (N i n : Nat) (hn : Impar n) (hle : n ≤ somaJanela N i) :
    Par (complemento N i n) := by
  obtain ⟨a, ha⟩ := somaJanela_impar N i
  obtain ⟨b, hb⟩ := hn
  refine ⟨a - b, ?_⟩
  simp only [complemento]
  omega

/-- Toda célula da grade é ímpar. -/
theorem grade_impar (N r c : Nat) : Impar (grade N r c) :=
  ⟨r * N + c, rfl⟩

/-- O complemento de qualquer célula da grade é par. -/
theorem complemento_de_celula_par (N i r c : Nat) (hle : grade N r c ≤ somaJanela N i) :
    Par (complemento N i (grade N r c)) :=
  complemento_par N i (grade N r c) (grade_impar N r c) hle

/-! ## Estrutura aritmética das configurações (Paper 04, §4) -/

/-- Propriedade 4.1: `D₁` é progressão aritmética de razão `2N + 2`. -/
theorem pa_d1 (N i : Nat) (hi : 1 ≤ i) :
    grade N 1 i - grade N 0 (i - 1) = 2 * N + 2 := by
  simp only [grade]
  omega

/-- Propriedade 4.1: segundo passo de `D₁`, mesma razão. -/
theorem pa_d1' (N i : Nat) :
    grade N 2 (i + 1) - grade N 1 i = 2 * N + 2 := by
  simp only [grade]
  omega

/-- Propriedade 4.1: `D₂` tem razão `2N - 2`. -/
theorem pa_d2 (N i : Nat) (hN : 1 ≤ N) :
    grade N 1 i - grade N 0 (i + 1) = 2 * N - 2 := by
  simp only [grade]
  omega

/-- Propriedade 4.1: segundo passo de `D₂`, mesma razão. -/
theorem pa_d2' (N i : Nat) (hi : 1 ≤ i) :
    grade N 2 (i - 1) - grade N 1 i = 2 * N - 2 := by
  simp only [grade]
  omega

/-- Propriedade 4.1: `C_v` tem razão `2N`. -/
theorem pa_cv (N i : Nat) :
    grade N 1 i - grade N 0 i = 2 * N := by
  simp only [grade]
  omega

/-- Propriedade 4.2: as diferenças entre linhas consecutivas são constantes. -/
theorem dif_linhas (N r c : Nat) :
    grade N (r + 1) c - grade N r c = 2 * N := by
  cases r with
  | zero => simp [grade]; omega
  | succ r =>
    simp only [grade, Nat.succ_mul]
    omega

/-- Propriedade 4.3 (uniformidade modular): `f(r,c) ≡ 2c + 1 (mod 2N)`
    na indexação 0-based, i.e. `≡ 2c - 1` na indexação do artigo. -/
theorem uniformidade_modular (N r c : Nat) :
    grade N r c % (2 * N) = (2 * c + 1) % (2 * N) := by
  have h2 : r * (2 * N) = 2 * (r * N) := by
    rw [← Nat.mul_assoc, Nat.mul_comm r 2, Nat.mul_assoc]
  have hrew : grade N r c = (2 * c + 1) + r * (2 * N) := by
    simp only [grade]
    rw [h2]
    omega
  rw [hrew, Nat.add_mul_mod_self_right]

/-! ## Generalização para grades `k × N` (Paper 04, §5) -/

/-- Soma das `k` primeiras linhas da coluna `c` (0-based). -/
def somaColuna : Nat → Nat → Nat → Nat
  | 0, _, _ => 0
  | k + 1, N, c => somaColuna k N c + grade N k c

/-- `k = 2`: `Σ₂ = 2(N + 2c + 1)`, sempre par (artigo: `2(N + 2j - 1)`, `j = c+1`). -/
theorem coluna_k2 (N c : Nat) :
    somaColuna 2 N c = 2 * (N + 2 * c + 1) := by
  simp [somaColuna, grade]
  omega

/-- `k = 3`: `Σ₃ = 3 · f(2,j)` — a âncora inteira existe. -/
theorem coluna_k3 (N c : Nat) :
    somaColuna 3 N c = 3 * grade N 1 c := by
  simp [somaColuna, grade]
  omega

/-- `k = 4`: `Σ₄ = 4(3N + 2c + 1)` (artigo: `4(3N + 2j - 1)`, `j = c+1`). -/
theorem coluna_k4 (N c : Nat) :
    somaColuna 4 N c = 4 * (3 * N + 2 * c + 1) := by
  simp [somaColuna, grade]
  omega

/-- `k = 5`: `Σ₅ = 5 · f(3,j)` — a âncora volta a existir. -/
theorem coluna_k5 (N c : Nat) :
    somaColuna 5 N c = 5 * grade N 2 c := by
  simp [somaColuna, grade]
  omega

/-- Para `k = 3` (ímpar), a soma da coluna é ímpar; logo o complemento `Σ - n`
    (com `n` ímpar) é par — a Série Singular é aplicável. -/
theorem coluna_k3_impar (N c : Nat) : Impar (somaColuna 3 N c) := by
  rw [coluna_k3]
  simp only [grade]
  exact ⟨3 * (N + c) + 1, by omega⟩

/-- Idem para `k = 5`. -/
theorem coluna_k5_impar (N c : Nat) : Impar (somaColuna 5 N c) := by
  rw [coluna_k5]
  simp only [grade]
  exact ⟨5 * (2 * N + c) + 2, by omega⟩

/-- Para `k` par, a soma da coluna é par, logo o complemento é **ímpar** — o
    oposto do que afirma o *enunciado* da Proposição 5.4 do Paper 04, que se
    contradiz com a sua própria demonstração e com a tabela resumo do artigo.
    Ver `TrustLedger.md`, item F-1. -/
theorem coluna_k4_par (N c : Nat) : Par (somaColuna 4 N c) := by
  rw [coluna_k4]
  exact ⟨2 * (3 * N + 2 * c + 1), by omega⟩

/-- Consequência: o complemento de `k = 4` é ímpar, não par. -/
theorem complemento_k4_impar (N c n : Nat) (hn : Impar n) (hle : n ≤ somaColuna 4 N c) :
    Impar (somaColuna 4 N c - n) := by
  obtain ⟨a, ha⟩ := coluna_k4_par N c
  obtain ⟨b, hb⟩ := hn
  exact ⟨a - b - 1, by omega⟩

end Goldbach
