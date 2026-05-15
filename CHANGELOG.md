# Changelog

Todas as mudanças significativas neste projeto são documentadas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

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