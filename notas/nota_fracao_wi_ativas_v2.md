# Nota: Fração de Wi Ativas e Constante Geométrica do Motor (atualizada)

**Série Motor de Herança Estrutural — Tiago Bandeira, Maio 2026**  
*Versão 2 – incorporando resultados estendidos até $C = 500.000$ e a relação com a série singular*

---

## Contexto

Na configuração canônica da grade $G(3 \times C)$, o scanner gera $m \approx M^+/8$ janelas $W_i$, cada uma com 4 eixos satisfazendo $E_1 + E_2 = 2M^+$ incondicionalmente. $HR^-$ ativa em uma $W_i$ quando pelo menos um eixo tem ambos os extremos primos.

A questão investigada: **como a fração de $W_i$ ativas se comporta conforme $M^+$ cresce?**

---

## Resultados Empíricos Estendidos

Foram testados valores de $C$ (pares) até $500.000$ (equivalentes a $M^+ = 6C$ até $3.000.000$). Os dados foram agrupados em blocos de $50.000$ em $C$. A tabela abaixo mostra a estabilização a partir de $C \approx 75.000$:

| $C_{\text{mid}}$ | $\langle\mathfrak{S}(6C)\rangle$ | $c_{\text{emp}}$ | $16 C_2 \langle\mathfrak{S}\rangle$ | $4 \cdot \text{dens-ancora} \cdot \log^2 C$ |
|-------------------|-----------------------------------|--------------------|--------------------------------------|----------------------------------------------|
| 75.003            | 2,2725                            | 21,57              | 24,00                                | 22,59                                        |
| 125.003           | 2,2711                            | 21,13              | 23,99                                | 22,02                                        |
| 175.003           | 2,2712                            | 21,02              | 23,99                                | 21,84                                        |
| 225.003           | 2,2724                            | 20,99              | 24,00                                | 21,78                                        |
| 275.003           | 2,2714                            | 20,93              | 23,99                                | 21,69                                        |
| 325.003           | 2,2729                            | 20,94              | 24,01                                | 21,69                                        |
| 375.003           | 2,2718                            | 20,95              | 24,00                                | 21,68                                        |
| 425.003           | 2,2727                            | 20,98              | 24,01                                | 21,69                                        |
| 475.002           | 2,2717                            | 20,97              | 24,00                                | 21,66                                        |

**Síntese (últimos 9 blocos):**

- $\langle\mathfrak{S}(6C)\rangle \approx 2,27$ (estável)
- $c_{\text{emp}}$ médio $\approx 21,0$
- $16 C_2 \langle\mathfrak{S}\rangle \approx 24,0$ (previsto se os 4 eixos fossem independentes)
- $4 \cdot \text{dens-ancora} \cdot \log^2 C \approx 21,7$ (quase idêntico a $c_{\text{emp}}$)

**Conclusão empírica:** a fração de janelas ativas é aproximadamente

$$\frac{\text{Wi ativas}}{\text{Wi totais}} \approx \frac{c}{\log^2 M^+},\quad \text{com } c \approx 21 \text{ para } M^+ \gtrsim 10^5.$$

---

## Relação com a Série Singular e a Constante dos Primos Gêmeos

O valor de $c$ pode ser decomposto como:

$$c = 4 \cdot n_{\text{ef}} \cdot C_2 \cdot \langle\mathfrak{S}(6C)\rangle,$$

onde $C_2 = 0,6601618$ é a constante dos primos gêmeos, $\langle\mathfrak{S}\rangle \approx 2,27$ é a média da série singular sobre os $C$ pares, e $n_{\text{ef}} \approx 3,6$ é o **número efetivo de eixos independentes** por janela (os quatro eixos não são completamente independentes devido a correlações aritméticas – por exemplo, módulo 3,5,7…). O fator $4$ vem do número de eixos; o fator $C_2 \langle\mathfrak{S}\rangle$ vem da densidade esperada de representações de Goldbach; e $n_{\text{ef}}$ quantifica a perda de independência.

A previsão $16 C_2 \langle\mathfrak{S}\rangle \approx 24$ corresponde a $n_{\text{ef}}=4$, que seria o caso de eixos perfeitamente independentes. A diferença de cerca de 12% para o valor observado é devida a correlações negativas (já medidas entre janelas distintas em $\approx -2,5\%$, e também presentes intra‑janela).

---

## Por que $c \approx 21$ (em vez de 1) – A força da geometria

Num modelo de Poisson ingênuo na reta numérica, a probabilidade de um par $(p,2M^+-p)$ ser primo‑primo seria $\sim 1/\log^2 M^+$, o que corresponderia a $c=1$. A estrutura das janelas $W_i$ multiplica essa eficiência por um fator de aproximadamente **21**, pelas seguintes razões estruturais:

- Cada janela tem **quatro eixos**, o que dá uma tentativa múltipla (fator 4).
- Os elementos inferiores $E_1$ dos eixos são ímpares **pequenos** (região $R_1$), onde a densidade de primos é muito maior do que em torno de $M^+$.
- A série singular $\mathfrak{S}(6C)$ é, em média, $\approx 2,27$ (maior que 1), reflectindo a abundância de fatores primos pequenos em $6C$.
- O produto desses efeitos ($4 \times 2,27 \times C_2 \approx 4 \times 2,27 \times 0,66 \approx 6$), combinado com o fator de correção $n_{\text{ef}} \approx 3,6$ (em vez de 4), leva a $c \approx 21$.

---

## Conexão com o decaimento exponencial e a lei $k^* \sim 5,5\log N$

A fração de janelas ativas está diretamente ligada à densidade $\rho_{\text{janela}} = c / \log^2 C$, que por sua vez determina a taxa de decaimento do gap máximo:

$$\beta = -\log(1 - \rho_{\text{janela}}) \approx \rho_{\text{janela}} = \frac{c}{\log^2 C}.$$

Com $c \approx 21$ e $\log^2 C \approx 230$ (para $C \approx 5\cdot10^6$), obtém-se $\beta \approx 0,09$ – um pouco abaixo do valor observado ($\approx 0,20$). A discrepância é explicada pelo facto de a densidade efectiva nos primeiros passos (âncoras pequenas) ser maior que a média, acelerando o decaimento. A lei final $k^* \sim 5,5\log N$ é dominada pelo regime de eliminação dos últimos buracos, que depende do número de classes mod 8 (4) e não directamente de $c$. A constante $c$ é mais relevante para o valor exacto de $\beta$ na parte assintótica.

---

## Status e próximos passos

| Item | Status |
|---|---|
| Fração Wi ativas $\sim c/\log^2 M^+$ | Confirmado (estável para $M^+ \gtrsim 10^5$) |
| Valor empírico de $c$ | $\approx 21$ |
| Relação $c = 4 \cdot n_{\text{ef}} \cdot C_2 \cdot \langle\mathfrak{S}\rangle$ | Confirmado ($n_{\text{ef}} \approx 3,6$) |
| Expressão analítica de $n_{\text{ef}}$ (produto euleriano) | **Em aberto** (pode ser derivada da correlação entre eixos módulo primos pequenos) |
| Prova incondicional de $c > 1$ | **Em aberto** (mas os dados mostram $c \gg 1$) |

---

*Nota atualizada com base nos scripts `verificar_constante_c.py` e `verifica_fator_4.py`. Código disponível no repositório da série.*