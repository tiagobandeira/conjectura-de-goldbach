# Nota Técnica: Análise de Consistência — O Motor de Herança e a Heurística de Hardy–Littlewood

**Série:** Motor de Herança Estrutural – Conjectura de Goldbach  
**Autor:** Tiago Bandeira  
**Data:** Maio 2026  
**Status:** Nota de alinhamento – não constitui prova incondicional

> **Disclaimer**  
> Esta nota **não** reivindica uma prova da Conjectura de Goldbach. Seu objetivo é demonstrar que o Motor de Herança Estrutural, operando no regime absoluto, reproduz fielmente as densidades esperadas pela heurística de Hardy–Littlewood. Ao fazê‑lo, mostramos que o motor não introduz obstruções aritméticas adicionais e que o gargalo remanescente é exatamente o mesmo que desafia a comunidade há um século – o controlo dos arcos menores no método do círculo. Esta nota serve como validação da arquitetura do motor e como ponte para a reformulação espectral (Paper 08).

---

## 1. Objetivo

A série do Motor de Herança Estrutural [1–6] propõe uma mudança de paradigma: em vez de atacar pares isolados, o motor pergunta se a estrutura geométrica garante a cobertura de todos os pares por indução, a partir de um caso base. A lacuna central é a Hipótese Restritiva Fraca ($HR^-$): para cada par alvo $2M^+=4N$, existe um primo $p\ge5$ (âncora) tal que $2M^+-p$ também é primo.

A presente nota analisa a **consistência** do motor com os resultados clássicos de Hardy–Littlewood. Mostramos que, se assumirmos a heurística de Hardy–Littlewood (ou, alternativamente, controlarmos os arcos menores, o que é equivalente à própria dificuldade de Goldbach), então o motor prevê que $HR^-$ é verdadeira para todo $N$ suficientemente grande. Isto é, a arquitetura geométrica **não introduz obstáculos extras** – ela está alinhada com o que a teoria analítica espera.

---

## 2. Redução algébrica (incondicional)

Pelas propriedades da fita‑dobra (Paper 07), a existência de um par de primos para $2M^+=4N$ é equivalente à existência de um índice $k\in\{1,\dots,N-1\}$ tal que

$$a_{k+1}=2k+1 \quad\text{e}\quad b_k^{(1)}=4N-2k-1$$

são ambos primos. A soma sobre $k$ da função característica de primos é

$$T(N)=\sum_{k=1}^{N-1} \mathbf{1}_{\mathbb{P}}(2k+1)\,\mathbf{1}_{\mathbb{P}}(4N-2k-1).$$

A relação com a função de von Mangoldt é padrão:

$$T(N)=\frac{1}{(\log N)^2}\sum_{k=1}^{N-1}\Lambda(2k+1)\Lambda(4N-2k-1)+O(N^{1/2}).$$

---

## 3. A expectativa de Hardy–Littlewood

Definimos a soma ponderada

$$S(N)=\sum_{k=1}^{N-1}\Lambda(2k+1)\Lambda(4N-2k-1).$$

Pelo método do círculo (ver, e.g., [7, 8]), a contribuição dos **arcos maiores** para $S(N)$ é assintoticamente

$$S_{\text{maiores}}(N)\sim 4C_2\,\mathfrak{S}(4N)\,N,$$

onde

- $C_2=\prod_{p>2}\bigl(1-\frac{1}{(p-1)^2}\bigr)\approx0.66016$ é a constante dos primos gêmeos,
- $\mathfrak{S}(4N)=\prod_{q\mid 4N,\, q>2}\frac{q-1}{q-2}\ge 1$ é a série singular.

**A heurística de Hardy–Littlewood** postula que a contribuição dos **arcos menores** é desprezível comparada ao termo principal, de modo que

$$S(N)\sim 4C_2\,\mathfrak{S}(4N)\,N.$$

Esta é a predição clássica que está na base da conjectura de Goldbach.

---

## 4. O gargalo analítico (arcos menores)

A dificuldade central – e a razão pela qual a conjectura permanece aberta – reside em **controlar a integral sobre os arcos menores**. Mesmo sob a Hipótese de Riemann Generalizada (GRH), o conhecimento atual não é suficiente para provar que a contribuição dos arcos menores é $o(N)$. A GRH controla excelentemente os arcos maiores, mas os arcos menores exigem técnicas de cancelamento de exponenciais que ainda não foram dominadas.

Portanto, qualquer argumento que pretenda provar $T(N)>0$ incondicionalmente (ou mesmo sob GRH) terá que enfrentar essa mesma barreira. **O motor não a remove**, mas também **não a agrava** – ele simplesmente reorganiza a contagem sem introduzir erros adicionais.

---

## 5. Alinhamento do Motor com a Heurística

A nossa verificação empírica (Papers 10 e 11) mostra que, para $N\le10^8$, a fração de $C$ não cobertos após $k$ âncoras decai exponencialmente com taxa consistente com $\bar{\rho}(C)\approx 19/\log^2 C$, que é precisamente a densidade predita pela série singular (integrada sobre as âncoras). Além disso, a matriz de correlação entre as ativações das âncoras apresenta correlação média $<0{,}4\%$, confirmando a quase‑independência assumida no modelo de Poisson.

Esses resultados experimentais são **compatíveis** com a heurística de Hardy–Littlewood e **não revelam qualquer obstrução estrutural adicional** proveniente da geometria do motor.

---

## 6. Conclusão e ponte para a reformulação espectral

- A arquitetura do Motor de Herança é **consistente** com as densidades preditas pela teoria clássica.  
- O problema de Goldbach, quando traduzido na linguagem do motor, reduz‑se a uma única quantidade real: a componente de frequência zero $\widehat{F}(0)$ da função de colisão (Paper 08).  
- **O gargalo analítico permanece o mesmo:** controlar a contribuição dos arcos menores para garantir $\widehat{F}(0)>0$.  

Em vez de insistir em vias condicionais (como GRH), a série avança em duas direções originais:

1. **Descorrelação espectral incondicional** – via o teorema de Green–Tao–Ziegler (Paper 08), prova‑se que todas as componentes $\widehat{w}(j)$, $j\neq0$, tendem a zero. Isto isola a dificuldade na componente zero.
2. **Evidência empírica robusta** (Papers 10 e 11) – leis de escala, quase‑independência e decaimento exponencial do gap máximo, que corroboram a saturação geométrica do motor.

Convidamos os leitores a explorar essas frentes e a utilizarem a estrutura algébrica aqui apresentada como um **ambiente organizado** para futuras investigações analíticas sobre os arcos menores.

---

## Referências

[1] T. Bandeira, *Motor de Herança Estrutural: Formalização Algébrica da Fita‑Dobra e do Mecanismo de Promoção de Pares de Goldbach*, preprint (2026).  
[2] T. Bandeira, *Reformulação Espectral do Motor de Herança Estrutural*, preprint (2026).  
[3] T. Bandeira, *Leis de Escala e a Conjectura da Âncora Absoluta*, preprint (2026).  
[4] T. Bandeira, *Saturação Geométrica e Decaimento Exponencial do Gap*, preprint (2026).  
[5] H. Davenport, *Multiplicative Number Theory*, Springer, 2000.  
[6] H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS, 2004.

---

*Esta nota é um documento de trabalho. Comentários e sugestões são bem‑vindos.*
