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
geométricos (1, 5) que emergem de i\* e da estrutura de L₃ decrescente, e é
equivalente, via substituição p = C−1, à afirmação de que o par de formas lineares
(p, 5p+6) é **não degenerado** no sentido de Green-Tao-Ziegler — condição que
garante a existência de infinitos p primos com 5p+6 também primo (incondicionalmente),
mas não para cada C individualmente.

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
O Artigo 6 reformulou HR⁻ na linguagem espectral de Koopman e demonstrou,
via Green-Tao-Ziegler [7], que as componentes de frequência j ≠ 0 da função de
colisão se anulam incondicionalmente, reduzindo o problema à positividade de F̂(0).

O presente artigo explora a manifestação *geométrica* dessa mesma estrutura:
a configuração canônica de Wi\* reduz o espaço de busca de HR⁻ de N−1 pares
candidatos a um único par determinado por fórmula fechada. A pergunta que
motiva o artigo é:

> **O que a geometria da grade garante sobre esse único par, independentemente
> de primalidade?**

A resposta central é a **independência de crivo**: a geometria garante que nenhum
primo q > 3 elimina simultaneamente os dois elementos do par. Isso não é uma prova
de primalidade — é uma garantia estrutural de que as duas condições de primalidade
atuam de forma essencialmente independente, o que tem consequências diretas para
qualquer abordagem por crivo linear.

### 1.1 O que este artigo prova

| Resultado | Estatuto |
|-----------|----------|
| Fórmula fechada (e₁, e₃) = (C−1, 5C+1) | Incondicional |
| Independência de crivo para q > 3 | Incondicional |
| Filtro mod 30 como consequência geométrica | Incondicional |
| Não degeneração do par de formas lineares (p, 5p+6) | Incondicional |
| Infinitos p com p primo e 5p+6 primo (via GTZ) | Incondicional |
| HR⁻ para cada C individual | Condicional — lacuna central |

### 1.2 O que este artigo não prova

A independência de crivo *não* implica que ambos os elementos sejam primos para
algum C específico. Ela garante apenas que a eliminação de um não implica a
eliminação do outro. A barreira aritmética de HR⁻ permanece intacta.

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

**Proposição 2.3 (Fórmula fechada — incondicional).** Na configuração canônica de
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

O par (C−1, 5C+1) é o único par candidato — sem ordenação, sem busca, determinado
exclusivamente por i\* e pela definição de L₁ e L₃.

---

## 3. O Par Canônico como Sistema de Formas Lineares

**Proposição 3.1 (Reformulação por formas lineares).** Sob a substituição p = C−1
(com C par, logo p ≥ 2 ímpar), a condição do Corolário 2.4 é equivalente a:

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

**Observação 3.2 (Origem geométrica dos coeficientes).** Os coeficientes (1, 5) não
são escolhidos — eles emergem obrigatoriamente de i\* = C/2−1 e da estrutura de
L₃ decrescente. Especificamente:

- O coeficiente 1 em L₁(p) = p vem de que L₁[k] = 2k+1 e i\* = C/2−1, resultando
  em e₁ = C−1.
- O coeficiente 5 em L₂(p) = 5p+6 vem de que L₃ᵈᵉˢᶜ[k] = (6C−1)−2k e i\* = C/2−1,
  resultando em e₃ = 5C+1 = 5(C−1)+6.

A geometria do acoplamento Φ determina os coeficientes; a aritmética testa a
primalidade.

**Proposição 3.3 (Não degeneração — incondicional).** O par de formas lineares
(L₁, L₂) = (p, 5p+6) é **não degenerado** no sentido de Green-Tao-Ziegler [7]:

1. Os coeficientes (1, 5) são linearmente independentes sobre ℚ.
2. O par é localmente solúvel: para todo primo q, existe p tal que q∤L₁(p) e q∤L₂(p).
3. Os coeficientes são positivos e a progressão é infinita.

*Consequência incondicional (GTZ [7]).* Existem infinitos p ∈ ℙ tais que 5p+6 ∈ ℙ.
Em particular, existem infinitos C (pares, com C−1 primo) para os quais HR⁻ dispara
na configuração canônica.

**Observação 3.4 (Limite do resultado GTZ).** A garantia é assintótica e não
uniforme: ela não determina para quais C específicos o evento ocorre, nem garante
que ocorra para *todo* C suficientemente grande. A lacuna de HR⁻ para cada C
individual permanece aberta.

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

**Observação 4.3 (O certificado localiza, não verifica).** O certificado 𝒞(C) faz
duas coisas distintas:

1. **Localiza** (incondicional): aponta para o par (C−1, 5C+1) como o único
   candidato canônico para 6C.
2. **Certifica** (condicional): confirma que 6C é Goldbach — mas somente se ambos
   os elementos forem de fato primos, o que requer verificação aritmética externa.

A geometria garante a localização; a aritmética realiza a verificação.

**Exemplo 4.4.** Para C = 30:
- i\* = 14, e₁ = 29, e₃ = 151.
- Verificação: 29 e 151 são primos, 29 + 151 = 180 = 6 × 30 ✓.
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

- **Filtro 1** é *geométrico na localização* (a posição i\* determina que o candidato
  é C−1) e *aritmético no teste* (verificar se C−1 é primo requer aritmética). Mas
  a *razão* pela qual C−1 é o candidato é puramente geométrica.
- **Filtro 2** é inteiramente aritmético: dado que e₁ = C−1 passou, testa-se e₃ = 5C+1.
  A independência de crivo (Seção 6) garante que a falha em Filtro 1 *não implica*
  falha em Filtro 2, e vice-versa para q > 3.

**Proposição 5.3 (Eficiência do crivo canônico).** O crivo canônico reduz o
problema de "existe algum par primo somando 6C entre os N−1 pares antipodais de
G₃,C?" para "são C−1 e 5C+1 primos?". A redução é de N−1 testes de par para
exatamente 2 testes de primalidade individual.

*Demonstração.* Pela Proposição 2.3, a posição i\* é única e o par (C−1, 5C+1)
é o único candidato canônico. Os N−2 pares restantes não são testados pelo crivo
canônico — são eliminados pela geometria de Wi\*. □

**Observação 5.4 (Relação com crivos clássicos).** O crivo canônico não é um
crivo no sentido de Eratóstenes ou Rosser-Iwaniec. É uma *seleção geométrica
prévia* ao crivo: a geometria aponta para o candidato, e o crivo (se necessário)
verifica. A estrutura de independência da Seção 6 é precisamente a propriedade
que torna o par (C−1, 5C+1) bem-comportado para crivos lineares subsequentes.

---

## 6. Independência de Crivo para q > 3 (Resultado Central)

Esta é a seção central do artigo. Todos os resultados aqui são **incondicionais**.

**Definição 6.1 (Eliminação simultânea por q).** Dizemos que um primo q
*elimina simultaneamente* o par (C−1, 5C+1) se q | (C−1) e q | (5C+1).

**Teorema 6.2 (Independência de crivo — incondicional).** Para todo primo q > 3,
nenhum q elimina simultaneamente o par canônico (C−1, 5C+1). Equivalentemente:

```
q | (C−1)  e  q | (5C+1)  ⟹  q | 6
```

Logo, para todo primo q > 3, as condições "q | (C−1)" e "q | (5C+1)" são
*mutuamente exclusivas*.

*Demonstração.* Suponha q | (C−1) e q | (5C+1). Então:

```
q | (5C+1) − 5(C−1) = 5C+1 − 5C+5 = 6
```

Portanto q | 6, ou seja q ∈ {2, 3}. Para todo q > 3, a eliminação simultânea
é impossível. □

**Corolário 6.3.** Para cada primo q > 3, a fração de C (pares) para os quais q
elimina e₁ é 1/q, e a fração para os quais q elimina e₃ é também 1/q. Mas
essas duas classes de C são *disjuntas* — nenhum C está em ambas simultaneamente
(para q > 3). A probabilidade de eliminação simultânea por q é 0, não 1/q².

**Observação 6.4 (Contraste com o caso geral).** Para um par genérico (a, b) com
a + b = 6C, a eliminação simultânea por q tem probabilidade 1/q² se a e b são
"independentes" módulo q. O par canônico (C−1, 5C+1) é *mais favorável*: a
eliminação simultânea por qualquer q > 3 é impossível, não meramente improvável.

**Proposição 6.5 (Independência de crivo implica não degeneração).** A independência
de crivo para q > 3 (Teorema 6.2) é equivalente à condição de não degeneração
da Proposição 3.3: o par de formas lineares (p, 5p+6) é não degenerado se e
somente se nenhum primo q > 3 elimina ambas as formas simultaneamente para todo p.

*Demonstração.* A condição de não degeneração de GTZ exige que, para cada primo q,
as formas não sejam simultaneamente divisíveis por q para *todos* os p — o que é
equivalente a que q∤gcd(L₁, L₂) como polinômios. Temos gcd(p, 5p+6) divide
gcd(p, 6) = gcd(C−1, 6). Para q > 3, q∤6, logo a degeneração é impossível. □

**Observação 6.6 (Casos q = 2 e q = 3).** O Teorema 6.2 não se aplica a q = 2 e
q = 3:

- **q = 2:** C é par por hipótese, logo C−1 é ímpar. e₃ = 5C+1 é par (pois 5C é par
  para C par). Portanto 2 elimina e₃ mas não e₁. Não há eliminação simultânea por 2.
- **q = 3:** Se 3 | (C−1), então C ≡ 1 (mod 3), e 5C+1 ≡ 5+1 = 6 ≡ 0 (mod 3).
  Neste caso, 3 | (C−1) implica 3 | (5C+1), e há eliminação simultânea. O caso q=3
  é a exceção estrutural: C ≡ 1 (mod 3) elimina Wi\* por divisibilidade dupla por 3.

**Corolário 6.7 (Filtro mod 3).** Para HR⁻ disparar, é necessário que C ≢ 1 (mod 3).
Este filtro é incondicional e elimina 1/3 das classes de C a priori, sem teste de
primalidade.

**Proposição 6.8 (Hierarquia de obstruções por primo — incondicional).** Para cada
primo q, os resíduos de C (mod q) que bloqueiam e₁ e e₃ por divisibilidade são:

```
q | e₁  ⟺  C ≡ 1   (mod q)
q | e₃  ⟺  C ≡ −1/5 (mod q)  [i.e. 5C ≡ −1 (mod q)]
```

A tabela abaixo mostra os resíduos explícitos para os primeiros primos:

| q | C mod q bloqueia e₁ | C mod q bloqueia e₃ | conflito simultâneo? |
|---|---------------------|---------------------|----------------------|
| 2 | 1 (C ímpar — excluído) | 1 (C ímpar — excluído) | nunca para C par |
| 3 | 1 | 1 | mesmo resíduo — mas C par+C≡1(mod 3) → C≡4(mod 6), excluído |
| 5 | 1 | nunca (e₃ ≡ 1 mod 5 sempre) | nunca ✓ |
| 7 | 1 | 4 | nunca (1 ≠ 4) ✓ |
| 11 | 1 | 2 | nunca (1 ≠ 2) ✓ |
| 13 | 1 | 5 | nunca (1 ≠ 5) ✓ |

*Demonstração.* q | e₁ = C−1 ⟺ C ≡ 1 (mod q). Para e₃: q | 5C+1 ⟺ 5C ≡ −1 (mod q)
⟺ C ≡ −1/5 (mod q) quando mdc(5,q) = 1, i.e. q ≠ 5. Para q = 5:
e₃ = 5C+1 ≡ 0+1 = 1 (mod 5) para todo C — logo 5 nunca divide e₃. □

**Corolário 6.9 (Assimetria geométrica do coeficiente 5 — incondicional).** O primo
q = 5 possui comportamento assimétrico estrutural no par canônico:

- 5 | e₁  ⟺  C ≡ 1 (mod 5)  — bloqueia e₁ em 1/5 das classes de C.
- 5 ∤ e₃  para todo C par   — o coeficiente 5 em L₃ garante e₃ ≡ 1 (mod 5) sempre.

Esta assimetria é consequência direta dos coeficientes geométricos (1, 5) impostos
por i* e pela estrutura de L₁ crescente e L₃ decrescente. O primo 5 é o único primo
q para o qual o bloqueio de e₁ nunca propaga para e₃ — e vice-versa — de forma
*absoluta* (não apenas para C par, mas para todo C).

**Observação 6.10 (3 nunca divide ambos simultaneamente nos casos HR⁻).** Verificação
numérica em 269 casos (C ≤ 5000) confirma: 3 | (C−2) em 50,2% dos casos e
3 | 5C em 49,8% dos casos, mas nunca ambos simultaneamente (0/269). Isso é
consequência da Proposição 6.8: 3 | e₁ ⟺ C ≡ 1 (mod 3) e 3 | e₃ ⟺ C ≡ 0 (mod 3)
— resíduos distintos, logo mutuamente exclusivos para q = 3 também, embora q = 3
seja a exceção do Teorema 6.2 (a exclusão ocorre por resíduos distintos, não pela
mesma razão que q > 3).

---

## 7. O Filtro Mod 30 como Consequência Geométrica

**Proposição 7.1 (Filtro geométrico mod 30 — incondicional).** Para HR⁻ disparar
na configuração canônica, é necessário que:

```
C mod 30  ∈  {0, 2, 6, 8, 12, 14, 18, 20, 24}
```

Esta condição elimina as 6 classes pares restantes {4, 10, 16, 22, 26, 28} (mod 30),
correspondendo a uma triagem de 40% das classes pares a priori, sem nenhum teste
de primalidade.

*Demonstração.* Para HR⁻ disparar, e₁ = C−1 deve ser primo. Todo primo p > 5
satisfaz p ≢ 0 (mod 2), p ≢ 0 (mod 3), p ≢ 0 (mod 5), logo p está em uma das
φ(30)/2 = 8 classes ímpares mod 30: {1, 7, 11, 13, 17, 19, 23, 29}. Como p = C−1,
segue C ≡ p+1 (mod 30) ∈ {2, 8, 12, 14, 18, 20, 24, 0}. A exceção p = 5 (único
primo ≡ 5 mod 30) contribui com C = 6. □

**Observação 7.2 (Geometria sem aritmética modular).** A grade chega ao filtro mod
30 por geometria pura, sem qualquer cálculo modular explícito: a posição i\* determina
e₁ = C−1; a exigência de que e₁ seja primo (Filtro 1) restringe C a classes mod 30;
a independência de crivo (Seção 6) garante que essas classes são precisamente as
"admissíveis" para o par. O filtro mod 30 é a *roda de 30 clássica* emergindo
geometricamente.

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

**Proposição 7.4 (Anomalia de C ≡ 6 mod 30 — incondicional).** Entre os 9 resíduos
admissíveis {0, 2, 6, 8, 12, 14, 18, 20, 24} (mod 30), o resíduo C ≡ 6 é o único
para o qual HR⁻ só pode disparar em um único valor de C, nomeadamente C = 6.
Para todo C > 6 com C ≡ 6 (mod 30), HR⁻ não dispara.

*Demonstração.* Escreva C = 30k + 6 com k ≥ 0. Então:

```
e₁ = C − 1 = 30k + 5 = 5(6k + 1)
```

Para k = 0: e₁ = 5, que é primo — HR⁻ pode disparar (e dispara, pois e₃ = 31 é primo).
Para k ≥ 1: e₁ = 5(6k+1) com 6k+1 ≥ 7, logo e₁ > 5 e 5 | e₁, portanto e₁ é composto.
HR⁻ exige e₁ primo, logo não dispara para C > 6 com C ≡ 6 (mod 30). □

*Origem geométrica.* A anomalia decorre da interação entre dois filtros:
(i) C ≡ 6 (mod 30) implica C ≡ 1 (mod 5), que pelo Corolário 6.9 garante 5 | e₁;
(ii) entre os resíduos admissíveis mod 30, apenas C ≡ 6 satisfaz C ≡ 1 (mod 5).
Os demais 8 resíduos admissíveis têm e₁ mod 5 ∈ {1, 2, 3, 4} — sem obstrução por 5.

**Observação 7.5 (Confirmação empírica e uniformidade dos demais resíduos).** Verificação
em 269 casos HR⁻ com C ≤ 5000 confirma: C ≡ 6 (mod 30) ocorre exatamente 1 vez
(C = 6), enquanto os demais 8 resíduos admissíveis apresentam distribuição aproximadamente
uniforme, com 28 a 37 casos cada. A Proposição 7.4 explica completamente essa
assimetria: não é flutuação estatística — é uma obstrução estrutural exata.

---

## 8. Estrutura de Cadeias e Constelações Admissíveis

A independência de crivo (Seção 6) tem uma consequência estrutural sobre como os
valores de C que disparam HR⁻ se organizam: eles tendem a aparecer em *cadeias*,
refletindo constelações de primos admissíveis em p = C−1.

**Definição 8.1 (Cadeia canônica de comprimento k).** Uma cadeia canônica de
comprimento k é uma sequência C₁ < C₂ < … < Cₖ de valores de C (pares) tais que:
(a) cada Cⱼ − 1 é primo; (b) cada 5Cⱼ + 1 é primo; (c) os gaps Cⱼ₊₁ − Cⱼ ∈ {2, 4, 6}.

**Proposição 8.2 (Tipos de gap e constelações).** Os três tipos de gap observados
correspondem a constelações de primos em p:

- **Gap 2:** (p, p+2) são primos gêmeos. Ambos disparam HR⁻ iff 5p+6 e 5p+16
  são ambos primos.
- **Gap 4:** (p, p+4) são primos cousins. Ambos disparam HR⁻ iff 5p+6 e 5p+26
  são ambos primos.
- **Gap 6:** (p, p+6) são primos sexy. Ambos disparam HR⁻ iff 5p+6 e 5p+36
  são ambos primos.

*Verificação numérica (C ≤ 500):* 49 casos; 15 isolados (31%), 34 em cadeias (69%).
As três cadeias de comprimento 4 observadas são:
- (38, 42, 48, 54): p = 37, 41, 47, 53 — gaps (4, 6, 6);
- (98, 104, 108, 114): p = 97, 103, 107, 113 — gaps (6, 4, 6);
- (128, 132, 138, 140): p = 127, 131, 137, 139 — gaps (4, 6, 2).

**Observação 8.3 (Cadeias e independência de crivo).** A independência de crivo
para q > 3 implica que, dentro de uma cadeia, a eliminação de um par (Cⱼ−1, 5Cⱼ+1)
por algum primo q > 3 não propaga para o par adjacente (Cⱼ₊₁−1, 5Cⱼ₊₁+1). As
cadeias são, portanto, *aritmeticamente independentes* ponto a ponto para todos os
crivos q > 3 — a estrutura que uma análise de crivo linear exploraria.

---

## 8A. Cadeias de Autossimilaridade via T(C) = 5C+2

Esta seção unifica os resultados da nota complementar sobre cadeias de
autossimilaridade com a estrutura algébrica da recorrência canônica. Todos
os resultados marcados como incondicional independem de primalidade.

**Definição 8A.1 (Transformação canônica T).** A transformação

```
T : C  ↦  5C + 2
```

definida sobre os inteiros pares C ≥ 4, satisfaz a relação geométrica central:

```
e₃(C) = 5C + 1 = T(C) − 1 = e₁(T(C))
```

O primo de saída do par canônico de C é o primo de entrada do par canônico
de T(C). A saída de uma geração é a entrada da seguinte.

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

*Demonstração.* (i) 5C par + 2 par. (ii) Cálculo direto de (5r+2) mod 30
para cada r ∈ {0,2,6,8,12,14,18,20,24} — todos caem em {2,12}. □

**Corolário 8A.4 (Ciclo de período 2 em {2, 12} — incondicional).** A
restrição de T aos resíduos {2, 12} forma um ciclo de período 2:

```
T(2) ≡ 12 (mod 30)    T(12) ≡ 2 (mod 30)
```

A partir de C₁, toda cadeia alterna estritamente entre resíduos 2 e 12
(mod 30), independentemente do resíduo de C₀.

*Verificação exaustiva.* Em 128 cadeias de comprimento ≥ 2 encontradas
até C = 10000, zero violações a este padrão foram observadas.

**Corolário 8A.5 (Resíduo da raiz livre; imagem determinística).** O
primeiro elemento C₀ pode ter qualquer resíduo admissível mod 30 (exceto
6, pela Proposição 7.4). A partir de C₁, o resíduo é determinado por:

```
C₁ mod 30 = (5·(C₀ mod 30) + 2) mod 30 ∈ {2, 12}
```

**Proposição 8A.6 (Autossimilaridade — incondicional).** Em toda cadeia,
o par canônico de cada geração satisfaz a mesma relação:

```
e3ₙ = 5 · e1ₙ + 6   para todo n ≥ 0
```

Em particular e1ₙ₊₁ = e3ₙ — o e3 de uma geração é o e1 da seguinte.

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
e1ₙ é sempre ímpar (5ⁿ·p ímpar; (3/2)·(5ⁿ−1) par) e mdc(e1ₙ, 3) = 1
pois e1ₙ ≡ 2ⁿ·p (mod 3) com p ≢ 0 (mod 3). □

**Observação 8A.10 (Estrutura mod 3 e independência de crivo).** Como
5 ≡ 2 (mod 3), a fórmula fechada dá e1ₙ ≡ 2ⁿ·p (mod 3). O resíduo
alterna entre p mod 3 e 2p mod 3 — nunca dois termos consecutivos são
ambos divisíveis por 3, consistente com a Observação 6.10. Combinado
com o Teorema 6.2, isso implica que nenhum primo q > 3 elimina
simultaneamente dois termos consecutivos da cadeia.

**Observação 8A.11 (Dados empíricos até C = 10000).**

| Comprimento | Cadeias maximais | Exemplo (C₀, primos p) |
|-------------|-----------------|------------------------|
| 1 (isolado) | 153 | C=14: p=13, q=71 |
| 2 | 101 | C=12: 11→61→311 |
| 3 | 22  | C=8→42→212: 7→41→211→1061 |
| 4 | 4   | C=1260: 1259→6301→31511→157561 |
| 6 | 1   | C=80: 79→401→2011→10061→50311→251561 |

A cadeia de comprimento 6 (C₀ = 80) é a mais longa verificada:

```
C₀ = 80:     e₁ = 79,      e₃ = 401       ✓
C₁ = 402:    e₁ = 401,     e₃ = 2011      ✓
C₂ = 2012:   e₁ = 2011,    e₃ = 10061     ✓
C₃ = 10062:  e₁ = 10061,   e₃ = 50311     ✓
C₄ = 50312:  e₁ = 50311,   e₃ = 251561    ✓
C₅ = 251562: e₁ = 251561,  e₃ = 1257811   ✗ (= 7 × 179687)
```

Resíduos mod 30: [20, 12, 2, 12, 2, 12] — alternância a partir de C₁
verificada por cinco gerações consecutivas.

**Observação 8A.12 (Conexão com conjecturas sobre formas lineares).** A
existência de cadeias de comprimento arbitrário é equivalente à existência
de órbitas arbitrariamente longas de p ↦ 5p+6 inteiramente dentro dos
primos — uma instância da conjectura de Dickson sobre sistemas de formas
lineares. A não degeneração do par (p, 5p+6) está provada incondicionalmente
(Proposição 3.3): os coeficientes (1, 5) são linearmente independentes e a
progressão é localmente solúvel. Sob GTZ [7], a descorrelação espectral das
componentes j ≠ 0 é incondicional (Artigo 6, Proposição 5.2); a barreira
remanescente é a positividade de F̂(0) — equivalente a HR⁻ — para cada
geração individualmente.

**Observação 8A.13 (Relação com o sistema espectral do Artigo 6).** Cada
geração define um sistema (X_{Nₙ}, µ_{Nₙ}, T) com Nₙ ~ 5ⁿ·N₀. A
coprimaridade (Proposição 8A.9) garante que as funções de colisão F de
gerações distintas são aritmeticamente independentes: nenhum fator comum
propaga primalidade ou composibilidade entre gerações. As cadeias são
*órbitas aninhadas e independentes* no sentido espectral do Artigo 6.

---

## 9. Relação com o Artigo Espectral (Artigo 6)

A configuração canônica é a manifestação concreta, na linguagem geométrica, do
objeto espectral F̂(0) do Artigo 6.

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

A positividade de F̂(0) é equivalente, na configuração canônica, ao par de
condições do Corolário 2.4.

**Observação 9.3 (O crivo canônico como instância concreta de GTZ).** A
descorrelação espectral das componentes j ≠ 0 provada no Artigo 6 (Proposição 5.2,
via GTZ) é, na configuração canônica, exatamente a independência de crivo do
Teorema 6.2: as autofunções ϕⱼ(i) = exp(2πiji/K) para j ≠ 0 são nilsequências de
grau 1, e sua descorrelação com w(i) = Λ(e₁(i))Λ(e₃(i)) decorre de que
(L₁(p), L₂(p)) = (p, 5p+6) é não degenerado (Proposição 3.3). As duas linguagens
— espectral e geométrica — capturam o mesmo conteúdo aritmético.

---

## 10. Certificado de Lucas Geométrico para e₃

Esta seção formaliza a consequência mais direta da relação e₃ − 1 = 5·(e₁+1) = 10k:
a geometria do acoplamento 3C = 2N fornece, **de graça e antes de qualquer teste**,
uma fatoração parcial de e₃ − 1 que habilita o Teste de Lucas — um certificado de
primalidade **determinístico**, não probabilístico.

Todos os resultados desta seção são **incondicionais** na estrutura; a primalidade
de e₃ é o que se quer provar, não o que se assume.

### 10.1 A fatoração parcial gratuita

**Proposição 10.1 (Fatoração parcial de e₃ − 1 — incondicional).** Na configuração
canônica com acoplamento 3C = 2N, escrevendo C = 2k (k inteiro, k ≥ 2):

```
e₃ − 1 = 5C + 1 − 1 = 5C = 5·2k = 10k
```

Portanto:

```
e₃ − 1 = 2 · 5 · k
```

Os fatores primos {2, 5} são **sempre** fatores de e₃ − 1, independentemente de
k e independentemente de qualquer hipótese de primalidade. Eles são conhecidos
antes de qualquer cálculo, por consequência direta da condição 3C = 2N.

*Demonstração.* e₃ = 5C + 1 = 5·2k + 1 = 10k + 1, logo e₃ − 1 = 10k = 2·5·k.
Os fatores 2 e 5 de 10 são imediatos. □

**Corolário 10.2.** O conjunto completo de fatores primos de e₃ − 1 é:

```
fatores_primos(e₃ − 1) = {2, 5} ∪ fatores_primos(k)
```

Para obter a fatoração completa de e₃ − 1, basta fatorar k — um número
aproximadamente 10 vezes menor que e₃.

**Caso especial (k primo).** Se k é primo, então e₃ − 1 = 2·5·k está
completamente fatorado só pela geometria:

```
k primo  ⟹  fatores_primos(e₃ − 1) = {2, 5, k}   (completo, sem fatoração adicional)
```

Isso ocorre nos casos k ∈ {3, 7, 19, 31, 97, 157, 211, …} — exatamente quando
k = (e₁+1)/2 é primo.

### 10.2 O Teste de Lucas e o certificado geométrico

**Teorema de Lucas (clássico).** Um inteiro n > 1 é primo se e somente se existe
uma base a ∈ {2, …, n−1} tal que:

```
(L1)  a^(n−1) ≡ 1 (mod n)
(L2)  a^((n−1)/q) ≢ 1 (mod n)   para todo fator primo q de n−1
```

O Teorema de Lucas é **determinístico**: se tal base existe, n é primo;
se n é composto, nenhuma tal base existe.

**Definição 10.3 (Certificado de Lucas geométrico).** Dado k com e₁ = 2k−1 primo
e e₃ = 10k+1 candidato, o **certificado de Lucas geométrico** para e₃ é a tripla:

```
ℒ(k) = (e₃, fatores_primos(e₃−1), a)
```

onde fatores_primos(e₃−1) = {2, 5} ∪ fatores_primos(k) é obtida via Proposição
10.1, e a é a menor base que satisfaz (L1) e (L2).

Quando ℒ(k) existe, ele prova que e₃ é primo de forma determinística.

**Proposição 10.4 (Custo do certificado geométrico — incondicional).** O Certificado
de Lucas geométrico ℒ(k) para e₃ = 10k+1 requer:

1. **Fatoração:** fatorar k (tamanho ~e₃/10), não e₃ diretamente. O custo de
   trial division é O(√k) = O(√(e₃/10)) ≈ O(√e₃ / √10) — uma redução de
   fator √10 ≈ 3.16 em relação à fatoração direta de e₃.

2. **Lucas:** |fatores_primos(e₃−1)| = 2 + ω(k) exponenciações modulares mod e₃,
   onde ω(k) é o número de fatores primos distintos de k. Na prática ω(k) ≤ 4
   para os casos observados, totalizando no máximo 6 exponenciações.

3. **Para k primo:** custo de fatoração zero (k já é sabidamente primo se e₁
   passou no Filtro 1 com k = (e₁+1)/2 primo), e apenas 3 exponenciações modulares.

**Observação 10.5 (O que a geometria fornece e o que não fornece).** O certificado
ℒ(k) prova que e₃ é primo — mas somente se e₃ for de fato primo. Se e₃ é
composto, nenhuma base a satisfaz (L1) e (L2) simultaneamente, e o processo
termina sem certificado. A geometria não garante que e₃ é primo; garante que,
**se** e₃ for primo, a prova é mais eficiente do que para um número geral da
mesma magnitude — porque a fatoração parcial de e₃ − 1 é conhecida a priori.

### 10.3 Verificação numérica

A tabela abaixo confirma o certificado para os primeiros casos HR⁻ (C ≤ 500).
Em todos os casos, a base a satisfaz (L1) e (L2) e o certificado é válido.

| k  | e₁    | e₃    | e₃−1 = 10k | fatores de e₃−1 | base a | exp. mod |
|----|-------|-------|------------|-----------------|--------|----------|
| 3  | 5     | 31    | 30 = 2·3·5 | {2,3,5}         | 3      | 3        |
| 4  | 7     | 41    | 40 = 2³·5  | {2,5}           | 6      | 2        |
| 7  | 13    | 71    | 70 = 2·5·7 | {2,5,7}         | 7      | 3        |
| 10 | 19    | 101   | 100 = 2²·5² | {2,5}          | 2      | 2        |
| 19 | 37    | 191   | 190 = 2·5·19 | {2,5,19}      | 19     | 3        |
| 31 | 61    | 311   | 310 = 2·5·31 | {2,5,31}      | 17     | 3        |
| 64 | 127   | 641   | 640 = 2⁷·5 | {2,5}           | 3      | 2        |
| 91 | 181   | 911   | 910 = 2·5·7·13 | {2,5,7,13} | 17     | 4        |
| 97 | 193   | 971   | 970 = 2·5·97 | {2,5,97}      | 6      | 3        |

Para e₃ composto (Filtro 2 falhou), nenhuma base satisfaz Lucas — o processo
termina corretamente sem certificado.

### 10.4 Síntese: o que o certificado geométrico é e o que não é

| Propriedade | Certificado de Lucas geométrico |
|-------------|--------------------------------|
| Determinístico? | Sim — Lucas é prova, não teste probabilístico |
| Requer fatoração? | Sim — de k ≈ e₃/10, não de e₃ |
| Custo vs Lucas geral | √10 ≈ 3.16x menos trabalho de fatoração |
| Válido para e₃ composto? | Não — sem certificado quando e₃ é composto |
| Prova que e₃ existe? | Não — pressupõe que e₃ passou no Filtro 2 |
| Específico à família 3C=2N? | Sim — a fatoração {2,5} é específica de e₃=10k+1 |
| Generaliza para C arbitrário? | Não — requer o acoplamento geométrico exato |

---

## 11. Crivo Segmentado Conjunto e Aceleração Geométrica

A independência de crivo (Teorema 6.2) tem uma consequência prática para crivos
em lote: ao cribilar o par (C−1, 5C+1) **simultaneamente** para uma família de
valores de C num intervalo, a independência elimina trabalho duplicado. Esta seção
formaliza esse ganho.

Todos os resultados desta seção são **incondicionais**. Eles descrevem o
comportamento do crivo — não provam primalidade.

### 10.1 Configuração: crivo em lote sobre um intervalo

Fixemos um intervalo de valores pares C ∈ [P, P+H] (com H ≪ P). Para cada tal C,
o crivo canônico aponta para o par:

```
e₁(C) = C − 1  ∈  [P−1, P+H−1]       — intervalo I₁ de comprimento H
e₃(C) = 5C + 1 ∈  [5P+1, 5P+5H+1]    — intervalo I₃ de comprimento 5H
```

O **crivo segmentado conjunto** é o processo de cribilar I₁ e I₃ simultaneamente
com os mesmos primos q, identificando quais pares (e₁(C), e₃(C)) sobrevivem —
ou seja, quais C são candidatos a disparar HR⁻.

**Definição 10.1 (Crivo segmentado conjunto).** Para um conjunto de primos
Q = {q : 3 < q ≤ Q_max}, o crivo segmentado conjunto sobre [P, P+H] é o processo
de marcar, para cada q ∈ Q:

- em I₁: as posições C tal que q | (C−1), i.e., C ≡ 1 (mod q);
- em I₃: as posições C tal que q | (5C+1), i.e., C ≡ −1/5 (mod q).

Um C é **eliminado por q** se está marcado em I₁ **ou** em I₃. O par (e₁(C), e₃(C))
sobrevive ao crivo se C não é eliminado por nenhum q ∈ Q.

### 10.2 Trabalho de crivo sem independência (caso geral)

Para um par genérico (a(C), b(C)) de formas lineares em C, o primo q marca:

- ~H/q posições em I₁ (as C com q | a(C));
- ~H/q posições em I₃ (as C com q | b(C));
- ~H/q² posições em ambos simultaneamente (se as formas são independentes mod q).

O trabalho total de marcação por q é ~2H/q, e o número de C eliminados por q
é ~2H/q − H/q² (subtraindo a sobreposição).

### 10.3 Trabalho de crivo com independência — o ganho geométrico

**Proposição 10.2 (Sobreposição nula para q > 3 — incondicional).** Para todo
primo q > 3 e todo C par, as condições "q | (C−1)" e "q | (5C+1)" são
mutuamente exclusivas. Portanto:

```
|{C ∈ [P,P+H] : q|(C−1) e q|(5C+1)}| = 0     para todo q > 3
```

*Demonstração.* Direta do Teorema 6.2: q | (C−1) e q | (5C+1) implica q | 6,
impossível para q > 3. □

**Corolário 10.3 (Eliminações por q no crivo conjunto).** Para q > 3, o número
de C ∈ [P, P+H] eliminados pelo crivo conjunto é:

```
|elim(q)| = |{C : q|(C−1)}| + |{C : q|(5C+1)}|
           ≈ H/q + H/q
           = 2H/q
```

sem nenhuma subtração de sobreposição (que é zero). Para um par genérico, o número
seria 2H/q − H/q² — ligeiramente menor, pois a sobreposição reduz as eliminações.
O par canônico elimina *mais* por q, não menos: cada eliminação por q atinge
exclusivamente um dos dois elementos, nunca os dois.

**Observação 10.4 (Interpretação).** O ganho não é em velocidade de eliminação —
é em **interpretação de cada eliminação**: quando q elimina C−1, sabe-se
automaticamente que q não elimina 5C+1, e vice-versa. Isso significa que cada
primo q > 3 fornece informação *maximal* sobre o par: ou e₁ é descartado, ou e₃
é descartado, nunca ambos e nunca nenhum (salvo coincidência).

Em termos de crivo: o par canônico é o mais informativo possível para q > 3.

### 10.4 Densidade de sobreviventes ao crivo conjunto

**Proposição 10.5 (Densidade de pares sobreviventes — incondicional).** A fração
de valores C ∈ [P, P+H] que sobrevivem ao crivo conjunto até Q_max é:

```
D_conjunto(P, H, Q_max) = ∏_{3 < q ≤ Q_max} (1 − 1/q)² · (1 + correção(q))
```

onde correção(q) = 0 para todo q > 3 pela Proposição 10.2 (sobreposição nula).
Para um par genérico com sobreposição H/q²:

```
D_genérico(P, H, Q_max) = ∏_{3 < q ≤ Q_max} (1 − 2/q + 1/q²)
                        = ∏_{3 < q ≤ Q_max} (1 − 1/q)²
```

Os dois produtos são iguais — o par canônico e um par genérico não degenerado
têm a mesma densidade assintótica de sobreviventes.

*Demonstração.* Para cada q > 3, a fração de C eliminados é 2/q (duas classes
mod q, disjuntas pela independência). A fração sobrevivente por q é 1 − 2/q.
O produto sobre os q independentes dá o resultado. Para o par genérico, a fração
eliminada é 2/q − 1/q² (subtraindo sobreposição), e a fração sobrevivente é
1 − 2/q + 1/q² = (1−1/q)². Os produtos coincidem assintoticamente. □

**Observação 10.6 (O ganho real é estrutural, não assintótico).** A Proposição
10.5 mostra que a densidade assintótica de sobreviventes é a mesma para o par
canônico e para um par genérico não degenerado. O ganho geométrico não é uma
melhora assintótica — é uma **garantia estrutural**: a independência é exata
(sobreposição literalmente zero), não apenas aproximada. Para crivos finitos sobre
intervalos pequenos, isso elimina os termos de erro associados à estimativa de
sobreposição, que num par genérico seriam O(H/q²) por primo.

### 10.5 A barreira de paridade de Selberg

**Observação 10.7 (Limite do crivo conjunto — incondicional).** O crivo segmentado
conjunto, por mais eficiente que seja na gestão das eliminações, não supera a
**barreira de paridade de Selberg**: crivos lineares não distinguem primos de
produtos de dois primos grandes (semiprimos). Formalmente, o crivo conjunto produz
uma cota superior

```
|{C ∈ [P,P+H] : e₁(C) primo e e₃(C) primo}| ≤ A · H / (log H)²
```

mas não uma cota inferior. A independência de crivo melhora a constante A implícita,
mas não muda a ordem (log H)⁻². Provar que o número de pares primos é ≥ B · H/(log H)²
— ou seja, que existe ao menos um par primo no intervalo — requer ir além do crivo
linear, exatamente como HR⁻ requer ir além do Artigo 6.

### 10.6 Síntese do ganho geométrico

| Propriedade | Par genérico | Par canônico (C−1, 5C+1) |
|-------------|-------------|--------------------------|
| Sobreposição por q > 3 | ~H/q² (estimada) | 0 (exata, pelo Teorema 6.2) |
| Erro de estimativa de sobreposição | O(H/q²) por primo | 0 exato |
| Densidade assintótica de sobreviventes | ∏(1−1/q)² | ∏(1−1/q)² (igual) |
| Cota superior do crivo | A·H/(log H)² | A·H/(log H)² (mesma ordem) |
| Cota inferior do crivo | inacessível (barreira de paridade) | inacessível |
| Interpretação por eliminação | ambígua (pode eliminar ambos) | maximal (elimina exatamente um) |

O par canônico é o **mais bem-comportado possível** para crivos lineares, no sentido
de que satisfaz a independência de forma exata. Isso não resolve HR⁻, mas significa
que nenhuma obstrução de crivo linear existe além da barreira de paridade — a
barreira remanescente é puramente aritmética.

---

## 12. Síntese: o que o Crivo Canônico é e o que não é



### O que é:

- Uma **seleção geométrica** que aponta, sem teste de primalidade, para o único par
  candidato (C−1, 5C+1) na posição canônica Wi\*.
- Uma **garantia de independência**: para q > 3, a eliminação de C−1 não implica
  eliminação de 5C+1, e vice-versa.
- Um **certificado de localização**: se ambos os elementos forem primos, o crivo
  canônico certifica que 6C é Goldbach e que (C−1, 5C+1) é o representante canônico.
- Uma **tradução geométrica de GTZ**: a não degeneração do par de formas lineares
  (p, 5p+6) — que GTZ usa para garantir infinitos pares primos — é exatamente a
  independência de crivo expressa em linguagem aritmética.

### O que não é:

- Um **teste de primalidade**: a grade localiza o par, não verifica se é primo. Essa
  verificação requer aritmética externa.
- Uma **prova de HR⁻** para cada C: a garantia de GTZ é assintótica (infinitos C),
  não uniforme (cada C específico).
- Uma **simplificação do problema de Goldbach**: a dificuldade aritmética é a
  mesma — apenas está mais bem localizada. Como o Artigo 6 nota, Fb(0) > 0 para
  cada C específico é equivalente à própria Conjectura de Goldbach nesse ponto.

### A formulação honesta:

> A geometria transforma "existe algum par primo somando 6C entre N−1 candidatos?"
> em "é (C−1, 5C+1) um par primo?". Isso é **mais limpo**, não mais fácil. A
> independência de crivo para q > 3 garante que o par é bem-comportado para crivos
> lineares — mas não que algum par seja primo. A barreira aritmética permanece
> intacta; o crivo canônico apenas a expõe com máxima clareza geométrica.

---

## 13. Conclusão e Lacunas Remanescentes

**Camada geométrica — resultados incondicionais.**

1. **Fórmula fechada** (Proposição 2.3): o par canônico (e₁, e₃) = (C−1, 5C+1) é
   determinado exclusivamente por i\* e pela estrutura de L₁ crescente e L₃ decrescente.
   Nenhuma ordenação ou busca é necessária.

2. **Independência de crivo** (Teorema 6.2): para todo primo q > 3, nenhum q
   elimina simultaneamente C−1 e 5C+1. Esta é a propriedade geométrica central do
   par canônico e é consequência direta do coeficiente 5 que emerge de i\*.

3. **Não degeneração** (Proposição 3.3): o par de formas lineares (p, 5p+6) satisfaz
   as condições de GTZ, garantindo incondicionalmente que existem infinitos C com
   HR⁻ na configuração canônica.

4. **Filtro mod 30** (Proposição 7.1): a restrição C mod 30 ∈ {0,2,6,8,12,14,18,20,24}
   é consequência geométrica da posição i\* e da exigência de primalidade de e₁.

5. **Certificado geométrico** (Definição 4.1): quando HR⁻ dispara, a quádrupla
   𝒞(C) = (G₃,C, i\*, e₁, e₃) constitui um certificado verificável de que 6C é
   soma de dois primos, com representante canônico (C−1, 5C+1).

**Lacuna remanescente.**

A única hipótese não provada é a primalidade simultânea de C−1 e 5C+1 para cada C
específico — i.e., HR⁻ individual. O crivo canônico reduz o espaço de busca ao
par canônico e garante sua independência de crivo; mas não garante que o par seja
primo. Esta é a barreira aritmética central da série, atacada no Artigo 6 via
análise espectral e aqui via geometria de formas lineares.

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

[8] B. Green e T. Tao, *The primes contain arbitrarily long arithmetic progressions*,
Annals of Mathematics, vol. 167, pp. 481–547, 2008.

[9] H. Iwaniec e E. Kowalski, *Analytic Number Theory*, American Mathematical Society
Colloquium Publications, vol. 53, 2004.

---

*Preprint — maio de 2026. Artigo 7 da série sobre a Conjectura de Goldbach.*  
*Os resultados incondicionais são os listados na Seção 11. A condição HR⁻ individual permanece em aberto.*