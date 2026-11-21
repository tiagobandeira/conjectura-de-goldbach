# Trust Ledger — o que está provado, o que é hipótese, o que é evidência

Este documento é o mapa de confiança da série. Para cada afirmação relevante
dos 12 papers diz **onde ela vive**, **qual é o seu estatuto lógico** e, quando
aplicável, **qual o teorema Lean que a verifica**.

Legenda:

| Símbolo | Significado |
|---|---|
| ✅ | **Provado em Lean 4** — verificado por máquina, sem `sorry`, sem axiomas extra. |
| 🟡 | **Provado no paper, não formalizado** — argumento analítico válido mas fora do alcance da camada Lean actual (precisa de Mathlib: análise, crivo, séries). |
| 🔵 | **Condicional** — depende de hipótese não provada (GRH, `HR⁻`, quasi-independência). Não é teorema. |
| ⚪ | **Empírico** — resultado de simulação/ajuste numérico. Evidência, não demonstração. |

---

## 1. Mapa por paper

### Paper 01 — Estrutura combinatória (`01_estrutura_combinatoria`)

| Afirmação | Estatuto |
|---|---|
| Definição dos conjuntos estruturais `S_n(p)`, `A_p` e dos pares simétricos | definição |
| Resultados válidos sobre a estrutura (contagens, inclusões) | 🟡 |
| Lacuna central: o union bound ingênuo dá `O(log³ N)` e é pessimista | 🟡 (argumento heurístico) |

### Paper 02 — Saturação geométrica (`02_saturacao_geometrica`)

| Afirmação | Estatuto |
|---|---|
| Proposição principal de saturação da malha `3×N` | 🔵 depende da **hipótese de quasi-independência** |
| Fator de correção / unicidade estrutural | 🔵 |
| Análise assintótica de `K_u` e limiar de estabilidade | 🟡 |

### Paper 03 — Abordagem unificada (`03_abordagem_unificada`)

| Afirmação | Estatuto |
|---|---|
| Elo "trio primo ↦ três pares + um ternário" | ✅ `trio_d1_goldbach`, `trio_d1_ternaria` (Paper 04 §6) |
| Colapso do crivo de Selberg/Chen pelo problema da paridade | 🟡 (argumento qualitativo) |
| Formalização ergódica da grade | 🟡 (ver Paper 08) |
| Peso geométrico `Ω_N(n)` e estimador | ⚪ (verificação computacional) |

### Paper 04 — Propriedade de grade (`04_propriedade_grade`)

**Este é o paper mais formalizado da série — praticamente todo o seu conteúdo
é aritmética elementar e está verificado.**

| Afirmação | Estatuto | Nome em Lean |
|---|---|---|
| Lema da Soma Constante: `D₁ = D₂ = C_v = 3(2N+2i+1)` | ✅ | `lema_soma_constante` |
| Invariante Âncora: `3·f(2,i+1) = S(i)` | ✅ | `corolario_ancora` |
| Complemento `C(n,i) = S(i) − n` é sempre par | ✅ | `complemento_par`, `complemento_de_celula_par` |
| `D₁` é PA de razão `2N+2` | ✅ | `pa_d1`, `pa_d1'` |
| `D₂` é PA de razão `2N−2` | ✅ | `pa_d2`, `pa_d2'` |
| `C_v` é PA de razão `2N` | ✅ | `pa_cv` |
| Diferenças entre linhas consecutivas são `2N` | ✅ | `dif_linhas` |
| Uniformidade modular `f(r,c) ≡ 2c−1 (mod 2N)` | ✅ | `uniformidade_modular` |
| `k` ímpar ⇒ âncora inteira; complemento par | ✅ | `coluna_k3`, `coluna_k5`, `coluna_k3_impar`, `coluna_k5_impar` |
| `k = 2` ⇒ `Σ₂ = 2(N+2j−1)`, complemento ímpar | ✅ | `coluna_k2` |
| `k = 4` ⇒ `Σ₄ = 4(3N+2j−1)`, complemento **ímpar** | ✅ | `coluna_k4`, `coluna_k4_par`, `complemento_k4_impar` (ver **E-1**) |
| Trio primo ⇒ 3 representações binárias distintas | ✅ | `trio_d1_goldbach`, `trio_d1_distintas`, `soma_d1_ab/ac/bc` |
| Trio primo ⇒ representação ternária de `S(i)` | ✅ | `trio_d1_ternaria` |
| "Por que `k=3` é o caso mínimo privilegiado" | 🟡 | argumento qualitativo (contagem de percursos), não é teorema |

### Paper 05 — Invariante âncora e `Ω*_N` (`05_invariante_ancora`)

| Afirmação | Estatuto |
|---|---|
| Série singular `𝔖(C)` como peso aritmético; definição de `Ω*_N` | definição (analítica) |
| `Ω*_N` discrimina primos de semiprimos (KS `p ≈ 3·10⁻⁴⁷` em `N=1800`) | ⚪ |
| Extensões a Legendre, gêmeos, Oppermann, Brocard | 🔵 (conjecturais) |

### Paper 06 — Problema B (`06_prova_problema_b`)

| Afirmação | Estatuto |
|---|---|
| Expansão de Dirichlet de `α(d)`, fórmula de Perron | 🟡 |
| Estimativa Tipo I (`L1`) e Tipo II (Kloosterman–Weil) | 🟡 |
| Desigualdade estrutural `μ_comp > μ_global > μ_primo` | 🟡 (depende das hipóteses de trabalho listadas no próprio paper) |

### Paper 07 — Motor de Herança (`07_motor_de_heranca_estrutural`)

| Afirmação | Estatuto | Nome em Lean |
|---|---|---|
| Soma constante das colunas da fita: `4N − 2ε` | ✅ | `fita_soma` |
| Dois pares por fita (`4N` e `4N−2`) | ✅ | `fita_dois_pares` |
| Diagonais somam o par alvo `4N` | ✅ | `fita_diagonal` |
| `Φ` bem definida sob `3C = 2N`, soma constante `6C = 4N` | ✅ | `phi_soma_externa`, `phi_soma_meio`, `phi_soma_total` |
| Coordenadas de `Φ` injectivas e sobrejectivas | ✅ | `phi_linha1_injetiva`, `phi_linha3_injetiva`, `phi_linha1_sobrejetiva`, `phi_linha3_sobrejetiva` |
| Órbita de `σ` cobre os `N−1` pares diagonais | 🟡 | prova por contagem no paper; exigiria formalizar o *scanner* |
| Unicidade do passo `δ = 1` | 🟡 | argumento de contagem |
| `HR⁺ ⇒ HR⁻` | ✅ | `hr_mais_implica_hr_menos` |
| Teorema do Motor (condicional a `HR⁻`) | ✅ | `teorema_motor` (ver **R-1**) |
| Protocolo de simulação caos→ordem | ⚪ |

### Paper 08 — Formulação ergódica (`08_formulacao_ergotica`)

| Afirmação | Estatuto | Nome em Lean |
|---|---|---|
| Sistema `(X_N, μ_N, T)`, operador de Koopman | definição | — |
| Espectro discreto puro de `U_T` (matriz circulante de permutação) | 🟡 | exige álgebra linear (Mathlib); é elementar mas fora do escopo |
| Função de colisão `F(t) = 1_ℙ(E₁)·1_ℙ(E₂)` | ✅ | `colisao`, `colisao_eq_one_iff` |
| **`HR⁻ ⟺ F̂(0) > 0`** | ✅ | `hrcol_iff_Fhat0_pos` (ver **R-2**) |
| `0 ≤ F̂(0) ≤ 1` | ✅ | `somaColisao_le` |
| Descorrelação espectral via Gowers/nilsequências (Green–Tao–Ziegler) | 🔵 | citação de teorema externo; não formalizado |
| "Colapso" do método do círculo e do crivo de Rosser–Iwaniec | 🟡 | argumento heurístico |

### Paper 09 — Motor, definição definitiva (`09_motor_definicao`)

Repete as definições do Paper 07 com outra apresentação (fita `F(2×N)`, grade
`G(3×C)`, janela `W_i`, scanner, `HR⁻`/`HR⁺`, gabarito). Não acrescenta
teoremas novos. As definições Lean `grade`, `fitaA`, `fitaB` estão alinhadas
com esta versão. O paper é, na prática, duplicação de 07 — candidato a
consolidação.

### Paper 10 — Leis de escala e Âncora Absoluta (`10_leis_de_escala_e_conjectura`)

| Afirmação | Estatuto |
|---|---|
| `k*(N) ≈ 6,3 log N` (convergente para `N ≥ 10⁷`) | ⚪ até `10⁹` |
| `p_max(N) ≈ 11,8 log N log log N` | ⚪ |
| Quase-independência das activações: correlação média `< 0,4 %` | ⚪ |
| Conjectura da Âncora Absoluta | 🔵 |
| Derivação analítica de `A_abs` | 🟡/🔵 |
| Modelo de Poisson da cobertura | 🟡/⚪ |

### Paper 11 — Saturação e gap exponencial (`11_saturacao_gap_exponencial`)

| Afirmação | Estatuto |
|---|---|
| `gap_max(k) ≈ G₀ e^{−βk}`, `β ≈ 0,20` (até `10⁸`) | ⚪ |
| Estabilidade de `β`; correlação entre `C` vizinhos | ⚪ |
| Lema da separação gap / pontos isolados (`O(log log N)` vs `O(log N)`) | 🟡 |
| Passo 2 do argumento analítico (cota inferior `ρ̄(C)` via GRH) | 🔵 GRH |

### Paper 12 — Cobertura condicional (`12_cobertura_condicional`)

| Afirmação | Estatuto |
|---|---|
| Prova condicional sob **GRH**: cobertura total ⇒ `HR⁻` ⇒ Goldbach | 🔵 GRH |
| `n_ef = 36/π² ≈ 3,6476` | 🟡 (produto euleriano excluindo `p=3`) |
| Constante de janelas activas `c = 4·n_ef·C₂·⟨𝔖⟩ ≈ 21` | 🟡 (ajuste; metade do empírico) |
| Dois regimes (âncoras pequenas via Mertens + eliminação mod 8) | 🟡 |

---

## 2. Achados — erratas e riscos lógicos

Itens encontrados ao formalizar. Os de tipo **E** são correcções pontuais; os
de tipo **R** são observações sobre a economia lógica do programa.

### E-1 — Paper 04, Proposição 5.4: complemento de `k=4` é ímpar, não par

O **enunciado** diz *"o complemento `C₄` é sempre par"* e o resumo (linha 43 do
`.tex`) repete-o. Mas:

- a **demonstração** do próprio paper conclui `C₄ = par − ímpar = ímpar`;
- a **tabela resumo** (linha 524) diz `Não (ímpar)`;
- a contagem confirma: `Σ₄ = 4(3N+2j−1)` é par, `n` é ímpar, logo `C₄` é ímpar.

Em Lean: `coluna_k4_par` (a soma é par) e `complemento_k4_impar` (o complemento
é ímpar). A consequência para o programa é real: `𝔖(C)` só está definida para
`C` par, logo **`k = 4` não é admissível** — o que aliás é o que o paper
conclui na Observação seguinte. Recomenda-se corrigir o enunciado e o resumo.

### E-2 — Paper 04, tabela resumo: linha `k` par malformada

A última linha da tabela traz `k[(k−1)/1 N + ⋯]`, que não é uma expressão
válida. A fórmula correcta é `Σ_k(j) = k[(k−1)N + 2j − 1]`, já usada na
Proposição 5.2 para `k` ímpar e válida para todo `k`.

### E-3 — Paper 04, Proposição 4.1: hipóteses implícitas

`r_{D₂} = 2N − 2` exige `N ≥ 1`, e `r_{D₁} = 2N + 2` exige `i ≥ 1`. Trivial no
contexto do paper (`N ≥ 3`), mas os enunciados não fixam as hipóteses; em Lean
aparecem explicitamente (`hN`, `hi`).

### E-4 — Paper 07, Proposição 3.5: "bijeção" provada por contagem

A demonstração conta células (`2C + C = 3C = 2N`) e conclui a boa definição,
mas não mostra injectividade. Em Lean separou-se o que é efectivamente usado:
soma constante (`phi_soma_externa`, `phi_soma_meio`), injectividade de cada
coordenada (`phi_linha1_injetiva`, `phi_linha3_injetiva`) e sobrejectividade
(`phi_linha1_sobrejetiva`, `phi_linha3_sobrejetiva`). Não é um erro — é uma
prova incompleta que a formalização fecha por partes.

### R-1 — `HR⁻` tal como enunciada *é* a Conjectura de Goldbach

A Definição 8.1 do Paper 07 enuncia `HR⁻` como:

> *para toda iteração do motor, existe `t` tal que `e₁(t)` e `e₃(t)` são ambos primos*

Mas as iterações percorrem exactamente os pares `2M₀, 2M₀+2, 2M₀+4, …`. Logo
`HR⁻` ⟺ *todo par `≥ 2M₀` é soma de dois primos*, isto é, Goldbach a partir de
`2M₀`. O Teorema 8.4 (`HR⁻ ⟹ Goldbach`) é, por isso, uma reindexação — não um
avanço.

A formalização expõe isso sem rodeios: em `teorema_motor`, a hipótese `Cadeia`
já contém, elo a elo, a certificação de primalidade; a conclusão é a leitura
da cadeia. Nada de errado com o teorema — mas ele **não reduz** o problema.

O que reduz de facto é o Paper 12, onde a hipótese usada é *local*: uma cota
inferior para a densidade de eventos primos numa janela, `ρ̄(C) ≥ c₀/log²C`.
**Sugestão:** reformular `HR⁻` no Paper 07 como essa afirmação local (ou
declará-la explicitamente como "equivalente a Goldbach"), para que o Teorema do
Motor não pareça mais forte do que é. O Lean pode então enunciar a versão local
como hipótese nomeada e a cadeia como teorema — o que já está feito em
`Motor.lean` com `HRmenos`/`Cadeia`.

### R-2 — Paper 08, Teorema 6.4: equivalência sem conteúdo aritmético

`HR⁻ ⟺ F(t₀) ≠ 0 ⟺ ΣF ≥ 1 ⟺ F̂(0) > 0` é uma tautologia sobre uma função
indicadora. O próprio paper o reconhece (Observação 6.5: *"é uma equivalência,
não uma prova... o ganho não é lógico, mas linguístico"*).

A formalização confirma-o de forma exacta: `hrcol_iff_Fhat0_pos` **não usa
nenhuma propriedade dos primos** além da definição do indicador. Isso não
invalida o programa — a mudança de linguagem é o ponto — mas convém que o
abstract não sugira que o Teorema 6.4 aproxima a prova. A formulação honesta é:
*"reduzimos `HR⁻` a uma questão de positividade espectral, para a qual existem
ferramentas"*.

### R-1 (continuação) — anatomia do colapso, e o que fazer com ele

A leitura do autor é correcta: `HR⁻` deveria falar de pares **base** e `HR⁺` de
um par **logo à frente**, ligados pelo deslocamento da fita — não de "um par de
primos qualquer". A formalização mostra exactamente onde essa intenção se
perde, e o que a recupera.

#### (a) O teorema que explica o colapso

A fita `F_N^1` tem pares diagonais `(2k+1, 4N−2k−1)` para `k = 1..N−1`. Quando
`k` percorre esse intervalo, a primeira coordenada percorre **todos** os ímpares
de `3` a `2N−1`:

```lean
theorem parDiagonal_sobrejetiva (N x : Nat) (hx : Impar x) (h3 : 3 ≤ x)
    (hxN : x ≤ 2 * N - 1) :
    ∃ k, 1 ≤ k ∧ k ≤ N - 1 ∧ (parDiagonal N k).1 = x
```

Ou seja: a fita **enumera todos os pares** de ímpares que somam `4N` (falta
apenas o par trivial `(1, 4N−1)`). «O par está na fita», «o par está na mesma
coluna», «é um par diagonal» — nenhuma destas condições exclui um único par.
É por isso que `HR⁻` colapsa: a hipótese não tem conteúdo de restrição.

#### (b) O trade-off inevitável

| Hipótese | Conteúdo | Dificuldade |
|---|---|---|
| "existe par de primos somando `n`" (fita actual) | **nada** além de Goldbach | igual a Goldbach |
| "existe par **atingível por transporte** a partir do par base" | cadeia coerente | **mais forte** que Goldbach |
| "existe janela `(C,i)` com um eixo certificado" | 3 pares prescritos | **mais forte** que Goldbach |

Não há escapatória: restringir a hipótese torna-a **mais forte**, logo mais
difícil de provar, não mais fácil. O ganho possível não é lógico — é
*estrutural*: uma hipótese prescrita pode ser atacada por crivo/APs, uma
hipótese arbitrária não.

#### (c) Tentativa 1 — cadeia inversa: por que não fecha

O passo de herança é `(p,q) ↦ (p+2, q)` ou `(p, q+2)`, e acrescenta `2` à soma:

```lean
theorem passo_soma {a b : Nat × Nat} (h : Passo a b) : b.1 + b.2 = a.1 + a.2 + 2
```

A certificação do elo seguinte é **exactamente** `p+2` primo:

```lean
theorem transporte_certificado (p q : Nat) :
    (Primo ((p + 2, q) : Nat × Nat).1 ↔ Primo (p + 2)) ∧ ...
```

O passo inverso exigiria `p−2` primo. Ora `p ↦ p−2` **não preserva
primalidade**: `9` é composto. Concretamente, partindo do par `(5,7)` para `12`:

- `12 = 5+7` → transporte para `14`: `(7,7)` ✓ certifica;
- `14 = 7+7` → transporte para `16`: `(9,7)` e `(7,9)` — `9` é composto, ambos falham;
- e no entanto `16 = 3+13`.

A cadeia pura morre em `16`; Goldbach sobrevive por um par **não relacionado**.
Nenhuma indução puramente combinatória pode evitar isto: as únicas relações
disponíveis são `±2` por coordenada, e elas não preservam primos. Uma descida
`n+2 → n` teria de mostrar que *alguma* representação sobrevive — o que é
precisamente uma afirmação de contagem (Hardy–Littlewood), não de álgebra.

O que **é** formalizável é a cadeia com a hipótese explícita:

```lean
theorem cadeia_certificada (f : Nat → Nat × Nat)
    (hpasso : ∀ j, Passo (f j) (f (j + 1)))
    (hcert : ∀ j, Primo (f j).1 ∧ Primo (f j).2) :
    ∀ j, TemRepGoldbach ((f 0).1 + (f 0).2 + 2 * j)
```

Note a diferença face a `teorema_motor`: aqui a hipótese é uma **cadeia
relacionada**, não uma escolha livre de par por par. Mais restritiva — e é
essa restrição que a torna não-tautológica.

#### (d) Tentativa 2 — janelas 3×3: o que ela fixa de facto

Esta é a via correcta, e é formalizável por inteiro. Os extremos de qualquer
dos três eixos de `W_i` somam `2·f(2,i+1)`, o dobro da âncora:

```lean
theorem eixo_extremos_soma (N i : Nat) (hi : 1 ≤ i) :
    grade N 0 (i - 1) + grade N 2 (i + 1) = 2 * grade N 1 i ∧   -- D₁
    grade N 2 (i - 1) + grade N 0 (i + 1) = 2 * grade N 1 i ∧   -- D₂
    grade N 0 i + grade N 2 i = 2 * grade N 1 i                 -- C_v
```

Dois primos num eixo certificam Goldbach para `2·âncora`:

```lean
theorem eixo_goldbach (N i : Nat) (hi : 1 ≤ i)
    (hp : Primo (grade N 0 (i - 1))) (hq : Primo (grade N 2 (i + 1))) :
    TemRepGoldbach (2 * grade N 1 i)
```

Ao contrário da fita, aqui a janela **não** deixa escolher o par: prescreve
três pares concretos por valor de `(C,i)`. É exactamente o "evento restritivo"
que faltava. Mas há dois limites duros:

**Limite 1 — só metade dos pares.** A âncora é ímpar, logo `2·âncora ≡ 2 (mod 4)`:

```lean
theorem alvo_mod_quatro (N i : Nat) : (2 * grade N 1 i) % 4 = 2
```

Os pares `≡ 0 (mod 4)` — que são precisamente os que a fita fornece, com soma
`4N` — **nunca** são certificados por uma janela. O motor precisa dos dois
objectos, e a razão não é estética: são resíduos diferentes.

**Limite 2 — as janelas falham com frequência.** Para `3 ≤ N ≤ 39`, contando
todas as janelas `1 ≤ i ≤ N−2` (703 no total), **285 (40,5 %)** não têm nenhum
dos três eixos certificado. Exemplo mínimo: `N=3, i=6` dá âncora `19`, alvo
`38`, eixos `(11,27), (23,15), (13,25)` — todos falham; e no entanto
`38 = 19+19`. O evento restritivo não é raro só por acidente: ele falha sempre
que os três extremos pequenos (`2i−1`, `2i+3`, `2i+1` em função de `N`) caem em
compostos.

**Limite 3 — `W_i` tem duas leituras incompatíveis.** Como submatriz da grade,
a janela soma `2·âncora`; como recipiente do scanner (pares `Φ`), soma `6C`.
As duas coincidem numa única janela por grade:

```lean
theorem leitura_dupla (C i : Nat) : 2 * grade C 1 i = 6 * C ↔ C = 2 * i + 1
```

O Paper 07 usa as duas leituras indistintamente (Definição 4.1 diz "soma
`2M⁺` garantida pela Prop. 2.3"), mas elas dão valores diferentes excepto em
`C = 2i+1`. Vale separar explicitamente: **`W_i`-submatriz** (eixos, âncora) e
**`W_i`-buffer** (slots preenchidos por `Φ`).

#### (e) `HR⁻` reformulada — proposta

```text
HR⁻_loc(C, i) : a janela W_i tem um eixo com os dois extremos primos
                (equivale a: 2·f(2,i+1) é soma de dois primos, com o par
                 prescrito pelos extremos).

HR⁻_global(N₀) : ∀ n ≡ 2 (mod 4), n ≥ N₀, ∃ (C, i) tal que 2·f(2,i+1) = n
                  e HR⁻_loc(C, i).
```

`HR⁻_loc` é decidível numa janela (três testes de primalidade) e `HR⁻_global`
é uma afirmação sobre primos em progressões prescritas — atacável por
Mertens/GRH, que é exactamente o que o Paper 12 faz. O motor passa a ser um
**teorema de transporte de certificados**, não de existência:

```text
se HR⁻_loc(C,i) e o alvo seguinte é 2·f(2,i+1)+2, então (a) certificar esse
alvo exige mudar de janela (Limite 1), e (b) a densidade de janelas
certificadas controla quantas mudanças são precisas.
```

É esta a versão que vale a pena provar — e é uma afirmação **mais forte** que
Goldbach, como tem de ser. O preço de abandonar a tautologia é assumir uma
hipótese mais exigente; o benefício é que ela é local e verificável.

#### (f) Consequência editorial

1. Paper 07: renomear `HR⁻` para o que ela é (Goldbach ponto a ponto) e
   apresentar `cadeia_certificada` como o motor genuíno, com o `Passo`
   explícito.
2. Paper 12: é o único sítio onde a versão local já está, de facto, a ser
   usada — vale promover essa formulação a definição principal.
3. Paper 07 §§4–5: separar `W_i`-submatriz de `W_i`-buffer, e assinalar o
   limite `mod 4` (a certificação por âncora cobre só `n ≡ 2 (mod 4)`).

#### (g) O que a geometria restringe de facto — o alcance das janelas

Pergunta decisiva: **qual** conjunto de pares a grade consegue produzir? A
resposta é exacta e está formalizada (`Projecao.lean`).

Uma janela `(C,i)` tem alvo `n = 2·âncora = 4C+4i+2`. Os três eixos dão pares
`(x, n−x)` com `x ∈ {2i−1, 2i+1, 2i+3}`. O eixo `D₂` é o mais generoso, e o
limite é `4x ≤ n+6`:

```lean
theorem janela_limite (C i : Nat) (hiC : i + 1 ≤ C) :
    4 * grade C 0 (i + 1) ≤ 2 * grade C 1 i + 6

theorem janela_alcanca (s j : Nat) (hj : 1 ≤ j) (hjs : 2 * j + 1 ≤ s) :
    1 ≤ j ∧ j + 1 ≤ s - j ∧
    2 * grade (s - j) 1 j = 4 * s + 2 ∧ grade (s - j) 0 (j + 1) = 2 * j + 3
```

Juntas: **as janelas alcançam exactamente os pares cujo membro menor é
`≤ n/4 + 3/2`**, e nenhum outro. Isto é uma restrição real — mas de **factor 2**
(metade das representações, as que têm o primo pequeno). Um factor 2 não altera
a classe de dificuldade: é por isso que a versão «janela» de `HR⁻` continua a
parecer Goldbach.

Empiricamente, a versão «janela» de `HR⁻` verifica-se para **todos** os
`n ≡ 2 (mod 4)` de `14` a `40000` (só `6` e `10` falham, por nem terem janela).
Isso confirma a intuição do autor: `HR⁻` ocorre sempre; é `HR⁺` que não.

#### (h) `HR⁺` falha, `HR⁻` não — o exemplo 18

`HR⁺` exige a tripla inteira prima, logo exige a âncora prima. Para `n = 18` há
uma única janela, de âncora `9`:

```lean
theorem ancora_18 (C i : Nat) (h : 2 * grade C 1 i = 18) : grade C 1 i = 9

theorem hrmais_falha_18 (C i : Nat) (h : 2 * grade C 1 i = 18) :
    ¬ Primo (grade C 1 i)
```

E no entanto `HR⁻` verifica-se: `5 + 13 = 18` (eixo `D₂` da mesma janela).
A assimetria é estrutural, não acidental: `HR⁺` ⟹ âncora prima, e as âncoras
percorrem todos os ímpares.

#### (i) Onde pode estar a restrição qualitativa: consistência ⇒ resíduo

A ideia do autor — usar `W_i` **e** a sua projecção na fita — tem um conteúdo
preciso, e é o único candidato a restrição *qualitativa* que a formalização
encontrou.

A janela contém um par completo de `Φ` (i.e. as duas descrições coincidem)
exactamente quando `C = 2i+1` (`leitura_dupla`). Nesse caso o alvo cai numa
classe de resíduo:

```lean
theorem central_mod_doze (i : Nat) : (2 * grade (2 * i + 1) 1 i) % 12 = 6
```

Ou seja: **exigir consistência geométrica entre as duas descrições força
`n ≡ 6 (mod 12)`** — um sexto dos inteiros, um terço dos pares. O preço da
consistência é cobertura.

Este é, na minha leitura, o «Que?» que o autor sente: a geometria não restringe
*quais primos*, mas **quais classes de resíduo** podem ser certificadas por cada
construção. Programa concreto que daqui sai:

1. enumerar as condições de consistência entre `W_i` e a fita (par completo,
   eixo alinhado, `Φ` fixo, …);
2. cada uma força uma classe de resíduo `n ≡ r (mod m)`;
3. se um número finito delas cobrir todos os pares, obtém-se uma estratégia
   estrutural cuja hipótese é *densidade de primos em progressões prescritas* —
   exactamente o tipo de afirmação que Mertens/GRH atacam (Paper 12).

O passo que falta não é geométrico: é mostrar que a união das classes cobre, e
com densidade suficiente. Aí a dificuldade volta a ser analítica — o que é
consistente com a suspeita do autor de que «pode ser da mesma dificuldade do
enunciado clássico».

#### (j) A cadeia tem comprimento ≤ 2 — o passo `±2` é demasiado fraco

Este é, na minha leitura, o resultado mais decisivo sobre o mecanismo de
herança, e é independente de Goldbach.

Três ímpares consecutivos de passo 2 nunca são todos primos — um deles é
múltiplo de 3:

```lean
theorem tres_consecutivos_multiplo (p : Nat) : 3 ∣ p ∨ 3 ∣ (p + 2) ∨ 3 ∣ (p + 4)

theorem nao_tres_primos (p : Nat) (hp3 : 3 < p)
    (h1 : Primo p) (h2 : Primo (p + 2)) (h3 : Primo (p + 4)) : False

theorem cadeia_limite (p q : Nat) (hp3 : 3 < p) (hq3 : 3 < q) (hp : Primo p) (hq : Primo q) :
    (¬ (Primo (p + 2) ∧ Primo (p + 4))) ∧ (¬ (Primo (q + 2) ∧ Primo (q + 4)))
```

Consequência: **cada coordenada pode avançar no máximo uma vez**. Como um
passo desloca uma única coordenada em `+2`, uma cadeia certificada tem
comprimento no máximo 2 — e 3 apenas no caso degenerado em que uma das
coordenadas começa em `3` (a corrida `3, 5, 7`, que morre em `9`).

Confirmação computacional (crivo até `10⁶`, `.setup/comprimento_cadeia.py`):
dos primos abaixo de `10⁶`, **70328 têm corrida 1**, **8168 têm corrida 2** e
**exactamente um tem corrida 3** (o `3`). O comprimento máximo de cadeia
observado para `6 ≤ n ≤ 20000` é `3` (e `4` apenas em `n = 6`, com o par
`(3,3)`).

**Veredicto.** O «motor» não transporta: ele avança um ou dois passos e tem de
recomeçar. Chamar-lhe herança é generoso — é *cobertura*. E uma cobertura é,
por definição, Goldbach ponto a ponto. Isto é mais forte do que R-1: não é que
a hipótese seja tautológica, é que o mecanismo **não pode iterar**. Qualquer
tentativa de prova por cadeia (incluindo a cadeia inversa) está condenada por
aritmética elementar, `3 | (p · (p+2) · (p+4))`.

**O que sobrevive.** Restam duas saídas, e ambas mudam de natureza:

1. **Cobertura com classes prescritas** — o programa de (i): a geometria
   prescreve progressões aritméticas, e a hipótese vira densidade de primos em
   PAs (Mertens/GRH, Paper 12). Não é uma herança; é um crivo geométrico.
2. **Uma relação de passo diferente.** O passo `±2` vem da translação na fita.
   O acoplamento `Φ` dá uma relação **não-local** (linha 1 ↔ linha 3 invertida,
   linha 2 dobrada ao meio). Se existir um passo induzido por `Φ` — em vez da
   translação — que ligue pares de somas consecutivas, ele não sofre a
   obstrução do `3`. É a única via que vejo para recuperar uma herança
   genuinamente iterável, e não a testei.

#### (k) `Φ` é a reflexão — a via não-translacional fecha

O experimento que faltava: existe um passo induzido pelo acoplamento `Φ`, em
vez da translação, que escape à obstrução do `3`? **Não.** `Φ` não tem
estrutura própria — cada par de `Φ` é `{x, 6C − x}`:

```lean
theorem phi_complemento (C k : Nat) (hk : 1 ≤ k) (hkC : k ≤ C) :
    phiLinha3 C k = 6 * C - phiLinha1 C k

theorem phi_meio_complemento (C k : Nat) (hk : C + 1 ≤ k) (hk2 : k ≤ 3 * C / 2) :
    phiMeioDir C k = 6 * C - phiMeioEsq C k

theorem acoplamento_e_reflexao (C : Nat) : …
```

E a fita é a mesma reflexão:

```lean
theorem fita_complemento (N k : Nat) : fitaB N k 0 = 4 * N - fitaA k
```

Verificado numericamente para `3 ≤ C ≤ 18` (`.setup/experimento_phi.py`): `Φ` é
involução, todo par soma `6C`, e `b_k = 4N − a_k` no modo normal.

Duas consequências:

1. **Não há passo de `Φ` que preserve incremento de soma.** Um passo
   `(x,y) ↦ (Φ(x), y)` altera a soma por `6C − 2x`, que percorre
   `±2, ±6, ±10, …` (todos `≡ 2 mod 4`) — nenhum `+2`. `Φ` não gera dinâmica
   ao longo dos pares consecutivos.
2. **`Φ` é, ainda assim, a ponte entre as duas classes de resíduo.** Como as
   variações são `≡ 2 (mod 4)`, `Φ` liga `n ≡ 0` a `n ≡ 2 (mod 4)` — que é
   precisamente a razão pela qual a série precisa dos dois objectos: a fita
   (soma `4N ≡ 0`) e a janela (soma `2·âncora ≡ 2`). Isso não estava explícito
   nos papers e é a única função estrutural genuína de `Φ`.

Também o «desmanche» diagonal → coluna, que parecia ser a herança correcta, é
o mesmo passo `±2`:

```text
diagonal k = (a_{k+1}, b_k)      soma 4N
coluna k+1 = (a_{k+1}, b_{k+1})  soma 4N-2      delta = -2
```

Logo herda o limite de (j): a cadeia morre em dois passos.

### Veredicto — o que era círculo e o que não era

Vale a pena separar três camadas, porque a resposta a «foi só rodar em círculo?»
é: **a estratégia de prova, sim; o trabalho todo, não.**

**Círculo (provado como tal, três vezes independentes).** A pretensão de que o
«motor» *deriva* Goldbach de uma hipótese mais fraca. Cai por três vias:
R‑1 (a fita enumera todos os pares), R‑2 (a equivalência espectral é
tautológica) e R‑3 (a cadeia não itera, por `3 | p(p+2)(p+4)`).

**Não é círculo (machine-checked).** As identidades algébricas da série:
soma constante, invariante âncora, paridade do complemento, razões das PAs,
uniformidade modular, generalização `k×N`, teorema do trio, alcance exacto das
janelas (`x ≤ n/4 + 3/2`), limite da cadeia, e agora `Φ` = reflexão. Nada disso
depende de Goldbach, e três destes resultados são no-go's que impedem retomar
caminhos mortos.

**Sobrevive como matemática de verdade.** Uma única afirmação, e não é trivial:
*existem representações de Goldbach com o primo pequeno controlado*. A
geometria não a prova — apenas a **prescreve** (as PAs de (i)). Empiricamente,
o Paper 10 mede `p_max(N) ≈ 11,8 log N log log N`; analiticamente, sob GRH há
resultados clássicos desse tipo para o menor primo numa partição de Goldbach
(`≪ log^{2+ε}`), que é exactamente o que o Paper 12 usa. Ou seja: a «Conjectura
da Âncora Absoluta» é, com toda a probabilidade, uma releitura geométrica de um
teorema condicional conhecido — e essa é a sua posição honesta.

**Por que tinha de ser círculo.** A razão é estrutural e agora está formalizada:
toda a construção é composta por reflexões (`x ↦ 6C − x`, `x ↦ 4N − x`) e
translações (`±2`). Reflexões e translações preservam somas; nenhuma delas vê
primalidade. Uma construção geométrica só pode, portanto, **prescrever** quais
pares testar. O trabalho de garantir que a prescrição acerta é aritmético por
necessidade, não por limitação da abordagem.

### E-5 — Paper 10/11: o domínio das leis de escala é `n ≡ 0 (mod 12)`

*(Correção de uma versão anterior desta nota, que afirmava que a lei estava
errada. Estava a comparar domínios diferentes — ver o fim desta secção.)*

O script `bandeira_ancora_absoluta_extendida.py` marca um valor de `C` quando
existe primo `q` com `p+q ≡ 0 (mod 6)` e `C = (p+q)/6` **par**. Logo os alvos
efetivamente cobertos são

```text
n = 6C ≡ 0 (mod 12),    24 ≤ n ≤ 6N
```

isto é **um sexto dos números pares**. As leis `k* ~ 6,3 log N` e
`p_max ~ 11,8 log N loglog N` descrevem corretamente essa classe — mas os
papers as enunciam como se cobrissem «todos os pares». Essa é a imprecisão.

**Reprodução independente** (medição direta de `g(n) = min{p : p e n−p primos}`
restrita a `n ≡ 0 (mod 12)`, `n ≤ 6N`):

| N | `p_max` (Paper 10) | `max g(n)` medido | `A` efetivo |
|---|---|---|---|
| `10⁶` | 269 | 263 | 7,25 |
| `10⁷` | 449 | 439 | 9,80 |

Bate — a diferença de um passo de âncora vem do critério de paragem (gap ≤ 2).

**Fora do domínio a lei não vale.** Para `n = 60 119 912 ≡ 8 (mod 12)`:

```text
g(n) = 1093            vs            11,8 · log(n/2) · loglog(n/2) ≈ 578
```

fator 1,89 acima. Como `n ∉ 0 (mod 12)`, não contradiz os dados — mas mostra que
`A = 11,8` não se transporta para todos os pares.

**Consequência.** A Conjectura da Âncora Absoluta, **para todo par**, exige a
ordem `log²n · loglog n`, não `log n · loglog n`:

| N | `max g(n)` (todos os pares) | `M/(logN·loglogN)` | `M/(log²N·loglogN)` |
|---|---|---|---|
| `10⁵` | 293 | 10,4 | 0,90 |
| `10⁶` | 523 | 14,4 | 1,04 |
| `10⁷` | 751 | 16,8 | 1,04 |
| `10⁸` | 1093 | **20,4** | 1,11 |

A razão `M/(log N·loglog N)` cresce 2× em quatro décadas e não converge;
`M/(log²N·loglogN)` fica em ≈ 1. A ordem `log²` é também a que a heurística de
Hardy–Littlewood (union bound sobre os `N` valores) prevê, e é compatível com a
cota condicional a GRH `log^{2+ε}`.

**Ajustes feitos.** Paper 10 ganhou a Subsecção 3.5 «Nota de escopo: domínio de
validade e verificação independente», com a reprodução, o contraexemplo e a
**Conjectura C′** restrita a `0 (mod 12)`; o abstract do Paper 12 remete para
ela; `PROGRESS.md` assinala o escopo. Script reproduzível:
`scripts/lei_ancora_verificacao.py N_MAX`.

### L-1 — A lacuna central permanece

`ŵ(0) > 0` incondicional, ou equivalentemente `HR⁻` incondicional, ou
Goldbach — nenhuma destas aparece como teorema em lado nenhum, e o Lean não as
assume. É a única lacuna que importa; as outras (mistura, correlação residual,
extensão a `10^{10}`) são de refino.

---

## 3. O que o Lean garante — e o que não garante

**Garante.** Que as definições são consistentes entre si; que o Lema da Soma
Constante, o Invariante Âncora, a paridade do complemento, as razões das PAs, a
uniformidade modular, a generalização `k×N`, a soma constante da fita e do
acoplamento, o teorema do trio e a equivalência espectral são **verdadeiros
como enunciados** e **demonstrados sem buracos**.

**Não garante.** Que os resultados analíticos (Papers 05, 06, 10–12) estejam
correctos; que `HR⁻` seja verdadeira; que as leis de escala se mantenham além
de `10⁹`; que a interpretação geométrica seja a "certa". O Lean verifica
implicações, não relevância.

## 4. Convenção de nomes para uso futuro

Ao escrever novos papers, usar os nomes Lean como referência canónica:

| Conceito | Nome Lean |
|---|---|
| `f(r,c)` da grade | `Goldbach.grade` |
| `S(i)` | `Goldbach.somaJanela` |
| `C(n,i)` | `Goldbach.complemento` |
| `a_k`, `b_k` da fita | `Goldbach.fitaA`, `Goldbach.fitaB` |
| `Φ` (duas metades) | `Goldbach.phiLinha1`, `phiLinha3`, `phiMeioEsq`, `phiMeioDir` |
| `HR⁻`, `HR⁺` | `Goldbach.HRmenos`, `Goldbach.HRmais` |
| função de colisão | `Goldbach.colisao` |
| `F̂(0)` | `Goldbach.Fhat0` |
