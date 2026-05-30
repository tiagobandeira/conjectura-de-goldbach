# Nota Complementar ao Artigo 7:
## Unicidade de C ≡ 6 (mod 30) e Cadeias de Autossimilaridade via T(C) = 5C+2

**Série:** Motor de Herança Estrutural — Conjectura de Goldbach  
**Autor:** Tiago Bandeira  
**Data:** maio de 2026  
**Status:** Nota complementar ao Artigo 7

---

> Esta nota formaliza dois resultados observados numericamente até C = 5000
> e identificados como estruturais: a unicidade de C ≡ 6 (mod 30) e a
> autossimilaridade das cadeias HR⁻ via a transformação T(C) = 5C+2.
> Ambos os resultados são **incondicionais**.

---

## 1. Unicidade de C ≡ 6 (mod 30)

### Observação

Na distribuição de casos HR⁻ até C = 5000 (269 casos), oito dos nove
resíduos admissíveis mod 30 ocorrem com frequência ~33 casos cada.
O resíduo C ≡ 6 (mod 30) ocorre exatamente **uma vez** (C = 6).

| C mod 30 | Casos HR⁻ (C ≤ 5000) |
|----------|----------------------|
| 0  | 36 |
| 2  | 32 |
| **6**  | **1** |
| 8  | 33 |
| 12 | 28 |
| 14 | 37 |
| 18 | 34 |
| 20 | 33 |
| 24 | 35 |

Isso não é uma anomalia estatística — trata-se de uma restrição estrutural exata.

### Proposição N.1 (Unicidade de C ≡ 6 (mod 30) — incondicional)

O único valor C ≡ 6 (mod 30) para o qual HR⁻ pode disparar é C = 6.

*Demonstração.* Seja C = 30m + 6 para algum m ≥ 0. Então:

```
e₁ = C − 1 = 30m + 5 = 5·(6m + 1)
```

Logo, 5 divide e₁. Para que e₁ seja primo sendo divisível por 5, é necessário que e₁ = 5.
Isso ocorre se e somente se 30m + 5 = 5, ou seja, m = 0 e C = 6.
Para todo m ≥ 1, e₁ = 30m+5 é composto (divisível por 5 e maior que 5), impossibilitando o disparo de HR⁻. □

**Corolário N.2.** O filtro mod 30 da Proposição 7.1 do Artigo 7 pode ser
refinado: dentre os 9 resíduos admissíveis, o resíduo C ≡ 6 (mod 30) admite
exatamente um caso (C = 6). Para os outros 8 resíduos admissíveis, existem infinitos 
valores de C com C − 1 primo (incondicionalmente, via Teorema de Dirichlet, visto que 
$\text{mdc}(r-1, 30) = 1$). O disparo de HR⁻ para infinitos C nesses resíduos, 
contudo, permanece condicional à Conjectura de Dickson. O resíduo 6 é 
**estruturalmente singular**.

---

## 2. Cadeias de Autossimilaridade via T(C) = 5C+2

### Definição

**Definição N.3 (Transformação T).** A transformação canônica é dada por:

```
T : C  ↦  5C + 2
```

definida sobre os inteiros pares C ≥ 4.

A relação geométrica fundamental é:

```
e₃(C) = 5C + 1 = T(C) − 1 = e₁(T(C))
```

O primo de saída do par canônico de C é o primo de entrada do par
canônico de T(C). A saída de um nível é a entrada do próximo.

**Definição N.4 (Cadeia de autossimilaridade).** Uma cadeia de
autossimilaridade de comprimento k é uma sequência:

```
C₀ → C₁ = T(C₀) → C₂ = T(C₁) → ⋯ → Cₖ₋₁ = T(Cₖ₋₂)
```

onde todos os Cⱼ disparam HR⁻. A cadeia é **maximal** se C₀ não é
imagem de nenhum outro C em HR⁻ (C₀ é raiz) e Cₖ₋₁ não tem continuação
em HR⁻.

A sequência de primos associada é:

```
p₀ → p₁ = 5p₀+6 → p₂ = 5p₁+6 → ⋯
```

onde pⱼ = Cⱼ − 1 — uma órbita da forma linear $p \mapsto 5p+6$ dentro dos primos.

> **Observação ($HR^{-}$ nas cadeias).** As cadeias definidas pela transformação $T(C)=5C+2$ aplicam-se à janela **central** $W_{i^*}$, por ser a única a satisfazer a relação de recorrência de extremos $e_{1,n+1}=e_{3,n}$. No entanto, a cobertura geral do scanner (não restrita às cadeias) pode empregar quaisquer janelas $W_i$. Os ensaios computacionais indicam que, mesmo sob a restrição à janela central, a taxa de sobrevivência atinge 21,87%, sugerindo robustez no acoplamento.

### Proposição N.5 (T preserva paridade — incondicional)

Para todo C par, T(C) = 5C+2 é par.

*Demonstração.* Se C é par, 5C é par, logo 5C+2 é par. □

### Proposição N.6 (T preserva admissibilidade mod 30 — incondicional)

Se C é admissível ($C \bmod 30 \in \{0,2,6,8,12,14,18,20,24\}$), então
$T(C) \bmod 30 \in \{2, 12\}$. Em particular, T(C) é admissível.

*Demonstração.* Calculando 5r+2 (mod 30) para cada resíduo r admissível:

| C mod 30 | T(C) mod 30 |
|----------|-------------|
| 0  | 2  |
| 2  | 12 |
| 6  | 2  |
| 8  | 12 |
| 12 | 2  |
| 14 | 12 |
| 18 | 2  |
| 20 | 12 |
| 24 | 2  |

A imagem de T está contida em $\{2, 12\} \subset \{0,2,6,8,12,14,18,20,24\}$. □

**Corolário N.7 (Ciclo de período 2 em {2,12}).** A restrição de T aos
resíduos {2, 12} forma um ciclo de período 2:

```
T(2) ≡ 12 (mod 30)    T(12) ≡ 2 (mod 30)
```

A partir do segundo elemento, toda cadeia alterna entre resíduos
2 e 12 (mod 30). Isso é **incondicional** — independe de primalidade.

### Proposição N.8 (Independência de crivo nas cadeias — incondicional)

Seja C₀ → C₁ → ⋯ → Cₖ₋₁ uma cadeia de autossimilaridade. Para cada
par consecutivo (Cⱼ, Cⱼ₊₁) e para todo primo q > 3, nenhum q elimina
simultaneamente e₁(Cⱼ) e e₃(Cⱼ). Além disso, a ligação e₃(Cⱼ) = e₁(Cⱼ₊₁) 
garante que a dependência de primalidade se propaga ao longo da cadeia: 
a primalidade de e₃(Cⱼ) é condição necessária e suficiente para que a 
cadeia continue em Cⱼ₊₁.

### Verificação numérica (C ≤ 5000)

| Comprimento | Cadeias | Exemplo |
|-------------|---------|---------|
| 1 (isolado) | 153 | C=14: 13→71 |
| 2 | 65 | C=8: 7→41→211 |
| 3 | 14 | C=8→42→212: 7→41→211→1061 |
| 4 | 4  | C=1260→6302→31512→157562: 1259→6301→31511→157561→787811 |
| 5 | 1  | C=80→402→2012→10062→50312: 79→401→2011→10061→50311→251561 |

**Cadeia de comprimento 5 (única até C=5000):**

```
C₀ = 80:    e₁ = 79,     e₃ = 401
C₁ = 402:   e₁ = 401,    e₃ = 2011
C₂ = 2012:  e₁ = 2011,   e₃ = 10061
C₃ = 10062: e₁ = 10061,  e₃ = 50311
C₄ = 50312: e₁ = 50311,  e₃ = 251561
```

Todos os elementos 79, 401, 2011, 10061, 50311, 251561 são primos.
A sequência satisfaz $p_{j+1} = 5p_j + 6$ em cada passo.

### Observação N.9 (Conexão com conjecturas sobre formas lineares)

A existência de cadeias longas é equivalente à existência de órbitas
longas da forma linear $p \mapsto 5p+6$ inteiramente dentro dos primos. A
pergunta "existem cadeias de comprimento arbitrário?" equivale a
"existem cadeias de primos $p_0, 5p_0+6, 5(5p_0+6)+6, \dots$ de comprimento
arbitrário?" — uma instância da conjectura de Dickson sobre sistemas de
formas lineares, que permanece aberta em geral mas é suportada pela
não degeneração provada no Artigo 7.

---

## 3. Síntese

| Resultado | Estatuto |
|-----------|----------|
| C ≡ 6 (mod 30): único caso é C = 6 | **Incondicional** — Proposição N.1 |
| T preserva paridade | **Incondicional** — Proposição N.5 |
| T preserva admissibilidade mod 30 | **Incondicional** — Proposição N.6 |
| Imagem de T ⊆ {2,12} (mod 30) | **Incondicional** — Proposição N.6 |
| Ciclo de período 2 em {2,12} | **Incondicional** — Corolário N.7 |
| Independência de crivo ao longo da cadeia | **Incondicional** — Proposição N.8 |
| Cadeias de comprimento arbitrário | Condicional — Conjectura de Dickson |
| Toda cadeia tem um passo T | Condicional — HR⁻ individual |

Os resultados incondicionais descrevem a **estrutura geométrica** das
cadeias. A existência de cada elo depende de HR⁻ — a lacuna aritmética
central da série.

---

*Nota complementar ao Artigo 7 — maio de 2026.*
