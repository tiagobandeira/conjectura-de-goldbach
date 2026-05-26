# Changelog

Todas as mudanças significativas neste projeto são documentadas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).


## [2.7.5] - 2026-05-26

### Adicionado

- `motor_heranca_definitivo.tex` / `.pdf` — Documento de Formalização do Motor de Herança Estrutural (Versão Definitiva, rev. 2). Define com precisão os dois objetos centrais da série: par base 2M (soma das colunas da fita) e par alvo 2M+2 (soma das diagonais), a Janela Wi com seus quatro eixos de simetria, o algoritmo do scanner com pivôs, o Gabarito como referência canônica, e o protocolo de simulação Caos → Ordem.
- `motor_heranca.ipynb` — Notebook de verificação computacional. Implementa o protocolo de transição de fase (Bubble Sort sobre a lista de ímpares), coleta métricas de ativação de HR− e HR+ por par base, e registra o Tempo de Primeira Passagem.
- `motor_heranca.py` — Código-fonte unificado de todos os módulos do motor: construção da Fita-Dobra, acoplamento grade 3×C, scanner de pivôs, preenchimento da Janela Wi, verificação de HR− e HR+, e rotina de simulação.
- `README.md` — Descrição em prosa do Motor de Herança Estrutural para leitores que não necessitem do PDF completo. Cobre todos os conceitos centrais sem notação formal pesada.

### Alterado

- **Redefinição do Motor (breaking):** as definições de par base e par alvo presentes nos Artigos 5 e 6 da série foram corrigidas e substituídas pelas deste documento.
  - **Antes:** a distinção entre par base e par alvo não estava formalizada; o papel das colunas vs. diagonais da fita era implícito.
  - **Agora:** par base 2M = soma das colunas (Goldbach já certificado); par alvo 2M+2 = soma das diagonais (certificado por HR−). Esta distinção propaga-se por todas as definições do motor.

### Corrigido

- Corrigida a descrição da Janela Wi nos Artigos 5 e 6: Wi não é deslizante — ela é preenchida pelo scanner e permanece como referência estrutural fixa.
- Corrigido o papel do elemento 1 no scanner: o pivô esquerdo pula o elemento 1 pois não existe par diagonal válido com soma igual ao par alvo que o inclua.

## [2.7.4] - 2026-05-25

### Adicionado
- nota: crivo canônico Wi* — fórmula fechada (e1=C−1, e3=5C+1),
  independência de crivo para q>3, filtro mod 30, certificado de Lucas
  geométrico. Status: rascunho (Artigo 7).

- nota: cadeias de autossimilaridade via T(C)=5C+2 — anomalia
  C≡6 (mod 30) provada incondicionalmente, ciclo {2,12} mod 30,
  fórmula fechada e1_n = 5^n·p + (3/2)·(5^n−1), coprimaridade,
  cadeia de comprimento 6 verificada (C₀=80). Status: nota complementar.

- código: canonical_wi_star.py — verificação da posição canônica
  por fórmula fechada, sem construção da grade.

- código: lucas_geometrico_wi_star.py — certificado de Lucas
  aplicado ao par canônico.

### Observações
- A geometria da grade (pivôs, janelas 3×3, diagonais da fita)
  está em reformulação. Definição do motor será revisada em versão
  futura antes de integrar estas notas à série principal.

## [2.7.3] - 2026-05-21
### Restaura v2.7.1
  - Restaura versões anteriores(artigo 8).


## [2.7.1] - 2026-05-21

### Adicionado
- Primeira versão dos notebooks de testes espectrais:  
  `notebooks/frentes_espectrais_motor_notebook.ipynb`
  - Implementa o Motor de Herança Estrutural com busca via órbita de σ.
  - Calcula a função de peso `w(t) = Λ(e₁)·Λ(e₃)` e sua DFT, verificando a positividade de ŵ(0) (HR⁻) e o decaimento de |ŵ(j≠0)|.
  - Inclui a Frente 4 (janela polinomial `L = M^δ`) e a Frente 2 (análise espectral).
  - Contém uma célula de diagnóstico que demonstra que o artefato 2,00× na razão ŵ(0)/max|ŵ(j≠0)| ocorre apenas quando `N-1` é potência de 10, e recomenda usar `N` arbitrários (não potências de 10) para evitar aliasing numérico.
  - Gera gráficos e estatísticas que corroboram a descorrelação espectral prevista na Proposição 5.2 do artigo.
- Documentação: seção no README sobre como executar os notebooks e interpretar os resultados.

---

### [v2.7.0] — Maio 2026

#### Adicionado — Paper 08: Reformulação Espectral do Motor de Herança

- **Sistema dinâmico de medida finita `(X_N, μ_N, T)`**:
  construção explícita sobre a linha mediana de `G_{3,N}`, com
  `X_N = {1, …, N-1}`, medida uniforme `μ_N` e translação cíclica
  `T(t) = t+1 mod (N-1)`. As linhas da grade são parametrizadas como
  `e1(t) = t`, `e2(t) = N` (fixo), `e3(t) = 2N-1-t`.

- **Operador de Koopman `U_T` — espectro e entropia** (incondicional):
  prova de que `U_T` tem espectro discreto puro (raízes da unidade) e
  entropia métrica `h(T) = 0`; ambos decorrem da natureza de rotação
  racional de `T` e são independentes de qualquer hipótese sobre primos.

- **Função de colisão `F(t) = 1_P(e1(t)) · 1_P(e3(t))`**:
  indicadora dos instantes em que `e1(t)` e `e3(t)` são simultaneamente
  primos; a sua componente de frequência zero `F̂(0)` conta, em média,
  as colisões primo-primo na linha mediana.

- **Teorema 4.4 — Equivalência espectral de HR⁻** (incondicional):
  `HR⁻ ⟺ F̂(0) > 0`. A positividade da componente de frequência zero
  da função de colisão é necessária e suficiente para a Hipótese
  Restritiva Fraca, sem qualquer condição adicional.

- **Proposição 5.2 — Cancelamento espectral das frequências laterais**
  (incondicional, via Green–Tao–Ziegler 2012):
  para a função de von Mangoldt ponderada `w(t) = Λ(e1(t)) Λ(e3(t))`,
  prova-se que `ŵ(j) → 0` para todo `j ≠ 0`. O argumento usa o teorema
  de nilsequências de Green–Tao–Ziegler para garantir o cancelamento
  incondicional de todas as oscilações espectrais.

- **Redução de Goldbach à positividade de `ŵ(0)`** (incondicional):
  combinando o Teorema 4.4 e a Proposição 5.2, o problema de Goldbach
  para o par `2M⁺` equivale incondicionalmente a provar `ŵ(0) > 0`.
  Todas as outras componentes espectrais são irrelevantes para o problema.

- **Diagnóstico do colapso dos métodos clássicos**:
  análise de por que o método do círculo de Hardy–Littlewood, o crivo
  linear de Rosser–Iwaniec e a abordagem de Buchstab–Chen esbarram no
  obstáculo da paridade e não alcançam uma prova de Goldbach; explicitação
  de como a formulação espectral evita esses obstáculos ao reformular
  o problema em termos de cancelamento de nilsequências, normas de Gowers
  e o princípio de ortogonalidade de Sarnak.

- **Lacuna remanescente precisamente isolada**:
  a positividade de `ŵ(0)` não é provada incondicionalmente; sob a
  Hipótese de Riemann Generalizada (GRH), a cota inferior `ŵ(0) > 0`
  pode ser estabelecida (trabalho futuro). Sem GRH, o problema tem
  exactamente a mesma dificuldade que a conjectura original.

#### Alterado

- **README — versão e contagem de artigos**: actualizado de v2.6.0 para
  v2.7.0; a frase "seis artigos complementares" passa a "oito artigos
  complementares".
- **README — diagrama da linha de Goldbach**: Paper 08 inserido no topo
  como estado actual; Paper 07 (Motor de Herança) recebe posição própria
  abaixo da camada espectral.
- **README — secção "Progresso recente"**: substituída pelo resumo do
  Paper 08; o resumo do Paper 06 (Problema B) mantém-se na secção do
  próprio artigo.
- **README — camadas de progresso**: Paper 07 passa a Camada 4;
  Paper 08 entra como Camada 5 *(novo)*; lacuna remanescente sobe para
  Camada 6.
- **README — tabela de resultados incondicionais**: seis novas linhas
  relativas ao Paper 08 (espectro, entropia, Teorema 4.4, Proposição 5.2,
  redução, acoplamento com Paper 07).
- **README — tabela de resultados condicionais**: duas novas linhas —
  Teorema do Motor condicional a HR⁻ (Paper 07) e cota `ŵ(0) > 0`
  condicional a GRH (Paper 08).
- **README — secção "Como compilar os PDFs"**: bloco bash para o
  Paper 08 adicionado.
- **README — secção de citações**: entrada BibTeX `bandeira2026ergotica`
  adicionada.
- **Paper 07 — secção "Conexão com a série"**: referência a Paper 08
  actualizada para reflectir que `Φ` e a órbita de `σ` são usados como
  ferramentas algébricas na reformulação espectral.

--- 

### [v2.6.0] — Maio 2026
#### Adicionado — Paper 7 (v3)
- **Observação 4.5 — Estrutura direccional de $\sigma$ por linha**:
  formaliza que L1 avança $e_1(t)\!+\!2$, L3 recua $e_3(t)\!-\!2$, e o
  cancelamento $\Delta e_1 + \Delta e_3 = 0$ é a razão geométrica da soma
  constante da Prop. 4.3(iii) — não apenas um facto algébrico mas uma
  simetria direccional explícita.
- **Nota sobre a natureza dos eventos** (dentro da Obs. 4.5): distingue
  formalmente os passos $t=1,\ldots,N-1$ de $\sigma$ como *eventos*
  (espaço de busca de HR$^-$ numa fita fixa) dos *passos do motor*
  (ditados pelo crescimento $N\to N+1$ da fita).
- **Proposição 4.6 — Pares diagonais da fita e unicidade do passo mínimo**
  (três partes, todas incondicionais):
  - Parte 1: nomeia e prova que os pares diagonais interiores
    $(a_k, b_{k+1}^{(0)})$ somam $2M^-$, conectando a órbita de $\sigma$
    à geometria da fita por nome explícito.
  - Parte 2: a bijecção da Prop. 4.3(ii) é exactamente a cobertura desses
    pares nomeados — completa o argumento de cobertura com referência
    concreta à fita.
  - Parte 3: prova que $\delta > 1$ quebra *simultaneamente* (i) a
    cobertura bijectiva (órbita fica curta) e (ii) a sincronização com o
    motor (passo seria $2\delta$ em vez de $2$) — formaliza o argumento
    de que deslocamentos arbitrários destroem o motor.
- **Observação de fixação canónica** (após Prop. 4.6): liga a Obs. 3.8
  (unicidade de $W_{i^*}$) e a Prop. 4.6 Parte 3 (unicidade de $\delta$)
  como os dois lados do mesmo argumento de rigidez.
- **Obs. 3.8 actualizada**: adicionada referência cruzada para a Prop. 4.6
  Parte 3 como argumento dual (alterar a janela vs. alterar o passo).
- **Conclusão actualizada**: item 5 adicionado à lista de resultados
  incondicionais, cobrindo a estrutura direccional e a identidade dos pares
  diagonais.

#### Alterado
- Numeração de resultados na Secção 4: Obs. 4.2, Prop. 4.3, Cor. 4.4
  permanecem; inseridos Obs. 4.5, Prop. 4.6, Obs. 4.7 antes da subsecção
  de verificação numérica (4.3 passa a 4.4).

#### Removido
 - Definição de deslocamento anterior. Motivo: quebrava a cadeia do motor se os deslocamentos na grade fossem arbitrários ou desordenados e não considerava os extremos da fita excluidos nos pares diagonais. Isso foi corrigido e redefinido na nova versão.

### [v2.5.0] — Maio 2026
#### Adicionado
- **Paper 5 — Motor de Herança Estrutural** (`bandeira_motor_heranca_formal_2026.tex`):
  fundação algébrica do mecanismo dinâmico de cobertura dos pares de Goldbach.
  - Definição formal da **fita-dobra** $\mathcal{F}_N^\varepsilon$ (matriz $2\times N$
    em percurso zigzag) com dois modos $\varepsilon\in\{0,1\}$ representando dois
    pares consecutivos $2M^-$ e $2M^+$ na mesma estrutura física.
  - **Acoplamento** $\Phi: G_{3,C}\to\mathcal{F}_N$ via condição de sincronização
    $3C=2N$, com fórmula explícita e prova de soma constante
    $\Phi(k)_1+\Phi(k)_2=4N$.
  - **Proposição do par deslocado** (incondicional): os extremos de qualquer
    configuração canónica da janela central $W_{i^*}$ formam sempre um par
    simétrico deslocado na fita, e o próximo passo da fita os alinha gerando
    o novo caso base — independente de primalidade.
  - **Teorema do Motor** (condicional a HR): a cadeia
    $2M_0\to2M_0+2\to2M_0+4\to\cdots$ cobre todos os pares $\geq2M_0$
    como somas de dois primos.
  - **Reformulação de HR** via rotação cíclica $\rho$ na janela central fixa
    $W_{i^*}$: HR é equivalente à recorrência de uma cadeia de Markov cíclica.
  - Lacuna precisamente isolada: apenas a primalidade do par deslocado depende
    de HR — toda a estrutura geométrica é incondicional.

#### Alterado
- Papers anteriores (1--4): a definição de evento restritivo será revista para
  incluir deslocamento mínimo como critério, em vez de apenas variação de $N$,
  para consistência com o acoplamento $\Phi$ do Paper 5.

---

## [v2.4.1] — 2026-05-17

### Paper 06 — Problema B: Desigualdade Estrutural (novo manuscrito)

#### Adicionado
- **"Problema B do Crivo Geométrico: Demonstração da Desigualdade Estrutural"**:
  novo artigo que fornece o **fechamento analítico definitivo** das lacunas L1 e L2,
  estabelecendo que a média de `Ω_N^*` sobre compostos é estritamente maior do que
  sobre primos, sem qualquer teste de primalidade sobre vizinhos.
- **Expansão de Dirichlet de `Ω_N^*(n)`** via a função multiplicativa `α(d) = ∏_{p|d} 1/(p−2)`;
  prova de convergência absoluta da série `Σ α(d)/d → C_M ≈ 1,515` (Lema 2.2 e
  Propriedade 2.3); fórmula de Perron registrada para uso posterior (Lema 2.4).
- **Média global `µ_global(X) → C_M ≈ 1,515`** (Lema 3.1): expansão da soma total
  por inversão de somatório, refinamento do erro a `O(X^{1/2+ε})` via Cauchy‑Schwarz
  e somas de Gauss, alinhamento com a estabilização observada computacionalmente.
- **Redução à função de von Mangoldt e decomposição de Vaughan** (Seção 4):
  separação de `S(X)` em partes Tipo I (`a ≤ U = X^{1/2}`, soma longa em `b`) e
  Tipo II (`a > U`, soma curta em `b`).
- **Fechamento de L1 — Parte Tipo I** (Proposição 5.1):
  - *Cancelamento do termo divergente*: a Parte 1 de `S_a` se anula por
    ortogonalidade de Möbius em progressões aritméticas, extinguindo o termo
    residual `X log X`.
  - *Emergência da constante do crivo*: a Parte 2 sobrevive via a identidade
    `Σ_{gcd(m,D)=1} µ(m) log m / m = −D/φ(D)` e a fatoração multiplicativa
    `Σ_{g|N} µ(g)φ(g)/g = 1/N`, produzindo o fechamento exato
    `Parte 2 = −d / (φ(d) · gcd(d,k))`.
  - Estimativa consolidada via Bombieri‑Vinogradov:
    `S_I(X) = X · C_I + o(X)`, com `C_I = ⅓ Σ_k Σ_d α(d) / (φ(d) · gcd(d,k))`.
- **Fechamento de L2 — Parte Tipo II via Kloosterman‑Weil** (Lema 6.1):
  expansão de Fourier da congruência `ab ≡ −k (mod d)`, redução a somas de
  Kloosterman, aplicação das cotas de Weil (`|Σ e^{2πi(rx+sx̄)/d}| ≤ 2√d`),
  resultado `S_{II}(X) = O(X^{3/4+ε}) = o(X)`.
- **Constante do crivo `C_p ≈ 1,108`** (Lema 7.1): limite de convergência exato
  de `µ_primo(X)`, identificado como `C_I` via fórmula de Abel; extensão de
  Dirichlet sobre o totiente de Euler absolutamente convergente.
- **Teorema principal — Desigualdade estrutural** (Teorema 7.2):
  como `C_M > C_p`, a diferença `µ_global − µ_primo` é estritamente positiva
  para `X` grande; por argumento de média ponderada,
  `µ_comp(X) > µ_global(X) > µ_primo(X)`.
- **Aplicações às Conjecturas de Goldbach e Legendre** (Seção 8):
  formuladas como **Conjecturas de Trabalho 8.2–8.3**; lacuna remanescente
  explicitada: passar da desigualdade de médias para cobertura pontual de todo
  par `2M` exige argumento adicional identificado mas não provado.
- **Seção 9 — Lacunas e hipóteses de trabalho remanescentes**:
  lista sistemática dos pontos em aberto após o fechamento de L1 e L2,
  incluindo extensão da verificação computacional além de `N = 10^5`.
- Observação estrutural central: o problema da paridade — que bloqueia crivos
  multiplicativos clássicos — é reformulado em termos aditivos via complemento
  `C(n,i) = S(i) − n`, abrindo caminho ao método do círculo ou métodos ergódicos.

### README

#### Alterado
- "cinco artigos complementares" → **"seis artigos complementares"**; perspectiva
  analítica adicionada à lista de abordagens.
- Diagrama da linha de Goldbach atualizado: Paper 06 inserido acima de Paper 05
  como **estado atual**, com as constantes `C_M ≈ 1,515` e `C_p ≈ 1,108`.
- Seção "Progresso recente" reescrita para Paper 06 (quatro etapas da prova).
- Estrutura do repositório: pasta `06_problema_b/` adicionada.
- Seção "Artigos": entrada completa do Paper 06 adicionada.
- Tabela resumo: cinco novas linhas de resultados incondicionais (Lemas 3.1,
  6.1, 7.1; Proposição 5.1; Teorema 7.2); Conjecturas 8.2–8.3 adicionadas à
  tabela de lacunas abertas.
- Citação BibTeX do Paper 06 adicionada (`bandeira2026problemab`).
- Exemplo de compilação LaTeX atualizado para `06_problema_b/`.

---

## [v2.3.0] — 2026-05-16

### Paper 04 — Propriedade de Soma Constante (expansão maior)

#### Adicionado
- Artigo expandido de artigo curto para manuscrito completo de 9 seções e 13 páginas.
- **Seção 4 — Corolário Âncora**: prova formal de $f(2,i+1)=S(i)/3$; definição do
  complemento oracle-free $C(n,i)=S(i)-n$; prova de que $C(n,i)$ é sempre par —
  condição necessária para aplicação da Série Singular de Hardy–Littlewood em [Paper 05].
- **Seção 5 — Estrutura aritmética das configurações**: prova de que $D_1$, $D_2$ e
  $C_v$ são progressões aritméticas com razões $2N+2$, $2N-2$ e $2N$; diferenças
  entre linhas sempre iguais a $2N$; uniformidade modular $f(r,c)\equiv 2c-1\pmod{2N}$
  com interpretação das obstruções modulares para $N$ altamente composto.
- **Seção 6 — Por que $G_{3,N}$? O caso privilegiado entre as grades $G_{k,N}$**:
  justificativa formal da escolha de $k=3$ via três condições necessárias simultâneas
  (âncora inteira, complemento par, igualdade tripla $D_1=D_2=C_v$); análise dos
  casos $k=2,3,4,5$ e $k$ geral; tabela resumo; observação conclusiva de que $k=3$
  é o caso natural mínimo — responde explicitamente "por que estudar $G_{3,N}$ e não
  $G_{k,N}$ para $k$ arbitrário?".
- **Seção 7 — Conexão com Goldbach** (expansão): adicionada observação de que
  $p_a+p_c=2\cdot f(2,i+1)$; formalização de $C(n,i)$ como fundamento oracle-free
  de $\Omega^*_N$; observação de que cada $D_1$ primo povoa três instâncias distintas
  de $\bigcup A_p$.
- **Seção 8 — Exemplos numéricos** (expansão): quatro trios primos verificados
  ($D_1$, $D_2$, $C_v$, e caso com obstrução modular $N=1800$) com representações
  binárias e ternárias explícitas.
- Introdução reescrita para explicitar o papel estrutural do artigo na série: fornece
  a base algébrica que torna possível o estimador oracle-free de [Paper 05].

### Paper 03 — Abordagem Unificada

#### Adicionado
- **Nota de revisão na Seção 11.4**: informa que o nó computacional identificado
  foi resolvido em [Paper 05] via Invariante Âncora de [Paper 02]; aponta para
  $\Omega^*_N$ e a verificação computacional correspondente.
- Duas entradas adicionadas à bibliografia: `bandeira2026propriedade` (Paper 02
  expandido) e `bandeira2026ancora` (Paper 05).

### Paper 05 — Invariante Âncora (novo manuscrito)

#### Adicionado
- **"O Invariante Âncora da Grade $G_{3,N}$ e um Estimador Geométrico Oracle-Free
  para a Conjectura de Goldbach"**: novo artigo que resolve o nó computacional
  central do programa do crivo geométrico identificado em [Paper 03, Seção 11.4].
- **Peso oracle-free $\Omega^*_N(n)$**: definido como média da Série Singular de
  Hardy–Littlewood $\mathfrak{S}(C(n,i))$ sobre as janelas de $n$; computável
  sem nenhum teste de primalidade sobre vizinhos.
- **Complemento $C(n,i)=S(i)-n$**: exploração da consequência não desenvolvida
  em [Paper 02] — o Invariante Âncora determina por posição o complemento
  aritmético de qualquer elemento da janela.
- **Verificação computacional** em $G_{3,N}$ para $N$ de $10^3$ a $10^5$:
  $\Omega^*_N$ discrimina $P_1$ de $P_2$ em todos os $N$ testados via testes
  Kolmogorov–Smirnov e Mann–Whitney — incluindo $N \in \{1800, 2400, 3600,
  7200, 12000\}$ com fatoração restrita a $\{2,3,5\}$ onde $\Omega_N$ falha
  completamente.
- **Resultado central**: $\Omega^*_N$ não é aproximação de $\Omega_N$ — correlação
  entre os dois pesos próxima de zero ($r\approx -0{,}06$ para $P_1$), confirmando
  sinais aritmeticamente independentes.
- **Conexão com o método do círculo**: fator $\mathfrak{S}(C)$ identificado como
  núcleo da estimativa de Hardy–Littlewood, conectando o crivo geométrico
  diretamente à heurística clássica sem passar pela estrutura multiplicativa do
  crivo de Selberg.
- **Extensões** a outros problemas clássicos: Legendre, primos gêmeos, Oppermann
  e Brocard formulados como instâncias do mesmo mecanismo geométrico com
  ancoragens distintas; Atlas de Ancoragens (Tabela 2).
- **Direções futuras**: formalização ergódica de $\Omega^*_N$, refinamento via
  funções $L$ de Dirichlet, extensão a grades $k\times N$, testes computacionais
  prioritários (primorial $p_6\#$, estimador $\hat{\pi}_2(a,N)$ para pares específicos).
- Código-fonte disponibilizado em repositório público (`crivo_geometrico_v2.py`).

---

## [v2.2.0] — 2026-05-16

### Paper 03 — Abordagem Unificada

#### Adicionado
- **Seção 12 — Verificação Computacional de Ω_N(n)**: implementação da grade G₃,ₙ
  para N ∈ [10³, 5×10⁵]; cálculo do peso geométrico Ω_N(n) para cada célula;
  classificação em P1 (primo), P2 (semiprimo) e composto via crivo de Eratóstenes.
- Testes não paramétricos **Kolmogorov–Smirnov** e **Mann–Whitney** comparando as
  distribuições de Ω_N sobre P1 e P2; tabela com 14 valores representativos de N.
- Interpretação dos resultados: distribuições estatisticamente distinguíveis para N
  livre de obstruções modulares (N com fator primo ≥ 7 ou N ≳ 10⁵); efeito de
  homogeneização para N = 2^a · 3^b · 5^c pequenos, alinhado com o W-trick da Seção 10.
- Direção do efeito documentada: Ω_N(P1) < Ω_N(P2) < Ω_N(composto), com
  interpretação em termos de densidade decrescente de primos vizinhos.
- **Observação 12.1**: limitações explícitas — significância estatística não implica
  computabilidade sem oráculo de primalidade; circularidade do nó computacional
  (Seção 11.4) permanece intacta.
- Lacuna central enunciada em **cinco linguagens** (combinatória, geometria, crivos,
  teoria ergódica, crivo geométrico).

### Paper 04 — Novo manuscrito (independente)

#### Adicionado
- **"Uma propriedade de soma constante na grade 3×N e as conjecturas de Goldbach"**:
  artigo autocontido e didático derivado da estrutura de G₃,ₙ.
- **Lema da Soma Constante**: prova elementar de que D₁, D₂ e Cᵥ em qualquer
  janela W_i têm a mesma soma S = 3(2N+2i+1), independentemente da primalidade.
- Conexão explícita com Goldbach forte (cada trio primo gera três pares) e
  Goldbach fraca (soma do trio é ímpar > 5, provada por Helfgott 2013).
- Exemplo numérico concreto: N=20, i=3, trio (5, 47, 89) — três representações
  binárias (52, 94, 136) e representação ternária (141) verificadas.
- Nota sobre D₂ e Cᵥ: cada configuração gera três pares distintos dos de D₁.

---

## [v2.1.0] — 2026-05-15

### Principais alterações

- Inclusão de **Nota do Autor** em todos os três artigos, explicitando o escopo exploratório e a separação entre resultados rigorosos e hipóteses heurísticas.
- Artigo geométrico: substituição de "suporte heurístico a Goldbach" por **"Comparação de restritividade"**, com a observação explícita de que a diferença de ordens de grandeza **não oferece evidência a favor ou contra** a conjectura.
- Artigo unificado (Seção 11): adição de advertências qualificando o **Crivo Geométrico** como programa especulativo, não como resultado estabelecido.
- Artigo combinatório: aprimoramento da comparação com Ellman, reforçando a distinção entre infinitude de primos e cobertura pontual.
- Pequenas correções de redação e referências cruzadas.

**Nota:** Nenhum resultado matemático novo foi introduzido. O trabalho permanece como uma investigação estrutural e heurística.

---

## [v2.0.0] — 2026-05-15

### Paper 03 — Abordagem Unificada (versão 2)

#### Adicionado
- **Seção 8 — Redução Dimensional**: formalização de G₃,ₙ como dobramento duplo
  da fita simétrica de Sₙ(p); diagonais D₁/D₂ como artefatos algébricos da dobra.
- **Seção 9 — Análise por Crivos**: Crivo de Selberg (limite superior), Teorema de
  Chen em linguagem de Aₚ ∪ Bₚ, problema da paridade, interpretação geométrica do
  fator ln N como assinatura quantitativa da paridade.
- **Seção 10 — Formalização Ergódica**: espaço simbólico (X, μ_N, T), operador de
  shift, W-trick preciso (W = ∏_{p≤w} p), Hipóteses 10.1 e 10.2 com média de
  Cesàro correta sobre translações.
- **Seção 11 — Crivo Geométrico**: definição formal de Ω_N(n), estimador
  π̂₂(a,N), análise dos dois caminhos de resolução (probabilístico vs. ergódico).
- Lacuna central enunciada em quatro linguagens equivalentes.

#### Corrigido
- W-trick: descrição vaga substituída por definição precisa com φ(W)/W.
- Typo "quarta direita" → "quarta direção".
- Parágrafo de organização da Seção 1 atualizado para refletir todas as seções.

---

## [v1.0.0] — 2026-05-02 / 2026-05-10

### Paper 01 — Estrutura Combinatória
- Definição de Sₙ(p), Qₚ, Aₚ.
- Proposição de simetria, condição necessária (Prop. 3.5), propagação condicional.
- Teorema de equivalência com Goldbach (Teo. 3.17).
- Identificação explícita da lacuna central (Obs. 3.10).
- Remoção de argumento circular presente em versões anteriores.

### Paper 02 — Saturação Geométrica
- Grade G₃,ₙ com mapeamento linha-a-linha f(r,c).
- Hipótese de quasi-independência de Cramér.
- Divergência de Σ P(Eᵢ) (Lema 4.4 com prova corrigida via substituição u=ln x).
- Saturação via Segundo Lema de Borel-Cantelli (Prop. 4.3, condicional).
- Kᵤ ~ 8N/(ln N)³, limiar N* ≈ 1,1×10⁴ (direto) e N* ≈ 1,1×10⁶ (estrito).
- Comparação com estimativa de Hardy-Littlewood.

### Paper 03 — Abordagem Unificada (versão 1)
- Elo central: cada trio primo em W_i gera 3 elementos de ∪Aₚ (Prop. 5.2).
- Corolário: Goldbach equivale à cobertura total pelas testemunhas geométricas.
- Fator ln N entre Kᵤ e G(N) identificado.