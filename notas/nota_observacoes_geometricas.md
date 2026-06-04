# Nota — Observações Geométricas via Exploração Visual do Motor de Herança

**T. Bandeira · Junho de 2026**  
*Nota adicional à série Motor de Herança Estrutural — Artigos 01–12*

---

## Sobre Esta Nota

As observações registradas aqui foram descobertas através da exploração interativa da grade G(3×C) usando o **Motor de Herança Estrutural Explorer**, uma página web interativa que acompanha esta série. O Explorer permite visualizar a grade, o acoplamento Φ, os pares acoplados (HR⁻), os padrões de simetria e o processo guloso de âncoras diretamente no navegador, sem instalação.

> 🌐 **Demonstração Interativa:** Para acompanhar visualmente os conceitos geométricos apresentados nesta série (como a Fita-Dobra, a Grade $G_{3,C}$ e o Scanner de pivôs), acesse o simulador oficial em: [**Motor de Herança Estrutural**](https://tiagobandeira.github.io/goldbach-motor/)

As três observações desta nota emergem da intuição geométrica proporcionada pela visualização — elas complementam os resultados formais dos Artigos 01–12 com perspectivas que só se tornam visíveis quando se pode explorar a grade interativamente.

---

## 1. A Diagonal que Atravessa a Grade: Âncoras e seus Pares

### 1.1 Localização geométrica das âncoras

A Conjectura da Âncora Absoluta (Artigo 10) afirma que todo número par $2M$ admite decomposição de Goldbach com o menor primo satisfazendo:

$$p_{\text{âncora}} \lesssim 11{,}8 \cdot \log N \cdot \log\log N$$

e que $k^*(N) \sim 6{,}3 \log N$ âncoras cobrem todos os pares até $N$.

Na grade G(3×C), com $C = N/2$, a âncora $p$ ocupa a coluna $c = (p-1)/2$ de L1. Como $p_{\max} \ll N$, essa coluna satisfaz:

$$\frac{c}{C} = \frac{p-1}{N} \sim \frac{11{,}8 \log N \log\log N}{N} \xrightarrow{N\to\infty} 0$$

As âncoras ocupam uma **fração que vai a zero** do lado esquerdo da grade. Para $N = 10^7$, por exemplo, as 85 âncoras necessárias para cobertura total ficam nas primeiras 224 colunas de uma grade com 5 milhões de colunas — menos de 0,009% da largura.

### 1.2 Os pares no extremo oposto

Pelo acoplamento Φ, o par de Goldbach de uma âncora $p$ em $L1[c]$ é o elemento $L3[C-1-c]$, com valor $6C - p$. Como $p \ll 6C$, temos:

$$6C - p \approx 6C$$

O par da âncora está na coluna $C-1-c \approx C$ — o **extremo direito de L3**.

**Observação geométrica:** cada decomposição de Goldbach certificada por uma âncora é uma linha diagonal que conecta o extremo esquerdo de L1 ao extremo direito de L3, atravessando a grade de ponta a ponta. Quanto menor a âncora, mais longa e extrema é essa diagonal.

```
L1: [p] · · · · · · · · · · · · · · · · · ·
L2:  · · · · · · · · · · · · · · · · · · ·
L3:  · · · · · · · · · · · · · · · · · · [6C-p]
      ↑ extremo esquerdo            extremo direito ↑
```

Isso ilustra geometricamente por que âncoras pequenas são tão eficientes: um único primo pequeno no canto esquerdo, se seu complemento $6C - p$ for primo, cobre o par alvo inteiro com dois pontos nos extremos opostos da grade.

---

## 2. Quartetos de Simetria e Pares Acoplados Duplos

### 2.1 A estrutura do quarteto

O acoplamento Φ organiza os elementos da grade em **quartetos** naturais. Fixados $C$ e $c \in \{0, \ldots, C/2-1\}$:

$$q_1 = L_1[c] = 2c+1$$
$$q_2 = L_3[c] = 4C+2c+1 = q_1 + 4C$$
$$q_3 = L_1[C-1-c] = 2C-2c-1 = 6C - q_2$$
$$q_4 = L_3[C-1-c] = 6C-2c-1 = 6C - q_1$$

**Proposição (incondicional).** Para todo $C$ e $c$:

$$q_1 + q_4 = 6C, \qquad q_2 + q_3 = 6C$$
$$q_2 - q_1 = 4C \qquad \text{(distância L1→L3 na coluna } c\text{)}$$
$$q_4 - q_3 = 4C \qquad \text{(distância L1→L3 na coluna } C{-}1{-}c\text{)}$$
$$q_3 = 6C - q_2 = 2C - q_1$$

O quarteto contém dois pares de Goldbach potenciais: $(q_1, q_4)$ e $(q_2, q_3)$, ambos somando $6C = 2M^+$.

### 2.2 Simetria visual

A simetria que se observa no Explorer ao ativar "Mostrar acoplamento Φ" é exatamente esta: os pares acoplados (azuis) aparecem em posições que respeitam a inversão $c \leftrightarrow C-1-c$ com troca $L_1 \leftrightarrow L_3$. A simetria é **incondicional** — decorre da álgebra do acoplamento, não da primalidade.

### 2.3 Quartetos duplamente ativos

**Definição.** Um quarteto $(q_1, q_2, q_3, q_4)$ é *duplamente ativo* se todos os quatro são primos — ou seja, tanto $(q_1, q_4)$ quanto $(q_2, q_3)$ são pares de Goldbach para $6C$.

**Resultado empírico** (verificado até $C = 500$): a frequência de quartetos duplamente ativos dado que $(q_1, q_4)$ é ativo é aproximadamente **5,6 vezes maior** do que a esperada por independência (modelo de Poisson ingênuo). Isso indica correlação positiva real entre pares de Goldbach geometricamente relacionados na grade.

A proporção observada é ~13,6% dos pares ativos, contra ~2,4% esperado por independência.

### 2.4 Relação com HR⁻

Cada par ativo $(q_1, q_4)$ é exatamente um eixo de $W_i$ ativando HR⁻. Um quarteto duplamente ativo corresponde a **dois eixos simultâneos** de $W_i$ ativando HR⁻ para o mesmo par alvo — redundância geométrica que contribui para a robustez da cobertura.

---

## 3. Formas Geométricas dos Pares Acoplados

### 3.1 A forma como objeto geométrico

Para um dado $C$, os pares acoplados ativos (azuis) ocupam posições específicas na grade. O conjunto dessas posições forma uma **configuração geométrica** — uma "forma" — que é sempre bilateralmente simétrica por construção:

> Se a posição $(r, c)$ está azul, então a posição $(2-r, C-1-c)$ também está azul.

Isso é incondicional: decorre do fato de que cada par azul usa exatamente uma célula de cada lado do eixo central, com inversão de linha ($L_1 \leftrightarrow L_3$).

A simetria pode ser descrita como: **espelhamento horizontal + inversão vertical**. O lado direito da grade é sempre o reflexo do lado esquerdo com $L_1$ e $L_3$ trocados.

### 3.2 Hierarquia de formas

Ao explorar a grade para diferentes valores de $C$, observam-se formas recorrentes que podem ser classificadas pelos *gaps* entre posições ativas consecutivas. Formas simples (dois pontos adjacentes em linhas diferentes — "zigzag") aparecem em ~70% dos valores de $C$ testados. Formas compostas como o "S" ou "Z" (três posições com padrão específico de gaps) aparecem em ~35% dos casos.

Cada forma tem preferências modulares — por exemplo, a forma "S" com gaps $(1, (0,1,0), (1,0,1))$ favorece $C \equiv 10 \pmod{12}$.

### 3.3 Conexão com HR⁻ e saturação

HR⁻ garante que a forma nunca é vazia — sempre haverá pelo menos um par azul para qualquer $C$ suficientemente grande. A riqueza crescente das formas (mais posições azuis, padrões mais complexos) é a manifestação visual da **saturação geométrica** descrita no Artigo 11: à medida que $C$ cresce, mais âncoras cobrem mais pares simultaneamente, e as formas ficam progressivamente mais densas.

A lei empírica $k^*(N) \sim 6{,}3 \log N$ é visível nessa progressão: o número de posições azuis distintas cresce logaritmicamente, mas cada posição nova cobre uma fração exponencialmente menor dos $C$ restantes — o decaimento exponencial do gap visto como evolução das formas.

---

## 4. Síntese

As três observações desta nota são faces diferentes do mesmo fenômeno:

| Observação | O que revela | Estatuto |
|-----------|-------------|---------|
| Diagonal âncora–par | Localização geométrica da Conjectura da Âncora Absoluta | Incondicional (geometria) + empírico |
| Quartetos de simetria | Correlação 5,6× entre pares de Goldbach geometricamente relacionados | Empírico (até $C=500$) |
| Formas dos pares acoplados | Manifestação visual de HR⁻ e da saturação geométrica | Incondicional (simetria) + heurístico |

A simetria bilateral das formas é sempre garantida algebricamente. O que HR⁻ acrescenta é que a forma nunca é vazia. O que a Conjectura da Âncora garante é que a forma sempre tem elementos no extremo esquerdo da grade. E o decaimento exponencial do gap é a forma ficando progressivamente mais densa.

---

## Referências

[7] T. Bandeira, *Motor de Herança Estrutural: Formalização Definitiva*, preprint (2026).  
[10] T. Bandeira, *Leis de Escala e a Conjectura da Âncora Absoluta*, preprint (2026).  
[11] T. Bandeira, *Saturação Geométrica e Decaimento Exponencial do Gap*, preprint (2026).  
[12] T. Bandeira, *Saturação Geométrica e Cobertura Total: Uma Prova Condicional*, preprint (2026).

---

*Nota gerada a partir de sessão de exploração visual com o Motor de Herança Estrutural Explorer. O Explorer está disponível no repositório público e pode ser usado para verificar, estender ou refutar as observações aqui descritas.*
