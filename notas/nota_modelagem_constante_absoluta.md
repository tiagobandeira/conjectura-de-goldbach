# Nota Técnica: Modelagem Probabilística da Constante Absoluta de Busca $A_{\text{abs}} \approx 10$ e Colapso de Gargalo Modular

**Série:** Motor de Herança Estrutural — Conjectura de Goldbach — Nota de Fundamentação Geométrica  
**Autor:** Tiago Bandeira  
**Data:** Maio de 2026  
**Status:** Esboço de Fundamentação para o Artigo 7 / Nota Complementar  

---

> **Resumo.** Esta nota técnica apresenta a modelagem probabilística que explica o colapso do coeficiente de escala física de busca do Scanner de $A \approx 44$ para $A_{\text{abs}} \approx 10$ na transição do regime restrito para o regime absoluto (multieixo). Demonstra-se que o ganho de eficiência geométrica de $+363\%$ é governado principalmente pela liberação das classes modulares sob a função totiente de Euler $\varphi(8) = 4$ e, secundariamente, pela compensação simétrica local (anticorrelação) dos eixos da janela na fita-dobra.

---

## 1. Introdução e o Problema da Deriva de $A$

Nas versões anteriores do crivo do Motor de Herança Estrutural, a Regra Restrita limitava a busca por âncoras ao eixo associado à progressão $8j-5 \equiv 3 \pmod 8$. Sob este regime, o coeficiente de cauda de busca $A(N)$ na lei de escala:

$$p_{\max}(N) \approx A(N) \cdot \log N \cdot \log \log N$$

revelou-se instável em faixas de alta magnitude, derivando de $44.75$ (em $N=10^6$) para $58.94$ (em $N=10^8$). 

Por outro lado, o Experimento 1 (Saturação de Cobertura) estabeleceu que a ativação da totalidade dos eixos simétricos da janela (Regra Absoluta) colapsa o teto de busca física de $p_{\max} = 2083$ para $p_{\max} = 449$ (em $N=10^7$), com estabilização robusta do coeficiente em $A_{\text{abs}} \approx 10.02$. Esta nota deduz analiticamente a origem deste comportamento limite.


> "A Regra Absoluta (multieixo) utiliza **todos os quatro eixos de todas as janelas** $W_j$ geradas pelo scanner. Isso equivale a permitir qualquer âncora $p \ge 5$ (primo absoluto). A condição $HR^{-}$ expressa, portanto, a existência de **alguma janela** cujo eixo contenha um par $(p, 6C-p)$ de números primos."

---

## 2. Densidade de Âncora sob Teorema dos Primos para Progressões Aritméticas

A eficiência física de busca do Scanner depende diretamente da densidade local do conjunto de âncoras admissíveis no intervalo de busca.

### 2.1 Densidade no Regime Restrito ($8j-5$)
Sob a Regra Restrita, o pool de âncoras é confinado a uma única classe de resíduo modulo 8:
$$p \equiv 3 \pmod 8$$

Pelo Teorema dos Primos para progressões aritméticas, a densidade assintótica de primos em classes coprimas modulo $q$ é uniforme e dada por $1 / (\varphi(q) \log x)$. Como $\varphi(8) = 4$ (classes $\{1, 3, 5, 7\}$), a densidade local de âncoras restritas é exatamente um quarto da densidade geral:

$$\rho_{\text{restrita}}(x) \sim \frac{1}{\varphi(8) \cdot \log x} = \frac{1}{4 \log x}$$

### 2.2 Densidade no Regime Absoluto (Multieixo)
A Regra Absoluta utiliza os 4 eixos nativos da janela $W_j$, mapeando as 4 classes coprimas de $\varphi(8)$. O pool de âncoras disponíveis expande-se para a totalidade dos números primos $p \ge 5$, cuja densidade local é governada pelo PNT geral:

$$\rho_{\text{absoluta}}(x) \sim \frac{1}{\log x}$$

---

## 3. A Equação do Limite de Cobertura e a Redução por $\varphi(8)$

O número de janelas $k^*$ necessárias para assegurar a saturação de cobertura completa de um intervalo $[4, N]$ correlaciona-se com a magnitude da maior âncora utilizada ($p_{\max}$) através da função de contagem de primos do pool:

$$k^* \approx \pi_{\text{pool}}(p_{\max}) \approx \int_2^{p_{\max}} \rho_{\text{pool}}(x) dx$$

Para uma mesma complexidade dimensional de saturação ($k^* \approx 80 \sim 85$ janelas, conforme demonstrado no Experimento 1), igualamos as estimativas de contagem assintótica sob ambos os regimes:

$$\frac{p_{\max}^{\text{restrita}}}{4 \log p_{\max}^{\text{restrita}}} \approx k^* \approx \frac{p_{\max}^{\text{absoluta}}}{\log p_{\max}^{\text{absoluta}}}$$

Desprezando a variação logarítmica de segunda ordem para escalas fixadas, obtemos a relação de escala direta entre os coeficientes de cauda:

$$\frac{A_{\text{restrita}}}{A_{\text{abs}}} \approx \varphi(8) = 4$$

### 3.1 Projeção Teórica
Aplicando o fator de redução analítico sobre a constante empírica medida no regime restrito em $N=10^7$ ($A = 44.35$):

$$A_{\text{teórico, abs}} = \frac{44.35}{4} = 11.08$$

O valor empírico real medido sob a Regra Absoluta foi de **$10.02$**. A diferença residual de $\approx 1.0$ (uma melhora adicional na eficiência real de busca) aponta para a existência de um efeito geométrico de acoplamento entre os eixos.

---

## 4. Efeito de Compensação Simétrica Local (Anticorrelação)

Os 4 eixos simétricos projetados por uma janela $W_j$ não se comportam como canais estocásticos independentes; eles são restritos pela álgebra da fita-dobra. Os candidatos inferiores desses eixos correspondem a quatro números ímpares consecutivos:

$$e_1^{(1)}, e_1^{(2)}, e_1^{(3)}, e_1^{(4)}$$

Esta proximidade aritmética gera uma forte restrição de solubilidade local mod $q$ para primos pequenos:

1.  **Modulo 3:** Três ímpares consecutivos cobrem necessariamente o conjunto completo de resíduos $\{0, 1, 2\} \pmod 3$. Isto garante que se um dos eixos for obstruído por divisibilidade por 3, os outros eixos estarão simultaneamente livres desta obstrução.
2.  **Modulo 5:** Quatro ímpares consecutivos cobrem 4 dos 5 resíduos de $\mathbb{F}_5$. A probabilidade de obstrução simultânea por 5 colapsa.

Esta dependência modular gera a correlação cruzada negativa discreta (anticorrelação média de $-2.5\%$, medida no Experimento 3). Probabilisticamente, a falha conjunta de cobertura de uma janela $W_j$ sob a regra absoluta é estritamente menor do que o produto das probabilidades de falha de 4 canais independentes:

$$P(\text{Falha Conjunta } W_j) < \prod_{i=1}^4 P(\text{Falha Eixo } i)$$

Este acoplamento geométrico otimiza a dispersão das ativações, reduzindo o limite superior de cauda de $11.08$ para o coeficiente de equilíbrio estável de **$10.02$** observado nas simulações.

---

## 5. Conclusão

A estabilização da constante de busca física em $A_{\text{abs}} \approx 10$ está matematicamente fundamentada. A transição para a análise multieixo remove o gargalo de classe modular mod 8 induzido artificialmente pela regra restrita ($8j-5$), multiplicando a densidade de âncoras disponíveis por $4$. A simetria física da janela introduz adicionalmente uma anticorrelação que otimiza a cobertura fina. 

Isto demonstra que o motor sob a regra absoluta não sofre da deriva de escala observada no regime restrito, comportando-se como um invariante estrutural previsível para a fita-dobra.