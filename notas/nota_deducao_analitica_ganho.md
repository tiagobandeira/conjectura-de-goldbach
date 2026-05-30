# Nota Técnica: Dedução Analítica da Série Singular de Hardy-Littlewood para o Par Canônico $(p, 5p+6)$

**Série:** Motor de Herança Estrutural — Conjectura de Goldbach — Nota de Fundamentação Analítica  
**Autor:** Tiago Bandeira  
**Data:** Maio de 2026 (versão corrigida)  
**Status:** Nota Heurística – Fundamentação para o Artigo 8

---

> **Resumo.** Esta nota apresenta a dedução da série singular de Hardy‑Littlewood aplicável ao par de formas lineares $(p, 5p+6)$, que rege a transição de escala do Motor de Herança Estrutural via $T(C)=5C+2$. Obtém-se $\mathfrak{S} = \frac{16}{3}C_2 \approx 3,52$. Este valor é a **predição heurística** (sob a conjectura de Hardy‑Littlewood) para o fator de amplificação da densidade de primos. Os dados experimentais até $10^8$ são compatíveis com essa predição, servindo como verificação numérica da heurística.

---

## 1. Contexto e Formulation das Formas Lineares

O acoplamento geométrico induzido pela janela canônica $W_{i^*}$ projeta o par de candidatos de Goldbach $(e_1, e_3) = (C-1, 5C+1)$. Sob a substituição $p = C-1$ (primo ímpar), a transição para a escala superior exige a primalidade simultânea de:

$$L_1(p) = p,\qquad L_2(p) = 5p+6.$$

Este é um sistema de duas formas lineares em uma variável ($d=1$). Para estimar a densidade assintótica de $p \le x$ tais que ambos são primos, aplicamos a **heurística de Bateman‑Horn** (generalização da conjectura de Hardy‑Littlewood).

---

## 2. A Série Singular de Hardy-Littlewood

A contagem assintótica esperada é:

$$\pi_{L_1,L_2}(x) \sim \mathfrak{S}(L_1,L_2) \int_2^x \frac{dt}{\log^2 t},$$

$$\mathfrak{S}(L_1,L_2) = \prod_{q} \frac{1 - \frac{\nu(q)}{q}}{\left(1 - \frac{1}{q}\right)^2},$$

onde $\nu(q)$ é o número de soluções de $p(5p+6) \equiv 0 \pmod q$.

---

## 3. Avaliação dos Fatores Locais $\nu(q)$

### 3.1 $q = 2$ (restringindo a primos ímpares)
Para $p$ ímpar, $p(5p+6) \equiv 1\cdot(5+0)\equiv 1 \pmod 2$, nunca 0. Portanto $\nu(2)=1$ (a única solução é $p\equiv 1 \pmod 2$, que é a condição de ímpar; ajustamos o produto para refletir que consideramos apenas ímpares). O fator local resulta em $H_2 = 2$.

### 3.2 $q = 3$
$p(5p+6) \equiv p(2p) \equiv 2p^2 \pmod 3$. A única solução é $p\equiv 0 \pmod 3$. Logo $\nu(3)=1$, $H_3 = \frac{1-1/3}{(1-1/3)^2} = \frac{3}{2}$.

### 3.3 $q = 5$
$p(5p+6) \equiv p(0+1)\equiv p \pmod 5$. Solução única: $p\equiv 0 \pmod 5$. Logo $\nu(5)=1$, $H_5 = \frac{1-1/5}{(1-1/5)^2} = \frac{5}{4}$.

### 3.4 $q > 5$
Para $q \nmid 30$, a congruência é quadrática com duas raízes distintas: $p\equiv 0$ e $p\equiv -6\cdot 5^{-1} \pmod q$. Portanto $\nu(q)=2$ e

$$H_q = \frac{1-2/q}{(1-1/q)^2} = \frac{q(q-2)}{(q-1)^2}.$$

---

## 4. Resolução do Produto Infinito

Reunindo os termos calculados:

$$\mathfrak{S} = 2 \cdot \frac{3}{2} \cdot \frac{5}{4} \cdot \prod_{q>5} \frac{q(q-2)}{(q-1)^2} = \frac{15}{4} \prod_{q>5} \frac{q(q-2)}{(q-1)^2}.$$

Usando a constante dos primos gêmeos $C_2 = \prod_{q>2} \frac{q(q-2)}{(q-1)^2} \approx 0,6601618$, temos:

$$\prod_{q>5} \frac{q(q-2)}{(q-1)^2} = \frac{64}{45} C_2.$$

Logo,

$$\mathfrak{S} = \frac{15}{4} \cdot \frac{64}{45} C_2 = \frac{16}{3} C_2 \approx 5,33333 \cdot 0,6601618 \approx 3,52086.$$

---

## 5. Interpretação Heurística e Comparação com Dados Experimentais

### 5.1 Significado do valor $\mathfrak{S} \approx 3,52$

Sob a heurística de Hardy‑Littlewood, o par $(p,5p+6)$ tem uma densidade assintótica de primos **cerca de 3,52 vezes maior** do que a de um par de números ímpares aleatórios da mesma magnitude. O ganho estrutural teórico (acima do modelo de Poisson ingênuo) é de $+252\%$.

### 5.2 Verificação experimental (dados de herança ativa, $N=10^7$)

O experimento de herança ativa (sobrevivência de cadeias $T(C)$) mediu:
- Taxa real de sobrevivência: $21,87\%$
- Taxa do modelo ingênuo (PNT): $6,69\%$
- Ganho empírico: $+227\%$

O ganho teórico esperado $+252\%$ é próximo do observado, considerando correções de escala fina e o fato de que o experimento não cobre toda a cauda assintótica. **Esta compatibilidade serve como evidência numérica favorável à heurística**, mas não constitui uma prova analítica independente.

---

## 6. Conclusão para o Operador de Transferência

A dedução da série singular fornece a **predição heurística** para a probabilidade de transição condicional:

$$P\bigl(T(C)-1 \in \mathbb{P} \mid C-1 \in \mathbb{P}\bigr) \sim \frac{3,52}{\log(5N)} \quad (N\to\infty).$$

Como $3,52 > 1$, a perda natural de densidade de primos ($1/\log(5N)$) é mais que compensada pelo fator estrutural. **Sob a hipótese de Hardy‑Littlewood**, isso implica que a constante de transferência $\gamma(N) = 3,52 \cdot \frac{\log N}{\log(5N)}$ satisfaz a desigualdade necessária ao Teorema 3 (Rota A). Na ausência de uma prova da conjectura de Hardy‑Littlewood, este resultado deve ser tratado como uma **forte evidência heurística** para o comportamento do motor, corroborada pelos dados numéricos até $10^8$.

---

*Nota redigida em maio de 2026 – versão corrigida (ênfase na natureza heurística).*