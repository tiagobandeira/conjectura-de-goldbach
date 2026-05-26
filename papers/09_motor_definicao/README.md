# Motor de Herança Estrutural
### Documento de Formalização — Versão Definitiva

**Tiago Bandeira** · tiagobandeira.goldbach2025@gmail.com  
Maio de 2026

---

> **Nota do Autor.**
> Este documento substitui e corrige as definições do Motor presentes nos Artigos 5 e 6 da série.
> A distinção central corrigida nesta revisão é: o **par base** (2M) é a soma das colunas da fita —
> o sistema já sabe que é Goldbach. O **par alvo** (2M+2) é a soma das diagonais da fita —
> quem certifica que é Goldbach é HR−.
> Esta distinção propaga-se por todas as definições do motor.

---

## Glossário — Distinção Fundamental

| Conceito | Definição | Quem garante |
|----------|-----------|--------------|
| **Par base 2M** | Soma das colunas da fita: $a_k + b_k = 2M$ | O sistema escolhe colunas com primos — Goldbach já é conhecido para 2M. |
| **Par alvo 2M+2** | Soma das diagonais da fita: $a_{k+1} + b_k = 2M+2$, $k \in \{1,\ldots,N-1\}$ | HR− certifica que 2M+2 é Goldbach ao encontrar primos nos extremos de $W_i$. |

---

## 1. Motivação e Mudança de Paradigma

A Conjectura de Goldbach afirma que todo número par maior que 2 é soma de dois primos.
A abordagem clássica trata essa questão de forma estática — para cada par 2M, pergunta-se se existe uma decomposição $2M = p + q$.
O Motor de Herança Estrutural substitui essa pergunta estática pela pergunta dinâmica:

> **Dado que 2M é Goldbach (par base), a estrutura geométrica garante que 2M+2 (par alvo) também o é?**

O motor organiza os ímpares em dois objetos acoplados — a Fita-Dobra e a Grade — de forma que a certificação de Goldbach para o par alvo deixe de ser uma questão aritmética pontual e passe a ser uma propriedade emergente de ocupação espacial.
A varredura geométrica substitui o teste aritmético.

---

## 2. A Fita-Dobra F(2×N)

### 2.1 Definição

A Fita-Dobra é uma matriz 2×N construída a partir do par base 2M.

| | $k=1$ | $k=2$ | $k=3$ | $\cdots$ | $k=N$ |
|---|---|---|---|---|---|
| **Linha 1 →** | $a_1 = 1$ | $a_2 = 3$ | $a_3 = 5$ | $\cdots$ | $a_N = 2N-1$ |
| **Linha 2 ←** | $b_1 = 2M-1$ | $b_2 = 2M-3$ | $b_3 = 2M-5$ | $\cdots$ | $b_N = 2M-(2N-1)$ |

A Linha 1 percorre os ímpares crescentes da esquerda para a direita.
A Linha 2 percorre os complementares da direita para a esquerda.

### 2.2 Propriedade Fundamental — Soma Constante (Par Base)

**Proposição (Par Base).** Para toda coluna $k \in \{1,\ldots,N\}$:

$$a_k + b_k = 2M$$

Esta soma é constante, independente da posição $k$ e independente de primalidade.
A fita é **cega à posição** e **cega à primalidade**.
O par base 2M é certificado por Goldbach ao se encontrar uma coluna $k$ com $a_k$ e $b_k$ ambos primos — o motor parte desse fato como dado.

### 2.3 As Diagonais da Fita — Par Alvo

Além dos pares colunares, a fita contém pares diagonais: pares $(a_{k+1},\, b_k)$ que cruzam entre colunas adjacentes. Por construção:

$$a_{k+1} + b_k = (2(k+1)-1) + (2M - 2k + 1) = (2k+1) + (2M - 2k + 1) = 2M+2$$

Cada par diagonal soma exatamente $2M+2$, independente de primalidade.
Esses pares diagonais são o objeto que o scanner captura e armazena em $W_i$.
A certificação de que $2M+2$ é Goldbach depende de encontrar uma diagonal com ambos os extremos primos — isso é precisamente **HR−**.

### 2.4 A Fita Representa Dois Pares Consecutivos

A Fita-Dobra representa simultaneamente dois números pares consecutivos:
o par base $2M$ (soma das colunas) e o par alvo $2M+2$ (soma das diagonais).
Isso é necessário para que o motor cubra todos os pares sem exceção.

**Nota:** quando $M$ é ímpar, $M + M = 2M$ faz com que o centro da fita (coluna $N$) tenha um elemento repetido.
Quando $M$ é par, o centro tem $M$ e $M+1$ adjacentes sem repetição.
Esta adaptação garante a proporção 2:1 entre naturais e ímpares e que a fita cubra dois pares consecutivos distintos.

---

## 3. A Grade G(3×C) e o Acoplamento

### 3.1 Condição de Acoplamento

A Grade G(3×C) é uma matriz de três linhas e $C$ colunas que contém os mesmos ímpares da Fita-Dobra, organizados em percurso zigzag. Para que grade e fita representem exatamente o mesmo conjunto de ímpares:

$$\boxed{3C = 2N}$$

Quando o número total de ímpares não é divisível por 3, duplicações centrais são introduzidas para satisfazer a condição.

### 3.2 Percurso Zigzag da Grade

Os ímpares são dispostos na grade em percurso zigzag de três linhas: Linha 1 (→), Linha 2 (←), Linha 3 (→).
Este percurso garante que as diagonais geométricas da grade correspondam às diagonais da fita.

**Exemplo:** Grade G(3×8) — par base 2M = 48, par alvo 2M+2 = 50.
Acoplamento: $3 \times 8 = 2 \times 12 = 24$ células. ✓

| | $c=1$ | $c=2$ | $c=3$ | $c=4$ | $c=5$ | $c=6$ | $c=7$ | $c=8$ |
|---|---|---|---|---|---|---|---|---|
| **Linha 1 →** | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 |
| **Linha 2 ←** | 31 | 29 | 27 | 25 | 23 | 21 | 19 | 17 |
| **Linha 3 →** | 33 | 35 | 37 | 39 | 41 | 43 | 45 | 47 |

---

## 4. A Janela $W_i$ — Definição Correta

$W_i$ é uma matriz 3×3 **fixa** que armazena, nos seus quatro eixos de simetria, até quatro diagonais da fita que somam o par alvo $2M+2$.
$W_i$ **não é deslizante**: ela é preenchida pelo scanner e permanece como referência estrutural.

### 4.1 Os Quatro Eixos de Simetria de $W_i$

Uma matriz 3×3 possui exatamente quatro linhas de simetria que passam pelo centro.
Cada eixo conecta dois extremos opostos e define um slot para um par diagonal da fita:

| Eixo | Posições |
|------|----------|
| **D1 — Diagonal Principal** | $[0,0] \leftrightarrow [2,2]$ |
| **D2 — Diagonal Secundária** | $[0,2] \leftrightarrow [2,0]$ |
| **Cv — Coluna Central** | $[0,1] \leftrightarrow [2,1]$ |
| **Lc — Linha Central** | $[1,0] \leftrightarrow [1,2]$ |

Em cada eixo: o elemento menor da diagonal é posicionado na entrada, o maior na posição oposta.
O centro $[1,1]$ armazena o **pivô** — o elemento central da varredura do scanner.

### 4.2 Estrutura Visual de $W_i$

```
┌─────────────┬─────────────┬─────────────┐
│  E₁(D1)     │  E₁(Cv)     │  E₁(D2)     │
├─────────────┼─────────────┼─────────────┤
│  E₁(Lc)     │    PIVÔ     │  E₂(Lc)     │
├─────────────┼─────────────┼─────────────┤
│  E₂(D2)     │  E₂(Cv)     │  E₂(D1)     │
└─────────────┴─────────────┴─────────────┘
```

Em cada eixo: $E_1 + E_2 = 2M+2$ (par alvo) — garantido incondicionalmente pela construção da fita.

### 4.3 Exemplo Numérico de $W_i$ (par base = 48, par alvo = 50)

```
┌────┬────┬────┐
│  7 │  9 │ 11 │
├────┼────┼────┤
│ 37 │ 25 │ 13 │
├────┼────┼────┤
│ 39 │ 41 │ 43 │
└────┴────┴────┘
```

- D1: 7 + 43 = 50 ✓ &nbsp; &nbsp; Cv: 9 + 41 = 50 ✓ &nbsp; &nbsp; D2: 11 + 39 = 50 ✓ &nbsp; &nbsp; Lc: 13 + 37 = 50 ✓
- **HR−:** D1 → (7, 43): 7 primo ✓, 43 primo ✓ → HR− ativada, certificando 50 = 7 + 43.

### 4.4 Número de Janelas $W_i$ por Varredura

Como cada $W_i$ comporta até 4 diagonais e existem $N-1$ diagonais internas na fita (excluindo $a_1 = 1$), o número de janelas necessárias para cobrir todas as diagonais é aproximadamente $\lceil (N-1)/4 \rceil$.

---

## 5. O Scanner — Preenchimento de $W_i$

### 5.1 O Mecanismo dos Pivôs

O scanner percorre a grade e preenche os eixos de $W_i$ com as diagonais da fita.
Dois pivôs marcham das extremidades da lista de ímpares em direção ao centro.
O pivô esquerdo **pula a primeira posição** (elemento 1), pois o 1 não forma diagonal secundária válida — não existe elemento na grade tal que $1 + a = 2M+2$.

**Algoritmo do Scanner:**
1. Posicionar pivô esquerdo na segunda posição da lista (pula o elemento 1).
2. Posicionar pivô direito na extremidade final da lista.
3. Registrar o par $(E_{esq},\, E_{dir})$ num eixo de $W_i$. O elemento central da lista é o pivô do sensor.
4. Avançar pivô esquerdo (+1) e recuar pivô direito (−1).
5. Repetir até os pivôs se encontrarem. Cada iteração preenche um eixo de $W_i$.
6. Quando $W_i$ tiver os 4 eixos preenchidos, registrá-la e iniciar nova $W_i$ para o bloco seguinte.

### 5.2 Propriedade de Soma Constante nos Eixos

Por construção da Fita-Dobra (Seção 2.3), cada par $(E_1, E_2)$ capturado pelo scanner satisfaz automaticamente $E_1 + E_2 = 2M+2$, independente de os elementos serem ou não primos.
Esta é a **garantia algébrica incondicional** do motor.

---

## 6. As Hipóteses Restritivas HR− e HR+

O motor opera em duas camadas.
A **camada algébrica** — construção da fita, acoplamento com a grade, preenchimento de $W_i$ pelo scanner — é inteiramente incondicional.
A **camada aritmética** introduz as únicas hipóteses não provadas:

| Hipótese | Condição | Significado |
|----------|----------|-------------|
| **HR− (Fraca)** | $\exists$ eixo de $W_i$ com $E_1, E_2 \in \mathbb{P}$ | Certifica o par alvo $2M+2$ como Goldbach. |
| **HR+ (Forte)** | $\exists$ eixo de $W_i$ com $(E_1,\, \text{Pivô},\, E_2) \in \mathbb{P}^3$ | Versão forte; implica HR−; conecta ao formalismo espectral. |

A separação entre camada algébrica e camada aritmética é a essência da arquitetura do motor:
a existência geométrica dos pares e sua cobertura pelos eixos de $W_i$ são incondicionais;
a primalidade simultânea dos extremos é o único ingrediente aritmético.
**HR− é a lacuna central** — objeto do próximo artigo da série.

---

## 7. O Gabarito — $W_i$ Canônica como Referência

### 7.1 O Que é o Gabarito

O Gabarito é uma instância canônica de $W_i$: uma janela construída com os pares obtidos pelo scanner na configuração canônica (ordenada) da grade, contendo pelo menos um par primo nos seus eixos.

> **Analogia:** se o motor fosse um acelerador de partículas, o gabarito seria a placa de detecção com os padrões de colisão esperados pré-impressos. Quando os dados dinâmicos se alinham com o gabarito, o sensor dispara HR− ou HR+.

**Por que o gabarito não é simplesmente copiar Goldbach da fita:**
Sem a estrutura geométrica da grade, pegar um par primo diretamente da fita é circular — equivale a afirmar Goldbach de forma direta.
O gabarito ancora a verificação no espaço físico das células da grade: o que está sendo verificado é a **ocupação espacial** de posições específicas por primos, não a existência aritmética de uma decomposição.

### 7.2 Estratégia Experimental

1. Construir o Gabarito — $W_i$ canônica com pares obtidos pelo scanner na grade ordenada, com pelo menos um par primo.
2. Iniciar o sistema em entropia máxima (caos puro).
3. Aplicar ordenação gradual.
4. A cada passo, sobrepor a configuração dinâmica ao Gabarito: quando as posições dos eixos coincidem com primos, o sensor dispara.

---

## 8. Protocolo de Simulação — Transição Caos → Ordem

### 8.1 Motivação

O experimento de transição de fase serve a dois propósitos:
1. Demonstrar computacionalmente que HR− e HR+ são ativadas durante a ordenação.
2. Medir o **Tempo de Primeira Passagem** — quantos passos (swaps) até que a primeira janela ative o sensor.

### 8.2 Protocolo

1. Escolher um par base 2M e construir a Fita-Dobra 2×N.
2. Executar o scanner na grade canônica e construir o Gabarito $W_i$ (referência fixa).
3. Embaralhar a lista de ímpares: entropia máxima (Caos Puro).
4. Verificar no estado inicial: o caos puro já ativa o sensor por acaso?
5. Aplicar ordenação total gradual (Bubble Sort — granularidade máxima).
6. A cada swap: executar o scanner e comparar com o Gabarito. Registrar ativação de HR− e HR+.
7. Registrar: Tempo de Primeira Passagem e percentual do percurso total até a ativação.

### 8.3 Métricas e Observações do Notebook

O notebook de verificação (`motor_heranca.ipynb`) coleta as seguintes métricas:

| Métrica | Descrição |
|---------|-----------|
| **Total de swaps** | Número de trocas até a ordenação canônica completa. |
| **Passo HR− (swap)** | Swap em que HR− é ativada pela 1ª vez — Tempo de Primeira Passagem. |
| **% do percurso** | Razão passo HR− / total de swaps: quão cedo no processo o evento ocorre. |
| **HR+ ativada** | Se existe $W_i$ com tripla prima completa antes do fim. |
| **Nº de janelas $W_i$** | Janelas geradas pelo scanner ≈ $\lceil (N-1)/4 \rceil$. |

**Observações empíricas dos testes iniciais (N pequeno):**

1. **HR− é frequentemente ativada já no swap 0** — no estado de caos puro, antes de qualquer ordenação. A estrutura geométrica de $W_i$ captura pares primos mesmo com dados completamente embaralhados. Isso faz sentido: $W_i$ é uma foto comprimida que amostra 3 regiões distintas da sequência $1,\ldots,N$ simultaneamente. No caos, os dados são partículas indistinguíveis — primos e compostos têm a mesma aparência probabilística — e mesmo assim a densidade de cobertura das janelas é suficiente para capturar pelo menos um par primo.

2. **Quando HR− não está ativa no caos**, ela é ativada muito cedo no percurso (geralmente abaixo de 10% do total de swaps), consistente com a Lei de Saturação Geométrica.

3. **HR+** é ativada em alguns casos, mas não em todos — esperado, pois é uma condição estritamente mais restritiva que HR−.

4. **Os testes atuais cobrem N pequeno.** A verificação para N grande — com múltiplas janelas $W_i$ e análise do crescimento do Tempo de Primeira Passagem em função de N — está planejada como próxima etapa computacional.

> **Nota sobre o caos e os primos:** no estado de entropia máxima, primos e compostos são indistinguíveis — podem ser considerados partículas num espaço. O caos atenua temporariamente a pseudo-aleatoriedade aparente dos primos e sua densidade característica. À medida que a ordenação avança e a sequência se torna distinguível, essa pseudo-aleatoriedade emerge de volta — e com ela, HR− dispara.

---

## 9. O Teorema do Motor (condicional a HR−)

**Teorema do Motor de Herança Estrutural.**

*Hipóteses:*
- **(HI)** Existe $2M_0$ com par de primos $(p,q)$ tal que $p + q = 2M_0$ — par base certificado.
- **(HR−)** Para toda iteração do motor, $W_i$ contém pelo menos um eixo com $E_1$ e $E_2$ ambos primos e $E_1 + E_2 = 2M_0 + 2$ — par alvo certificado por HR−.

*Conclusão:* A cadeia $2M_0 \to 2M_0+2 \to 2M_0+4 \to \cdots$ cobre todos os pares $\geq 2M_0$ como somas de dois primos.
O par alvo de uma iteração torna-se o par base da iteração seguinte.

---

## 10. Mapa de Resultados

| Componente | Estatuto | Observação |
|------------|----------|------------|
| Soma das colunas = 2M (par base) | **Incondicional** | Álgebra pura; coluna prima certifica par base |
| Soma das diagonais = 2M+2 (par alvo) | **Incondicional** | $a_{k+1} + b_k = 2M+2$, $k \in \{1,\ldots,N-1\}$ |
| Acoplamento $3C = 2N$ | **Incondicional** | Condição necessária e suficiente |
| $W_i$ fixa com 4 eixos de simetria | **Incondicional** | Estrutura geométrica pura |
| Scanner (pivôs borda→centro, pula 1) | **Incondicional** | Preenche $W_i$ com diagonais do par alvo |
| Soma constante nos eixos de $W_i$ | **Incondicional** | $E_1 + E_2 = 2M+2$, herdado da fita |
| Gabarito como referência canônica | **Incondicional** | Foto da estrutura diagonal ordenada |
| HR− (par primo num eixo de $W_i$) | **Condicional** | Lacuna central — certifica o par alvo |
| HR+ (tripla prima completa em $W_i$) | **Condicional** | Versão forte; implica HR−; conecta ao espectral |
| Teorema do Motor | **Condicional a HR−** | Cobre todos os pares $\geq 2M_0$ por indução |

---

*Este documento é a base para a revisão dos Artigos 7 e 8 da série sobre a Conjectura de Goldbach.
O código de simulação unificado (`motor_heranca.py`) e o notebook de verificação (`motor_heranca.ipynb`) implementam todos os módulos aqui descritos.*
