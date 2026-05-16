# Changelog

Todas as mudanças significativas neste projeto são documentadas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

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