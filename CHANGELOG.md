# Changelog

Todas as mudanças significativas neste projeto são documentadas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

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

## [v2.1.0] – 2026-05-15

### Principais alterações

- Inclusão de **Nota do Autor** em todos os três artigos, explicitando o escopo exploratório e a separação entre resultados rigorosos e hipóteses heurísticas.
- Artigo geométrico: substituição de “suporte heurístico a Goldbach” por **“Comparação de restritividade”**, com a observação explícita de que a diferença de ordens de grandeza **não oferece evidência a favor ou contra** a conjectura.
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