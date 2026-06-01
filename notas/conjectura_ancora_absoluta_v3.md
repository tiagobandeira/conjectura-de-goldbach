# Conjectura da Âncora Absoluta (versão 3.0)

**Autor:** Tiago Bandeira  
**Data:** Junho 2026  
**Série:** Motor de Herança Estrutural — Conjectura de Goldbach

> **Resumo.** Com base na estrutura geométrica do Motor de Herança e em evidências numéricas até $N=10^9$ (i.e., $2M\le 6\cdot10^9$), formulamos uma conjectura quantitativa sobre a existência de uma decomposição de Goldbach com o menor primo **logaritmicamente pequeno**. A conjectura é suportada por leis de escala empíricas ($k^*\sim6{,}3\log N$, $p_{\max}\approx11{,}8\log N\log\log N$), pela **quase‑independência** entre as ativações das âncoras absolutas (correlação média $<0{,}4\%$) e pela derivação analítica das constantes geométricas ($n_{\text{ef}}=36/\pi^2$, $c\approx21$). Resultados teóricos incondicionais (independência de crivo, recorrência $T(C)=5C+2$) fornecem a justificativa estrutural.

---

## 1. Enunciado da Conjectura (versão atualizada)

**Conjectura C (Âncora Absoluta).**  
Existem constantes $C_0>0$ e $A>0$ tais que, para todo número par $2M\ge C_0$, existe um número primo $p$ (chamado *âncora absoluta*) satisfazendo:

1. $p \le A\cdot\log M\cdot\log\log M$;
2. $2M-p$ também é primo;
3. O primo $p$ pode ser encontrado pelo **processo guloso** (testar os primos em ordem crescente) e o número total de primos necessários para cobrir todos os pares até $2M$ é assintoticamente $k^*(M)\sim\kappa\cdot\log M$, com $\kappa\approx6{,}3$.

Os dados numéricos até $N=10^9$ sugerem que podemos tomar $C_0=10^7$ e $A=12$. A constante $A$ efetiva estabiliza entre $11$ e $12$ para $N\ge10^8$, com clara convergência ($A=11{,}81$ em $5\times10^8$ e $A=11{,}83$ em $10^9$).

**Equivalência geométrica:**  
Para cada par alvo $2M^+=4N$ (com $N$ par), existe um índice $i$ (janela $W_i$) e um dos seus quatro eixos cujo extremo inferior $p$ é primo e o extremo superior $q=2M^+-p$ também é primo. O processo guloso que percorre os primos em ordem crescente constrói essas âncoras e cobre todos os pares.

---

## 2. Evidência empírica (até $N=10^9$)

### 2.1 Leis de escala

| $N$ (limite de $C$) | $k^*$ (âncoras) | $p_{\max}$ | $A = p_{\max}/(\log N\log\log N)$ | $k^*/\log N$ |
|---------------------|------------------|--------------|--------------------------------------|----------------|
| $10^6$              | 55               | 269          | 7,42                                 | 3,98           |
| $2\times10^6$       | 55               | 269          | 6,93                                 | 3,79           |
| $5\times10^6$       | 70               | 359          | 8,51                                 | 4,54           |
| $10^7$              | 85               | 449          | 10,02                                | 5,27           |
| $2\times10^7$       | 85               | 449          | 9,46                                 | 5,06           |
| $5\times10^7$       | 95               | 509          | 9,99                                 | 5,36           |
| $10^8$              | 105              | 587          | 10,94                                | 5,70           |
| $2\times10^8$       | 115              | 643          | 11,40                                | 6,02           |
| $5\times10^8$       | 125              | 709          | 11,81                                | 6,24           |
| $10^9$              | 130              | 743          | 11,83                                | 6,27           |

Para $N\ge10^7$ as leis empíricas são:

$$
k^*(N)\approx6{,}3\log N,\qquad p_{\max}(N)\approx11{,}8\log N\log\log N,
$$

com o coeficiente $A$ convergindo para $\approx11{,}8$.

### 2.2 Quase‑independência das ativações

- Correlação média entre pares de âncoras absolutas (100 primeiras) é **$<0{,}4\%$** (positiva), decrescendo com $N$.
- A variância do número de âncoras que cobrem um dado $C$ é $25$–$38\%$ maior que a predita pela independência.
- A anticorrelação de $-2{,}5\%$ observada no regime restrito ($8j-5$) não se aplica ao regime absoluto.

### 2.3 Saturação exponencial e cobertura total

- O gap máximo entre $C$ cobertos decai exponencialmente com a ordem das âncoras ($\beta\approx0{,}20$ em média).
- A cobertura final (gap máximo $=2$) é sempre $100\%$ (todos os $C$ pares até $N$ são cobertos).
- O modelo de Poisson independente subestima a variância, mas acerta a média; a fração de não cobertos torna‑se menor que $1/N$ para $k\approx6{,}3\log N$.

---

## 3. Base teórica e constantes analíticas

### 3.1 Geometria das janelas $W_j$

Os quatro eixos de $W_j$ fornecem elementos inferiores consecutivos, cobrindo todas as classes $\pmod 8$. Cada âncora $p$ aparece como $E_1$ de um único eixo numa única janela.

### 3.2 Número efectivo de eixos independentes $n_{\text{ef}}$

Para um primo $p\ge5$, o eixo está bloqueado se $p\mid E_1$ e $p\mid E_2$. Como $E_2=6C-E_1$, a condição $p\mid E_2$ implica $p\mid6C$. A fracção média de eixos bloqueados por $p$ é $1/p^2$ (pois $p\mid6C$ com probabilidade $1/p$). O primo $3$ não bloqueia âncoras (a única âncora múltipla de $3$ é o próprio $3$, excluído). Portanto,

$$
\frac{n_{\text{ef}}}{4}= \prod_{p\ge5}\Bigl(1-\frac1{p^2}\Bigr)=\frac{9}{\pi^2}\approx0{,}9119,
\qquad n_{\text{ef}}=\frac{36}{\pi^2}\approx3{,}6476.
$$

### 3.3 Densidade de cobertura e constante $c$

A densidade média de cobertura por eixo, sob a heurística de Hardy‑Littlewood (ou condicionalmente à GRH), é

$$
\rho_{\text{eixo}}(C)\approx\frac{2C_2\langle\mathfrak{S}\rangle}{\log^2 C},
$$

com $C_2=0{,}6601618$ (constante dos primos gêmeos) e $\langle\mathfrak{S}\rangle\approx2{,}27$ (média da série singular sobre os $C$ pares). Cada representação de Goldbach aparece duas vezes nos eixos, resultando na fracção de janelas ativas:

$$
\frac{\text{janelas ativas}}{\text{total janelas}} = \frac{4\,n_{\text{ef}}\,C_2\,\langle\mathfrak{S}\rangle}{\log^2 C},
\qquad\text{onde}\quad c = 4\,n_{\text{ef}}\,C_2\,\langle\mathfrak{S}\rangle \approx 21{,}8.
$$

O valor empírico é $c\approx21$, dentro de 4% da previsão.

### 3.4 Derivação das leis de escala

A separação em dois regimes (âncoras pequenas via teorema de Mertens, âncoras médias/grandes via eliminação das classes mod 8) leva a:

$$
k^*(N) = O(\log N),\qquad \beta \approx \frac{c}{\log^2 C}
$$

(com $\beta$ efectivo maior devido à aceleração inicial). Os valores numéricos concordam com as observações.

---

## 4. Discussão e trabalhos futuros

- A conjectura é **mais forte** do que a Conjectura de Goldbach, fornecendo uma cota explícita para o menor primo.
- Os dados até $10^9$ são compatíveis com $p_{\max}\le12\log N\log\log N$ para $N\ge10^7$.
- A quase‑independência ($<0{,}4\%$) justifica o uso de modelos probabilísticos como o Poisson.
- Trabalhos futuros: estender simulações a $10^{10}$; refinar a análise da variância; tentar uma prova analítica incondicional ou sob GRH.

---

## 5. Referências

- **Artigos da série:** Papers 07–11.
- **Notas técnicas:** `nota_sintese_cobertura_condicional_v3.md`, `nota_derivacao_beta_kstar_v2.md`, `nota_fracao_wi_ativas_v2.md`.
- **Scripts:** `bandeira_ancora_absoluta_extendida_v2.py`, `verificar_constante_c.py`, `verifica_fator_4.py`, `correlacao_janelas_escalas.py`, `ajuste_beta_gap.py`, `correlacao_C_vizinhos.py`.

*Esta conjectura consolida as descobertas experimentais e as derivações analíticas mais recentes (Junho 2026).*