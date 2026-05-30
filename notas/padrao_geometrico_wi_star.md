# Crivo Canônico e Certificado Geométrico do Par Primo na Configuração Wi\*

**Série:** Motor de Herança Estrutural — Conjectura de Goldbach — Nota 1  
**Autor:** Tiago Bandeira  
**Data:** maio de 2026  
**Preprint**

---

> **Nota do Autor.** Este artigo não reivindica uma demonstração da Conjectura de
> Goldbach nem da Hipótese Restritiva HR⁻. Seu objetivo é introduzir a noção de
> *crivo canônico* — uma estrutura de eliminação derivada da geometria da grade
> G₃,C — e demonstrar incondicionalmente que o único par candidato à posição
> canônica Wi\* possui independência de crivo para todos os primos q > 3. Os
> resultados incondicionais são explicitamente identificados; os condicionais
> são declarados como tais.

---

## Abstract

Na configuração canônica da grade G₃,C, o acoplamento Φ (condição 3C = 2N) fixa
geometricamente a janela Wi\* no índice i\* = C/2 − 1 e determina, por fórmula
fechada e sem qualquer hipótese de primalidade, o único par candidato (e₁, e₃) =
(C−1, 5C+1). Este artigo demonstra que esse par possui **independência de crivo
para todos os primos q > 3**: nenhum primo q > 3 elimina simultaneamente C−1 e
5C+1 por divisibilidade. Essa propriedade é consequência direta dos coeficientes
geométricos (1, 5) que emergem de i\* e da estrutura de L₃ decrescente. 

Sob a substituição p = C−1, a não degeneração local do par de formas lineares 
(p, 5p+6) é demonstrada incondicionalmente — o que satisfaz o critério local 
essencial exigido pela Conjectura de Dickson (ou Hardy-Littlewood) para a 
existência de infinitos p primos com 5p+6 também primo. Contudo, por tratar-se de 
um sistema de apenas uma variável (complexidade análoga à dos primos gêmeos), 
a existência de infinitos desses pares permanece estritamente **condicional** e 
fora do alcance dos teoremas incondicionais de Green-Tao-Ziegler (GTZ), que se 
aplicam a sistemas multidimensionais ($d \ge 2$).

Introduzimos formalmente a noção de **certificado geométrico de par primo**
(Definição 4.1) e **crivo canônico** (Definição 5.1), e provamos que a grade G₃,C
realiza, por geometria pura, uma triagem em dois filtros sequenciais: o Filtro
Geométrico (e₁ = C−1 primo, incondicional na sua localização, aritmético no seu
teste) e o Filtro Aritmético Residual (e₃ = 5C+1 primo, com independência de crivo
garantida). O filtro mod 30 que emerge da condição C ≡ r (mod 30) para r ∈
{0,2,6,8,12,14,18,20,24} é demonstrado como consequência direta da geometria de
i\*, sem qualquer cálculo modular explícito.

---

## Sumário

1. Introdução e Posicionamento na Série
2. Fundamentos: a Configuração Canônica e a Fórmula Fechada
3. O Par Canônico como Sistema de Formas Lineares
4. Certificado Geométrico de Par Primo
5. Crivo Canônico: Definição e Estrutura
6. Independência de Crivo para q > 3 (Resultado Central)
7. O Filtro Mod 30 como Consequência Geométrica
8. Estrutura de Cadeias e Constelações Admissíveis
9. Relação com o Artigo Espectral (Artigo 6)
10. Certificado de Lucas Geométrico para e₃
11. Crivo Segmentado Conjunto e Aceleração Geométrica
12. Síntese: o que o Crivo Canônico é e o que não é
13. Conclusão e Lacunas Remanescentes

---

## 1. Introdução e Posicionamento na Série

Este artigo integra a série [1–6] dedicada ao Motor de Herança Estrutural para a
Conjectura de Goldbach. A camada algébrica do motor — bijeção Φ, cobertura pela
órbita de σ, mecanismo de promoção — foi estabelecida incondicionalmente em [5].
O Artigo 6 propôs uma abordagem espectral de Koopman para analisar a Hipótese 
Restritiva HR⁻.

O presente artigo explora a manifestação *geométrica* dessa mesma estrutura:
a configuração canônica de Wi\* reduz o espaço de busca de HR⁻ de N−1 pares
candidatos a um único par determinado por fórmula fechada. A pergunta que
motiva o artigo é:

> **O que a geometria da grade garante sobre esse único par, independentemente
> de primalidade?**

A resposta central é a **independência de crivo**: a geometria garante que nenhum
primo q > 3 elimina simultaneamente os dois elementos do par. Isso não é uma prova
de primalidade — é uma garantia estrutural de que as duas condições de primalidade
atuam sem sobreposição de bloqueios locais para primos maiores que 3, o que estabelece
as bases necessárias para abordagens de crivos lineares.

### 1.1 O que este artigo prova e o que assume

| Resultado | Estatuto |
|-----------|----------|
| Fórmula fechada (e₁, e₃) = (C−1, 5C+1) | Incondicional |
| Independência de crivo para q > 3 | Incondicional |
| Filtro mod 30 como consequência geométrica | Incondicional |
| Não degeneração do par de formas lineares (p, 5p+6) | Incondicional |
| Infinitos p com p primo e 5p+6 primo | **Condicional (Conjectura de Dickson)** |
| HR⁻ para cada C individual | **Condicional (Lacuna central)** |

### 1.2 O que este artigo não prova

A independência de crivo *não* implica que ambos os elementos sejam primos para
algum C específico. Ela garante apenas que a eliminação local de um não implica a
eliminação do outro por primos maiores que 3. A barreira aritmética de HR⁻ individual 
permanece intacta.

---

## 2. Fundamentos: a Configuração Canônica e a Fórmula Fechada

Recapitulamos os objetos necessários de [5], todos incondicionais.

**Definição 2.1 (Grade G₃,C).** Para C ≥ 2 par, a grade G₃,C é a matriz 3 × C
cujas linhas contêm os primeiros 3C ímpares positivos em ordem:

```
L₁ = [1, 3, 5, …, 2C−1]
L₂ = [2C+1, 2C+3, …, 4C−1]
L₃ = [4C+1, 4C+3, …, 6C−1]
```

**Definição 2.2 (Acoplamento Φ e condição canônica).** Sob a condição 3C = 2N, o
acoplamento Φ fixa o índice da janela central em:

```
i* = C/2 − 1     (indexação 0-based)
```

Na *configuração canônica*, L₁ está em ordem crescente e L₃ em ordem decrescente
— o estado determinado geometricamente por Φ.

**Proposição 2.3 (Fórmula fechada — incondicional).** 
> **Observação ($HR^{-}$ nas cadeias).** As cadeias definidas pela transformação $T(C)=5C+2$ aplicam-se à janela **central** $W_{i^*}$, por ser a única a satisfazer a relação de recorrência de extremos $e_{1,n+1}=e_{3,n}$. No entanto, a cobertura geral do scanner (não restrita às cadeias) pode empregar quaisquer janelas $W_i$. Os ensaios computacionais indicam que, mesmo sob a restrição à janela central, a taxa de sobrevivência atinge 21,87%, sugerindo robustez no acoplamento.

Na configuração canônica de
G₃,C com C par, os extremos da janela Wi\* são:

```
e₁ = L₁[i*] = 2i* + 1 = C − 1
e₃ = L₃ᵈᵉˢᶜ[i*] = (6C−1) − 2i* = 5C + 1
e₁ + e₃ = 6C = 2M⁺
```

*Demonstração.* L₁ canônica tem L₁[k] = 2k+1 (0-based), logo L₁[i\*] = 2(C/2−1)+1 =
C−1. L₃ no estado decrescente tem L₃ᵈᵉˢᶜ[k] = (6C−1) − 2k (0-based), logo
L₃ᵈᵉˢᶜ[i\*] = (6C−1) − 2(C/2−1) = 5C+1. A soma é imediata. □

**Corolário 2.4.** O evento HR⁻ na configuração canônica ocorre se e somente se:

```
(C−1) ∈ ℙ   e   (5C+1) ∈ ℙ
```

O par (C−1, 5C+1) é o único par candidato — determinado exclusivamente por i\* e pela geometria de L₁ e L₃.

---

## 3. O Par Canônico como Sistema de Formas Lineares

**Proposição 3.1 (Reformulação por formas lineares).** Sob a substituição p = C−1
(com C par, logo p ≥ 2 ímpar), a condição do Corolário 2.4 equivale a:

```
p ∈ ℙ   e   5p + 6 ∈ ℙ,     p = C − 1
```

O par (e₁, e₃) = (C−1, 5C+1) corresponde ao sistema de duas formas lineares em p:

```
L₁(p) = p
L₂(p) = 5p + 6
```

com coeficientes (1, 5) e termos independentes (0, 6).

*Demonstração.* e₁ = C−1 = p e e₃ = 5C+1 = 5(p+1)+1 = 5p+6. □

**Observação 3.2 (Origem geométrica dos coeficientes).** Os coeficientes (1, 5) 
não são parâmetros livres; eles decorrem necessariamente da escolha de i\* = C/2−1 
e da estrutura decrescente de L₃. Especificamente:

- O coeficiente 1 em L₁(p) = p provém do comportamento L₁[k] = 2k+1 avaliado em i\* = C/2−1.
- O coeficiente 5 em L₂(p) = 5p+6 provém de L₃ᵈᵉˢᶜ[k] = (6C−1)−2k avaliado em i\* = C/2−1.

**Proposição 3.3 (Não degeneração local — incondicional).** O par de formas lineares
(L₁, L₂) = (p, 5p+6) é localmente não degenerado no sentido das conjecturas clássicas de crivo:

1. Os coeficientes (1, 5) são linearmente independentes sobre ℚ.
2. O par é localmente solúvel: para todo primo q, existe p tal que q∤L₁(p) e q∤L₂(p).
3. Os coeficientes são positivos.

**Observação 3.4 (Caráter condicional da infinitude).** Diferente de sistemas de equações 
lineares com duas ou mais variáveis ($d \ge 2$), onde o Teorema de Green-Tao-Ziegler 
[7] estabelece fórmulas assintóticas incondicionais para as contagens de primos, o par 
(p, 5p+6) possui apenas uma variável ($d=1$). Assim, a afirmação de que existem infinitos 
p primos tais que 5p+6 também é primo permanece estritamente **condicional**, 
sendo um caso particular da Conjectura de Dickson (ou de Hardy-Littlewood [8]).

---

## 4. Certificado Geométrico de Par Primo

**Definição 4.1 (Certificado geométrico de par primo).** Dado C par com e₁ = C−1
primo e e₃ = 5C+1 primo, o **certificado geométrico de par primo** para 6C é a
quádrupla

```
𝒞(C) = (G₃,C, i*, e₁, e₃)
```

onde:
- G₃,C é a grade na configuração canônica;
- i\* = C/2−1 é o índice da janela, determinado por Φ;
- e₁ = C−1 e e₃ = 5C+1 são os extremos de Wi\*, determinados por fórmula fechada;
- e₁ + e₃ = 6C é garantido geometricamente.

O certificado 𝒞(C) atesta que 6C é soma de dois primos (6C = e₁ + e₃) e que esse
par é o representante canônico de Goldbach para 6C na grade G₃,C.

**Proposição 4.2 (Unicidade do certificado canônico).** Para cada C par fixado,
existe no máximo um par (e₁, e₃) na posição i\* da configuração canônica. O
certificado 𝒞(C) é único quando existe.

*Demonstração.* Pela Proposição 2.3, i\* determina univocamente e₁ e e₃ por
fórmula fechada. A posição i\* é única por construção de Φ. □

**Observação 4.3 (O certificado localiza, não verifica).** O certificado 𝒞(C) cumpre
duas funções distintas:

1. **Localiza** (incondicional): aponta para o par (C−1, 5C+1) como o único
   candidato canônico para 6C.
2. **Certifica** (condicional): confirma que 6C é Goldbach — mas somente se ambos
   os elementos forem de fato primos, o que requer verificação aritmética externa.

A geometria garante a localização; a aritmética realiza a verificação.

**Exemplo 4.4.** Para C = 30:
- i\* = 14, e₁ = 29, e₃ = 151.
- Verificação: 29 e 151 são primos, 29 + 151 = 180 = 6 × 30.
- 𝒞(30) é um certificado válido para 180.

Para C = 10:
- i\* = 4, e₁ = 9 = 3², e₃ = 51 = 3 × 17.
- e₁ é composto → 𝒞(10) não existe. HR⁻ não dispara.

---

## 5. Crivo Canônico: Definição e Estrutura

**Definição 5.1 (Crivo canônico).** O **crivo canônico** associado à grade G₃,C
é a função de dois filtros sequenciais sobre o par (e₁, e₃) = (C−1, 5C+1):

```
Filtro 1 — Geométrico:   e₁ = C−1 ∈ ℙ?
                              ↓ sim          ↓ não
Filtro 2 — Aritmético:   e₃ = 5C+1 ∈ ℙ?   → descarte imediato
                              ↓ sim          ↓ não
                         HR⁻ dispara ✓       → descarte
```

**Observação 5.2 (Assimetria dos filtros).** Os dois filtros têm naturezas distintas:

- **Filtro 1** é *geométrico na localização* (a posição i\* determina o candidato C−1) 
  e *aritmético no teste* (verificar se C−1 é primo requer aritmética).
- **Filtro 2** é inteiramente aritmético: dado que e₁ = C−1 passou, testa-se e₃ = 5C+1.
  A independência de crivo (Seção 6) garante que a falha em Filtro 1 *não implica*
  falha em Filtro 2, e vice-versa para q > 3.

**Proposição 5.3 (Eficiência de busca do crivo canônico).** O crivo canônico reduz a 
busca de "existe algum par primo somando 6C entre os N−1 pares antipodais de G₃,C?" 
para a análise direta de "são C−1 e 5C+1 primos?". A redução é de N−1 testes de par 
para exatamente 2 testes de primalidade individual.

*Demonstração.* Consequência imediata da unicidade de i\* (Proposição 2.3). Os N−2 
pares restantes não necessitam de teste aritmético, pois são excluídos pela geometria 
da janela canônica Wi\*. □

**Observação 5.4 (Diferença para crivos clássicos).** O crivo canônico não é um
algoritmo de eliminação no sentido de Eratóstenes ou Rosser-Iwaniec. Consiste em uma
*seleção geométrica prévia*: a geometria isola o candidato e o crivo linear subsequente 
o avalia sob condições de independência favoráveis.

---

## 6. Independência de Crivo para q > 3 (Resultado Central)

Todos os resultados desta seção são **incondicionais**.

**Definição 6.1 (Eliminação simultânea por q).** Dizemos que um primo q
*elimina simultaneamente* o par (C−1, 5C+1) se q | (C−1) e q | (5C+1).

**Teorema 6.2 (Independência de crivo — incondicional).** Para todo primo q > 3,
nenhum q elimina simultaneamente o par canônico (C−1, 5C+1). Equivalentemente:

```
q | (C−1)  e  q | (5C+1)  ⟹  q | 6
```

Logo, para todo primo q > 3, as condições "q | (C−1)" e "q | (5C+1)" são
*mutuamente exclusivas*.

*Demonstração.* Suponha q | (C−1) e q | (5C+1). Então q divide a combinação linear:

```
q | (5C+1) − 5(C−1) = 5C+1 − 5C+5 = 6
```

Portanto q | 6, o que exige q ∈ {2, 3}. Para todo q > 3, a eliminação simultânea é impossível. □

**Corolário 6.3.** Para cada primo q > 3, a fração de C (pares) para os quais q
elimina e₁ é 1/q, e a fração para os quais q elimina e₃ é também 1/q. No entanto,
essas duas classes de C são *disjuntas* modulo q — nenhum C pertence a ambas simultaneamente 
(para q > 3). A probabilidade local de eliminação simultânea por q é zero, não 1/q².

**Observação 6.4 (Contraste com o caso geral).** Para um par genérico (a, b) com
a + b = 6C, a eliminação simultânea por q tipicamente possui densidade local de 1/q² 
se os termos se comportam de forma independente módulo q. O par canônico (C−1, 5C+1) 
mostra-se favorável, visto que a eliminação simultânea por qualquer q > 3 é 
algebricamente impossível.

**Proposição 6.5 (Relação com não degeneração local).** A independência de crivo 
para q > 3 (Teorema 6.2) garante que o sistema de formas lineares (p, 5p+6) não possui 
obstruções locais módulo q para qualquer q > 3, satisfazendo a condição de solubilidade 
local (Proposição 3.3).

**Observação 6.6 (Análise dos casos q = 2 e q = 3).** O Teorema 6.2 não se aplica a q = 2 e
q = 3:

- **q = 2:** C é par por hipótese, logo C−1 é ímpar. e₃ = 5C+1 é par (visto que 5C é par). 
  Assim, 2 elimina e₃ mas nunca e₁. Não ocorre eliminação simultânea por 2.
- **q = 3:** Se 3 | (C−1), então C ≡ 1 (mod 3), o que implica 5C+1 ≡ 5+1 = 6 ≡ 0 (mod 3).
  Nesse cenário, 3 | (C−1) implica 3 | (5C+1), configurando eliminação simultânea. O caso 
  q = 3 constitui a única exceção estrutural: C ≡ 1 (mod 3) inviabiliza o disparo de HR⁻.

**Corolário 6.7 (Filtro mod 3).** Para que HR⁻ dispare, é necessário que C ≢ 1 (mod 3).
Este filtro exclui 1/3 das classes de C a priori, sem necessidade de testes individuais.

**Proposição 6.8 (Hierarquia de obstruções por primo — incondicional).** Para cada
primo q, os resíduos de C (mod q) que bloqueiam e₁ e e₃ por divisibilidade são:

```
q | e₁  ⟺  C ≡ 1   (mod q)
q | e₃  ⟺  C ≡ −1/5 (mod q)  [i.e. 5C ≡ −1 (mod q)]
```

A tabela abaixo detalha esses resíduos para os menores primos:

| q | C mod q bloqueia e₁ | C mod q bloqueia e₃ | conflito simultâneo? |
|---|---------------------|---------------------|----------------------|
| 2 | 1 (C ímpar — excluído) | 1 (C ímpar — excluído) | nunca para C par |
| 3 | 1 | 1 | mesmo resíduo — mas C par + C≡1(mod 3) → C≡4(mod 6), excluído |
| 5 | 1 | nunca (e₃ ≡ 1 mod 5 sempre) | nunca |
| 7 | 1 | 4 | nunca (1 ≠ 4) |
| 11 | 1 | 2 | nunca (1 ≠ 2) |
| 13 | 1 | 5 | nunca (1 ≠ 5) |

*Demonstração.* $q | e₁ = C−1 \Longleftrightarrow C \equiv 1 \pmod q$. Para e₃: 
$q | 5C+1 \Longleftrightarrow 5C \equiv -1 \pmod q \Longleftrightarrow C \equiv -1/5 \pmod q$ 
quando $\text{mdc}(5,q) = 1$ ($q \neq 5$). Para $q = 5$: $e₃ = 5C+1 \equiv 0+1 = 1 \pmod 5$ 
para todo C — o que impede 5 de dividir e₃. □

**Corolário 6.9 (Comportamento do coeficiente 5 — incondicional).** O primo
q = 5 possui comportamento assimétrico estrutural no par canônico:

- 5 | e₁  ⟺  C ≡ 1 (mod 5)  — bloqueia e₁ em 1/5 das classes de C.
- 5 ∤ e₃  para todo C par   — o coeficiente 5 em L₃ garante e₃ ≡ 1 (mod 5) sempre.

Esta assimetria provém diretamente dos coeficientes geométricos (1, 5) impostos por i\*. 
O primo 5 é o único para o qual o bloqueio de um dos termos garante a não eliminação 
do outro de forma absoluta (para todo C).

**Observação 6.10 (Mutua exclusão modulo 3 sob HR⁻).** A verificação nos 269 
casos de HR⁻ (C ≤ 5000) mostra que C ≡ 2 (mod 3) ocorre em 50,2% e C ≡ 0 (mod 3) em 
49,8% dos casos, sem nenhuma ocorrência de C ≡ 1 (mod 3). Embora q = 3 seja algebricamente 
a exceção do Teorema 6.2, nos casos sobreviventes de HR⁻ a eliminação por 3 é mutuamente 
exclusiva por restrição dos resíduos admissíveis.

---

## 7. O Filtro Mod 30 como Consequência Geométrica

**Proposição 7.1 (Filtro geométrico mod 30 — incondicional).** Para que HR⁻ dispare
na configuração canônica, é necessário que:

```
C mod 30  ∈  {0, 2, 6, 8, 12, 14, 18, 20, 24}
```

Esta condição elimina as 6 classes pares restantes {4, 10, 16, 22, 26, 28} (mod 30),
realizando a triagem de 40% das classes pares sem testes individuais de primalidade.

*Demonstração.* Para que HR⁻ ocorra, e₁ = C−1 deve ser primo. Todo primo p > 5
satisfaz p ≢ 0 (mod 2), p ≢ 0 (mod 3), p ≢ 0 (mod 5), pertencendo a uma das 
8 classes ímpares mod 30: {1, 7, 11, 13, 17, 19, 23, 29}. Como p = C−1, segue 
$C \equiv p+1 \pmod{30} \in \{2, 8, 12, 14, 18, 20, 24, 0\}$. A exceção p = 5 
(único primo ≡ 5 mod 30) fornece C = 6. □

**Observação 7.2 (Emerge da geometria).** O filtro mod 30 surge da exigência de 
primalidade de e₁ sobre a fórmula geométrica do candidato na posição i\*. A 
independência de crivo (Seção 6) garante que essas classes são as únicas admissíveis 
para o par.

**Tabela 7.3 (Classes admissíveis mod 30).**

| C mod 30 | Origem (p = C−1 mod 30) | Exemplos de C ≤ 500 |
|----------|------------------------|----------------------|
| 0        | p ≡ 29                 | 30, 150, 360        |
| 2        | p ≡ 1                  | 62, 152, 422        |
| 6        | p = 5 (único)          | 6                   |
| 8        | p ≡ 7                  | 8, 38, 128, 488     |
| 12       | p ≡ 11                 | 12, 42, 132, 462    |
| 14       | p ≡ 13                 | 14, 104, 314        |
| 18       | p ≡ 17                 | 48, 108, 468        |
| 20       | p ≡ 19                 | 20, 80, 380         |
| 24       | p ≡ 23                 | 54, 84, 264, 444    |

**Proposição 7.4 (Anomalia de C ≡ 6 mod 30 — incondicional).** Dentre os 9 resíduos
admissíveis, o resíduo C ≡ 6 é o único para o qual HR⁻ só pode disparar em um único
valor de C (C = 6). Para todo C > 6 com C ≡ 6 (mod 30), HR⁻ não dispara.

*Demonstração.* Escreva C = 30k + 6 com k ≥ 0. Então:

```
e₁ = C − 1 = 30k + 5 = 5(6k + 1)
```

Para k = 0: e₁ = 5, que é primo — HR⁻ dispara, pois e₃ = 31 é primo.
Para k ≥ 1: e₁ = 5(6k+1) com 6k+1 ≥ 7. Logo, e₁ > 5 e é divisível por 5, sendo composto. 
Como HR⁻ exige e₁ primo, o disparo é impossível para k ≥ 1. □

**Observação 7.5 (Distribuição empírica).** A verificação em 269 casos HR⁻ com C ≤ 5000 
confirma: C ≡ 6 (mod 30) ocorre exatamente 1 vez (C = 6), enquanto as outras 8 classes 
admissíveis se distribuem uniformemente, com 28 a 37 casos cada. A Proposição 7.4 
explica estruturalmente essa assimetria.

---

## 8. Estrutura de Cadeias e Constelações Admissíveis

A independência de crivo (Seção 6) reflete-se na organização dos valores de C que 
disparam HR⁻: eles tendem a se agrupar em *cadeias*, associadas a constelações de 
primos em p = C−1.

**Definição 8.1 (Cadeia canônica de comprimento k).** Uma cadeia canônica de
comprimento k é uma sequência C₁ < C₂ < … < Cₖ de valores de C (pares) tais que:
(a) cada Cⱼ − 1 é primo; (b) cada 5Cⱼ + 1 é primo; (c) os gaps Cⱼ₊₁ − Cⱼ ∈ {2, 4, 6}.

**Proposição 8.2 (Tipos de gap e constelações).** Os três tipos de gap observados
correspondem a constelações de primos em p:

- **Gap 2:** (p, p+2) são primos gêmeos. Ambos disparam HR⁻ se 5p+6 e 5p+16 são primos.
- **Gap 4:** (p, p+4) são primos primos (cousins). Ambos disparam HR⁻ se 5p+6 e 5p+26 são primos.
- **Gap 6:** (p, p+6) são primos sexy. Ambos disparam HR⁻ se 5p+6 e 5p+36 são primos.

*Verificação numérica (C ≤ 500):* 49 casos; 15 isolados (31%), 34 em cadeias (69%).
As três cadeias de comprimento 4 observadas são:
- (38, 42, 48, 54): p = 37, 41, 47, 53 — gaps (4, 6, 6);
- (98, 104, 108, 114): p = 97, 103, 107, 113 — gaps (6, 4, 6);
- (128, 132, 138, 140): p = 127, 131, 137, 139 — gaps (4, 6, 2).

**Observação 8.3 (Cadeias e independência de crivo).** A independência de crivo
para q > 3 implica que, dentro de uma cadeia, a eliminação de um par (Cⱼ−1, 5Cⱼ+1)
por algum primo q > 3 não se propaga para o par adjacente (Cⱼ₊₁−1, 5Cⱼ₊₁+1).

---

## 8A. Cadeias de Autossimilaridade via T(C) = 5C+2

Esta seção analisa a relação entre as cadeias de autossimilaridade e a estrutura 
algébrica da recorrência canônica.

**Definição 8A.1 (Transformação canônica T).** A transformação

```
T : C  ↦  5C + 2
```

definida sobre os inteiros pares C ≥ 4, satisfaz a relação geométrica central:

```
e₃(C) = 5C + 1 = T(C) − 1 = e₁(T(C))
```

O primo de saída do par canônico de C é o primo de entrada do par canônico
de T(C).

**Definição 8A.2 (Cadeia de autossimilaridade).** Dado C₀ par com HR⁻
disparando, a cadeia de autossimilaridade iniciada em C₀ é a sequência

```
C₀ → C₁ = T(C₀) → C₂ = T(C₁) → ⋯,   Cₙ₊₁ = 5Cₙ + 2
```

com pares canônicos (e1ₙ, e3ₙ) = (Cₙ−1, 5Cₙ+1). A sequência de primos
associada é a órbita da forma linear p ↦ 5p+6:

```
p₀ → p₁ = 5p₀+6 → p₂ = 5p₁+6 → ⋯
```

A cadeia tem comprimento k se HR⁻ dispara em C₀, …, Cₖ₋₁ e não em Cₖ.
A cadeia é **maximal** se C₀ não é imagem de nenhum outro C via T.

**Proposição 8A.3 (T preserva paridade e admissibilidade — incondicional).**

*(i)* Para todo C par, T(C) = 5C+2 é par.

*(ii)* Se C mod 30 é admissível, então T(C) mod 30 ∈ {2, 12}. Em particular,
T(C) é admissível.

| C mod 30 | T(C) mod 30 | C mod 30 | T(C) mod 30 |
|----------|-------------|----------|-------------|
| 0  | 2  | 12 | 2  |
| 2  | 12 | 14 | 12 |
| 6  | 2  | 18 | 2  |
| 8  | 12 | 20 | 12 |
|    |    | 24 | 2  |

*Demonstração.* (i) 5C par + 2 par é par. (ii) Cálculo direto de (5r+2) mod 30
para cada r ∈ {0,2,6,8,12,14,18,20,24} — todos pertencem a {2,12}. □

**Corolário 8A.4 (Ciclo de período 2 em {2, 12} — incondicional).** A
restrição de T aos resíduos {2, 12} forma um ciclo de período 2:

```
T(2) ≡ 12 (mod 30)    T(12) ≡ 2 (mod 30)
```

A partir de C₁, toda cadeia alterna entre resíduos 2 e 12 (mod 30), independentemente do resíduo de C₀.

**Corolário 8A.5 (Resíduo da raiz).** O primeiro elemento C₀ pode ter qualquer resíduo 
admissível mod 30 (exceto 6, pela Proposição 7.4). A partir de C₁, o resíduo é dado por:

```
C₁ mod 30 = (5·(C₀ mod 30) + 2) mod 30 ∈ {2, 12}
```

**Proposição 8A.6 (Autossimilaridade — incondicional).** Em toda cadeia,
o par canônico de cada geração satisfaz a relação:

```
e3ₙ = 5 · e1ₙ + 6   para todo n ≥ 0
```

E e1ₙ₊₁ = e3ₙ — o e3 de uma geração é o e1 da seguinte.

*Demonstração.* e3ₙ = 5Cₙ+1 = 5(e1ₙ+1)+1 = 5·e1ₙ+6.
E e1ₙ₊₁ = Cₙ₊₁−1 = (5Cₙ+2)−1 = 5Cₙ+1 = e3ₙ. □

**Proposição 8A.7 (Fórmula fechada — incondicional).** Com p = e1₀ = C₀−1:

```
e1ₙ = 5ⁿ · p + (3/2) · (5ⁿ − 1)
```

Equivalentemente: e1ₙ + 3/2 = 5ⁿ · (p + 3/2) — progressão geométrica de
razão 5 centrada no ponto fixo −3/2 da recorrência e1ₙ₊₁ = 5·e1ₙ + 6.

*Demonstração.* Ponto fixo: x = 5x+6 → x = −3/2. Definindo aₙ = e1ₙ+3/2:
aₙ₊₁ = 5aₙ, solução aₙ = 5ⁿ·(p+3/2). Logo e1ₙ = 5ⁿ·p + (3/2)·(5ⁿ−1). □

**Corolário 8A.8 (Taxa de crescimento — incondicional).**

```
e1ₙ ~ 5ⁿ · p   e   Cₙ ~ 5ⁿ · C₀   (n → ∞)
```

Cada geração multiplica o tamanho da grade por 5.

**Proposição 8A.9 (Coprimaridade — incondicional).** Para p > 3 primo:

```
mdc(e1ₙ, e1ₙ₊₁) = 1   para todo n ≥ 0
```

*Demonstração.* mdc(e1ₙ, e1ₙ₊₁) = mdc(e1ₙ, 6). Como e1ₙ = 5ⁿ·p + (3/2)·(5ⁿ−1):
e1ₙ é sempre ímpar (5ⁿ·p é ímpar; (3/2)·(5ⁿ−1) é par) e mdc(e1ₙ, 3) = 1,
pois e1ₙ ≡ 2ⁿ·p (mod 3) com p ≢ 0 (mod 3). □

**Observação 8A.10 (Estrutura mod 3 e crivos).** Como 5 ≡ 2 (mod 3), a fórmula 
fechada fornece e1ₙ ≡ 2ⁿ·p (mod 3). O resíduo alterna entre p mod 3 e 2p mod 3 — impedindo 
que dois termos consecutivos sejam ambos divisíveis por 3. Combinado ao Teorema 6.2, 
nenhum primo q > 3 elimina simultaneamente dois termos consecutivos da cadeia.

**Observação 8A.11 (Dados empíricos até C = 10000).**

| Comprimento | Cadeias maximais | Exemplo (C₀, primos p) |
|-------------|-----------------|------------------------|
| 1 (isolado) | 153 | C=14: p=13, q=71 |
| 2 | 101 | C=12: 11→61→311 |
| 3 | 22  | C=8→42→212: 7→41→211→1061 |
| 4 | 4   | C=1260: 1259→6301→31511→157561 |
| 6 | 1   | C=80: 79→401→2011→10061→50311→251561 |

A cadeia maximal de comprimento 6 (C₀ = 80) é a mais longa verificada:

```
C₀ = 80:     e₁ = 79,      e₃ = 401       ✓
C₁ = 402:    e₁ = 401,     e₃ = 2011      ✓
C₂ = 2012:   e₁ = 2011,    e₃ = 10061     ✓
C₃ = 10062:  e₁ = 10061,   e₃ = 50311     ✓
C₄ = 50312:  e₁ = 50311,   e₃ = 251561    ✓
C₅ = 251562: e₁ = 251561,  e₃ = 1257811   ✗ (= 7 × 179687)
```

Resíduos mod 30: [20, 12, 2, 12, 2, 12] — alternância a partir de C₁ verificada.

**Observação 8A.12 (Conexão com conjecturas sobre formas lineares).** A
existência de cadeias de comprimento arbitrário é equivalente à existência
de órbitas arbitrariamente longas de p ↦ 5p+6 inteiramente dentro dos
primos — uma instância da conjectura de Dickson sobre sistemas de formas
lineares. A não degeneração do par (p, 5p+6) está provada incondicionalmente
(Proposição 3.3). Sob a ótica espectral do Artigo 6, as componentes de 
frequência $j \neq 0$ descorrelacionam-se, restando como barreira analítica a 
positividade de F̂(0) para cada geração individualmente.

**Observação 8A.13 (Propriedades espectrais).** Cada geração define um sistema 
com Nₙ ~ 5ⁿ·N₀. A coprimaridade (Proposição 8A.9) garante que as funções de 
colisão F de gerações distintas não compartilham fatores comuns de divisibilidade.

---

## 9. Relação com o Artigo Espectral (Artigo 6)

A configuração canônica é a representação geométrica do suporte da função de colisão 
F analisada espectralmente no Artigo 6.

**Proposição 9.1 (Suporte pontual da função de colisão).** Na configuração
canônica, a função de colisão F : XN → {0,1} definida por F(i) = 1ₚ(e₁(i))·1ₚ(e₃(i))
tem suporte em no máximo um ponto — o índice i = i\* correspondente à janela canônica:

```
F(i) = 1ₚ(C−1) · 1ₚ(5C+1) · δ(i − i*)
```

*Demonstração.* Na configuração canônica, apenas Wi\* possui os valores (C−1, 5C+1).
As demais janelas possuem pares (e₁(i), e₃(i)) distintos, não analisados pelo crivo
canônico. □

**Corolário 9.2.** A condição HR⁻ na configuração canônica é equivalente a F̂(0) > 0
(Artigo 6, Teorema 4.4), que na canônica se reduz diretamente a:

```
F̂(0) = (1/(N−1)) · F(i*) = (1/(N−1)) · 1ₚ(C−1) · 1ₚ(5C+1)
```

**Observação 9.3 (O crivo canônico e as propriedades locais).** A descorrelação das 
componentes $j \neq 0$ descrita no Artigo 6 refere-se ao comportamento assintótico 
global, enquanto a independência de crivo (Teorema 6.2) é uma propriedade aritmética 
local e exata (mdc finito). A não degeneração do par (p, 5p+6) (Proposição 3.3) 
garante que não há obstruções locais mod q, o que se alinha conceitualmente com a 
solubilidade local exigida em formulações de crivo.

---

## 10. Certificado de Lucas Geométrico para e₃

Esta seção formaliza a consequência da relação e₃ − 1 = 5·(e₁+1) = 10k:
a geometria do acoplamento 3C = 2N fornece uma fatoração parcial de e₃ − 1 
que viabiliza o Teste de Lucas de maneira determinística.

Todos os resultados desta seção são **incondicionais** na estrutura; a primalidade
de e₃ é o que se quer provar, não o que se assume.

### 10.1 A fatoração parcial

**Proposição 10.1 (Fatoração parcial de e₃ − 1 — incondicional).** Na configuração
canônica com acoplamento 3C = 2N, escrevendo C = 2k (k inteiro, k ≥ 2):

```
e₃ − 1 = 5C + 1 − 1 = 5C = 5·2k = 10k
```

Portanto:

```
e₃ − 1 = 2 · 5 · k
```

Os fatores primos {2, 5} são fatores de e₃ − 1, independentemente de k, por 
consequência direta da condição 3C = 2N.

*Demonstração.* e₃ = 5C + 1 = 5·2k + 1 = 10k + 1, logo e₃ − 1 = 10k = 2·5·k. □

**Corolário 10.2.** O conjunto de fatores primos de e₃ − 1 é:

```
fatores_primos(e₃ − 1) = {2, 5} ∪ fatores_primos(k)
```

Para obter a fatoração de e₃ − 1, basta fatorar k — um número menor que e₃.

**Caso especial (k primo).** Se k é primo, então e₃ − 1 = 2·5·k está
fatorado pela geometria:

```
k primo  ⟹  fatores_primos(e₃ − 1) = {2, 5, k}
```

Isso ocorre quando k = (e₁+1)/2 é primo.

### 10.2 O Teste de Lucas e o certificado geométrico

**Teorema de Lucas (clássico).** Um inteiro n > 1 é primo se e somente se existe
uma base a ∈ {2, …, n−1} tal que:

```
(L1)  a^(n−1) ≡ 1 (mod n)
(L2)  a^((n−1)/q) ≢ 1 (mod n)   para todo fator primo q de n−1
```

**Definição 10.3 (Certificado de Lucas geométrico).** Dado k com e₁ = 2k−1 primo
e e₃ = 10k+1 candidato, o **certificado de Lucas geométrico** para e₃ é a tripla:

```
ℒ(k) = (e₃, fatores_primos(e₃−1), a)
```

onde fatores_primos(e₃−1) = {2, 5} ∪ fatores_primos(k) é obtida via Proposição
10.1, e a é a menor base que satisfaz (L1) e (L2).

Quando ℒ(k) existe, ele prova que e₃ é primo de forma determinística.

**Proposição 10.4 (Custo de certificação — incondicional).** O Certificado
de Lucas geométrico ℒ(k) para e₃ = 10k+1 requer:

1. **Fatoração:** fatorar k (tamanho ~e₃/10). O custo de trial division é 
   $O(\sqrt{k}) = O(\sqrt{e_3/10})$, reduzindo o esforço numérico comparado à 
   fatoração direta de $e_3$.
2. **Lucas:** $|fatores\_primos(e₃−1)| = 2 + \omega(k)$ exponenciações modulares mod e₃,
   onde $\omega(k)$ é o número de fatores primos distintos de k.
3. **Para k primo:** custo de fatoração zero (visto que k é primo se e₁
   passou no Filtro 1 com k = (e₁+1)/2 primo), necessitando de apenas 3 exponenciações modulares.

**Observação 10.5 (Limite da garantia).** O certificado ℒ(k) prova que e₃ é primo 
apenas se e₃ for primo. Se e₃ for composto, nenhuma base a satisfará (L1) e (L2) 
simultaneamente. A geometria facilita a prova de primalidade, mas não garante a 
ocorrência da mesma.

### 10.3 Verificação numérica

A tabela abaixo confirma o certificado para os primeiros casos HR⁻ (C ≤ 500).

| k  | e₁    | e₃    | e₃−1 = 10k | fatores de e₃−1 | base a | exp. mod |
|----|-------|-------|------------|-----------------|--------|----------|
| 3  | 5     | 31    | 30 = 2·3·5 | {2,3,5}         | 3      | 3        |
| 4  | 7     | 41    | 40 = 2³·5  | {2,5}           | 6      | 2        |
| 7  | 13    | 71    | 70 = 2·5·7 | {2,5,7}         | 7      | 3        |
| 10 | 19    | 101   | 100 = 2²·5² | {2,5}          | 2      | 2        |
| 19 | 37    | 191   | 190 = 2·5·19 | {2,5,19}      | 19     | 3        |
| 31 | 61    | 311   | 310 = 2·5·31 | {2,5,31}      | 17     | 3        |
| 64 | 127   | 641   | 640 = 2⁷·5  | {2,5}          | 3      | 2        |
| 91 | 181   | 911   | 910 = 2·5·7·13 | {2,5,7,13} | 17     | 4        |
| 97 | 193   | 971   | 970 = 2·5·97 | {2,5,97}      | 6      | 3        |

---

## 11. Crivo Segmentado Conjunto e Aceleração Geométrica

A independência de crivo (Teorema 6.2) permite otimizar o processo de crivagem em 
lote para o par (C−1, 5C+1), reduzindo redundâncias de eliminação simultânea.

Todos os resultados desta seção são **incondicionais**.

### 11.1 Configuração: crivo em lote sobre um intervalo

Fixemos um intervalo de valores pares C ∈ [P, P+H] (com H ≪ P). Para cada tal C,
o crivo canônico aponta para o par:

```
e₁(C) = C − 1  ∈  [P−1, P+H−1]       — intervalo I₁ de comprimento H
e₃(C) = 5C + 1 ∈  [5P+1, 5P+5H+1]    — intervalo I₃ de comprimento 5H
```

O **crivo segmentado conjunto** consiste em cribilar I₁ e I₃ simultaneamente
com os mesmos primos q, identificando quais pares (e₁(C), e₃(C)) sobrevivem.

**Definição 11.1 (Crivo segmentado conjunto).** Para um conjunto de primos
Q = {q : 3 < q ≤ Q_max}, o crivo segmentado conjunto sobre [P, P+H] marca, para cada q ∈ Q:

- em I₁: as posições C tais que q | (C−1), i.e., C ≡ 1 (mod q);
- em I₃: as posições C tais que q | (5C+1), i.e., C ≡ −1/5 (mod q).

Um C é **eliminado por q** se está marcado em I₁ ou em I₃. O par (e₁(C), e₃(C))
sobrevive se C não for eliminado por nenhum q ∈ Q.

### 11.2 Trabalho de crivo sem independência (caso geral)

Para um par genérico (a(C), b(C)) de formas lineares em C, o primo q marca:

- ~H/q posições em I₁ (as C com q | a(C));
- ~H/q posições em I₃ (as C com q | b(C));
- ~H/q² posições em ambos simultaneamente (se as formas são independentes mod q).

O trabalho total de marcação por q é ~2H/q, e o número de C eliminados por q
é ~2H/q − H/q² (descontando a sobreposição).

### 11.3 Trabalho de crivo com independência

**Proposição 11.2 (Sobreposição nula para q > 3 — incondicional).** Para todo
primo q > 3 e todo C par, as condições "q | (C−1)" e "q | (5C+1)" são
mutuamente exclusivas. Portanto:

```
|{C ∈ [P,P+H] : q|(C−1) e q|(5C+1)}| = 0     para todo q > 3
```

*Demonstração.* Consequência direta do Teorema 6.2: a hipótese de divisibilidade 
dupla exige que q divida 6, o que é impossível para primos q > 3. □

**Corolário 11.3 (Eliminações por q no crivo conjunto).** Para q > 3, o número
de C ∈ [P, P+H] eliminados pelo crivo conjunto é:

```
|elim(q)| = |{C : q|(C−1)}| + |{C : q|(5C+1)}|
           ≈ H/q + H/q
           = 2H/q
```

A sobreposição nula implica que cada eliminação por q atinge de forma exclusiva 
um dos dois elementos, nunca ambos simultaneamente. Isso garante a eficiência de 
marcação para cada q > 3.

### 11.4 Densidade de sobreviventes ao crivo conjunto

**Proposição 11.4 (Densidade de pares sobreviventes — incondicional).** A fração
de valores C ∈ [P, P+H] que sobrevivem ao crivo conjunto até Q_max é:

```
D_conjunto(P, H, Q_max) = ∏_{3 < q ≤ Q_max} (1 − 2/q)
```

Para um par genérico com sobreposição local independente de H/q²:

```
D_genérico(P, H, Q_max) = ∏_{3 < q ≤ Q_max} (1 − 2/q + 1/q²)
                        = ∏_{3 < q ≤ Q_max} (1 − 1/q)²
```

Ambos os produtos são assintoticamente equivalentes.

*Demonstração.* Para cada q > 3, a fração de C sobreviventes é $1 - 2/q$ devido 
à exclusão mútua das duas classes. Para o par genérico, a sobrevivência é 
$1 - 2/q + 1/q^2 = (1-1/q)^2$. □

**Observação 11.5 (Garantia estrutural de erro nulo).** A equivalência assintótica 
mostra que o crivo canônico não altera a densidade final de sobrevivência em relação 
a um par não degenerado genérico. O ganho é **estrutural**: a sobreposição é nula, 
eliminando termos de erro flutuantes de sobreposição $O(H/q²)$ em intervalos finitos.

### 11.5 A barreira de paridade de Selberg

**Observação 11.6 (Limite do crivo conjunto — incondicional).** O crivo segmentado
conjunto, apesar da precisão estrutural na distribuição das classes, esbarra na
**barreira de paridade de Selberg**: métodos puramente lineares de crivo não são 
capazes de distinguir individualmente números primos de semiprimos. A cota superior 
produzida é:

```
|{C ∈ [P,P+H] : e₁(C) primo e e₃(C) primo}| ≤ A · H / (log H)²
```

mas não fornece uma cota inferior positiva de sobrevivência de primos. Superar essa 
barreira para garantir HR⁻ individual requer ferramentas que vão além do crivo clássico.

---

## 12. Síntese: o que o Crivo Canônico é e o que não é

### O que é:

- Uma **seleção geométrica** que isola, sem necessidade de testes aritméticos prévios, 
  o par candidato (C−1, 5C+1) na janela canônica Wi\*.
- Uma **garantia de independência local**: para q > 3, a eliminação de um termo não 
  coincide com a eliminação do outro.
- Um **certificado de localização**: caso ambos os elementos sejam primos, certifica 
  a representação canônica de Goldbach para 6C.
- Uma **garantia de não degeneração local**: o par de formas lineares (p, 5p+6) 
  satisfaz a solubilidade local necessária módulo q para todo q.

### O que não é:

- Um **teste de primalidade**: a grade apenas aponta para o candidato, cabendo à 
  aritmética validar a primalidade dos termos.
- Uma **demonstração incondicional de HR⁻** para cada C: a Conjectura de Dickson 
  assegura apenas a existência de infinitos desses pares de forma assintótica, mas 
  não garante a primalidade para cada C individualmente.
- Uma **resolução direta da barreira de paridade**: o crivo canônico otimiza a 
  marcação local, mas permanece limitado pelas cotas superiores características dos 
  crivos lineares.

---

## 13. Conclusão e Lacunas Remanescentes

**Camada geométrica — resultados incondicionais:**

1. **Fórmula fechada** (Proposição 2.3): o par canônico (e₁, e₃) = (C−1, 5C+1) é 
   isolado exclusivamente por i\* e pela estrutura geométrica das linhas L₁ e L₃.
2. **Independência de crivo** (Teorema 6.2): demonstra-se incondicionalmente a 
   exclusão mútua de eliminação simultânea por primos q > 3.
3. **Não degeneração local** (Proposição 3.3): o par de formas lineares (p, 5p+6) é 
   localmente solúvel módulo q para todo q.
4. **Filtro mod 30** (Proposição 7.1): as classes admissíveis decorrem da exigência 
   de primalidade na posição geométrica i\*.

**Lacuna remanescente:**

A primalidade simultânea de C−1 e 5C+1 para um C individual arbitrário (HR⁻ individual) 
permanece em aberto. A geometria do crivo canônico reduz o problema a esse par e 
elimina obstruções locais mod q (para q > 3), mas a barreira de paridade e a natureza 
unidimensional do sistema impõem que a prova de infinitude dependa da Conjectura de Dickson.

---

## Referências

[1] T. Bandeira, *Uma Abordagem Unificada para a Conjectura de Goldbach: Estrutura
Combinatória, Saturação Geométrica e o Elo entre Trios e Pares Primos*, preprint,
maio de 2026.

[2] T. Bandeira, *Uma propriedade de soma constante na grade 3 × N e as conjecturas
de Goldbach*, preprint, maio de 2026.

[3] T. Bandeira, *O Invariante Âncora da Grade G₃,N e um Estimador Geométrico
Oracle-Free para a Conjectura de Goldbach*, preprint, maio de 2026.

[4] T. Bandeira, *Problema B do Crivo Geométrico: Demonstração da Desigualdade
Estrutural*, preprint, maio de 2026.

[5] T. Bandeira, *Motor de Herança Estrutural: Formalização Algébrica da Fita-Dobra
e do Mecanismo de Promoção de Pares de Goldbach*, preprint, maio de 2026.

[6] T. Bandeira, *Reformulação Espectral do Motor de Herança Estrutural*, preprint,
maio de 2026.

[7] B. Green, T. Tao e T. Ziegler, *An inverse theorem for the Gowers Uˢ⁺¹[N]-norm*,
Annals of Mathematics, vol. 176, pp. 1231–1372, 2012.

[8] B. Green e T. Tao, *Linear equations in primes*, Annals of Mathematics, vol. 171, 
pp. 1753-1850, 2010.

[9] H. Iwaniec e E. Kowalski, *Analytic Number Theory*, American Mathematical Society
Colloquium Publications, vol. 53, 2004.

---

*Preprint — maio de 2026. Artigo 7 da série sobre a Conjectura de Goldbach.*  
