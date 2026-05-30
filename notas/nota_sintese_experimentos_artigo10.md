# Nota de Síntese: Experimentos Numéricos e Leis de Escala do Motor de Herança Estrutural

**Série:** Conjectura de Goldbach – Motor de Herança Estrutural  
**Autor:** Tiago Bandeira  
**Data:** Maio de 2026  
**Status:** Síntese para o Artigo 10 (Abordagem Experimental)

---

## 1. Objetivo e escopo

Esta nota reúne os resultados das simulações numéricas realizadas para caracterizar o comportamento do **Motor de Herança Estrutural** sob o regime de âncora absoluta (multieixo). Os experimentos cobrem escalas de `N` (limite superior dos `C` pares) de 10⁶ a 10⁸, com ênfase na saturação da cobertura, na evolução do número de janelas `k*` e da maior âncora `p_max`, na eficiência da ordem crescente de âncoras e na validação de modelos heurísticos de Poisson.

Os resultados fornecem evidências empíricas para os Lemas 1–4 da `nota_cobertura_v3.md` e fundamentam as leis de escala propostas no Artigo 10.

---

## 2. Experimentos realizados

### Experimento 1 (baseline) – Âncora absoluta vs. restrita
- **Arquivo:** `bandeira_ancora_absoluta.py` (versão extendida)
- **Descrição:** Para cada `N`, varre primos ≥5 até 5000, usando a regra absoluta (qualquer primo) e a regra restrita (`8j-5`). Mede `p_max` e `k*` (número de âncoras até gap máximo ≤2).
- **Resultado principal:** A regra absoluta reduz `p_max` de ~3200 para ~587 em N=10⁸, com `A_abs ≈ 10` (vs `A_restrita ≈ 60`). A deriva de `A_abs` é suave (~7–11).

### Experimento 2 – Sequência completa de âncoras e cobertura acumulada
- **Arquivo:** `bandeira_experimento2_sequencia_ancoras.py`
- **Descrição:** Registra, para cada `N`, a ordem, a âncora, o número acumulado de `C` cobertos e o gap máximo (a cada 5 âncoras). Salva CSV em `experimento2_resultados/`.
- **Resultados principais:**
  - A âncora `5` cobre sozinha ~16–20% de todos os `C`.
  - 50% da cobertura é atingida pela âncora `11` ou `13` (ordem 3–4).
  - 90% da cobertura é atingida pela âncora `37–47` (ordem 10–13).
  - 99% da cobertura é atingida pela âncora `73–107` (ordem 19–26).
  - A cobertura final é sempre 100% (gap máximo = 2).
> **$HR^{-}$ (Hipótese Restritiva Fraca):** Dado o par alvo $2M+2 = 6C$, a condição $HR^{-}$ é satisfeita se, na varredura do scanner sobre a grade canônica, existir **pelo menos uma janela $W_i$** (entre as $\lceil(N-1)/4\rceil$ janelas do intervalo) tal que, em **um dos seus quatro eixos** (D1, D2, Cv, Lc), os dois extremos $E_1$ e $E_2$ sejam ambos primos. Em termos de âncora $p$ (onde $p = E_1$), isso equivale à primalidade de $6C - p$. O modelo do motor não impõe que a janela seja fixa; a cada iteração, ela pode variar.

### Experimento 3 – Ordem aleatória das âncoras
- **Arquivo:** `ordem_aleatorias_das_ancoras.py`
- **Descrição:** Para `N=10⁷`, compara a ordem crescente com 10 ordens aleatórias das mesmas âncoras. Mede `k*` e `p_max`.
- **Resultado:** Ordem crescente é drasticamente superior: `k*` médio aleatório = 96 ± 9.4 vs 85; `p_max` médio aleatório = 971 ± 522 vs 449. A ordem natural (primos pequenos primeiro) é (quase) ótima.

### Experimento 4 – Validação do modelo de Poisson (média)
- **Arquivo:** `validacao_do_modelo_de_poisson.py`
- **Descrição:** Para cada `N`, calcula a cobertura final predita pelo modelo `1 - exp(-k·ρ_medio)` com `ρ_medio = 19 / log²(N/2)`. Compara com a cobertura observada (100%).
- **Resultado:** A predição final é ~99,8% (erro de 0,2%). O erro médio ao longo da curva é ~9–10%, com erro máximo ~28–38% nos primeiros passos. O modelo é uma boa aproximação de primeira ordem, mas subestima ligeiramente a cobertura final (devido à anticorrelação negativa entre janelas).

### Experimento 5 – Evolução do gap máximo
- **Arquivo:** `analisar_sequencias_ancoras.py` (extrai gaps dos CSVs do Exp. 2)
- **Descrição:** Plota o gap máximo (escala log) versus a ordem da âncora.
- **Resultado:** O gap máximo decai **exponencialmente** com a ordem (reta no gráfico log-linear). O gap inicial (após âncora 5) cresce lentamente com `N` (de 82 para 196).

### Experimentos auxiliares – Leis de escala
- **Arquivo:** `lei_empirica.py`
- **Descrição:** Ajusta regressões lineares para `k*(N)` e `A_abs(N)`.
- **Resultado:**
  - `k*(N) ≈ 5,5·log N` para N ≥ 10⁷ (R² > 0,95).
  - `A_abs(N) ≈ 10,3 ± 0,5` para N ≥ 10⁷.

---

## 3. Tabelas consolidadas

### Tabela 1 – Comparação entre regimes de âncora (N = 10⁷)

| Regime           | p_max | A     | k*   | Overhead vs. absoluta |
|------------------|-------|-------|------|----------------------|
| Restrita (8j-5)  | 2083  | 46,49 | 80   | +363,9%              |
| Expandida (2 classes) | 877   | 19,57 | 80   | +95,3%               |
| Absoluta (multieixo) | 449   | 10,02 | 85   | 0%                   |

### Tabela 2 – Evolução de k* e A_abs com N (regime absoluto)

| N           | log N | k* obs | k*/log N | p_max obs | A_abs = p_max/(log N·log log N) |
|-------------|-------|--------|----------|-----------|-------------------------------|
| 1.000.000   | 13,82 | 55     | 3,98     | 269       | 7,42                          |
| 2.000.000   | 14,51 | 55     | 3,79     | 269       | 6,93                          |
| 5.000.000   | 15,42 | 75     | 4,86     | 389       | 9,22                          |
| 10.000.000  | 16,12 | 85     | 5,27     | 449       | 10,02                         |
| 20.000.000  | 16,81 | 90     | 5,35     | 479       | 10,10                         |
| 50.000.000  | 17,73 | 95     | 5,36     | 509       | 9,99                          |
| 100.000.000 | 18,42 | 105    | 5,70     | 587       | 10,94                         |

**Média (N ≥ 10⁷):** `k*/log N ≈ 5,5`; `A_abs ≈ 10,3 ± 0,5`.

### Tabela 3 – Marcos de cobertura (N = 10⁷)

| Marco | Ordem da âncora | Âncora típica | % de C cobertos |
|-------|----------------|---------------|-----------------|
| 50%   | 3–4            | 11 ou 13      | 55–60%          |
| 90%   | 10–13          | 37–47         | 90–92%          |
| 99%   | 19–26          | 73–107        | 99,0–99,2%      |
| 100%  | 85             | 449           | 100%            |

### Tabela 4 – Gap máximo após algumas âncoras (N = 100M)

| Âncora | Ordem | Gap máx |
|--------|-------|---------|
| 5      | 1     | 196     |
| 7      | 2     | 98      |
| 11     | 3     | 56      |
| 13     | 4     | 46      |
| 37     | 10    | 44      |
| 59     | 15    | 38      |
| 103    | 25    | 34      |
| 181    | 40    | 18      |
| 239    | 50    | 8       |
| 449    | 85    | 4       |
| 587    | 105   | 2       |

---
> "Para cada $C$ testado, **existe alguma janela** $W_i$ cujo eixo fornece um par de primos. Isso é equivalente a dizer que o conjunto das âncoras (primos $p$) mapeados nos eixos cobre todos os valores de $C$."

## 4. Gráficos gerados

- `cobertura_acumulada.png` – Fração de C cobertos vs. ordem da âncora, para todos os N. Mostra invariância de escala.
- `decaimento_gap.png` – Gap máximo (escala log) vs. ordem da âncora. Mostra decaimento exponencial.
- `leis_escala.png` – Ajustes lineares para `k*` vs `log N` e `A_abs` vs N.

---

## 5. Leis empíricas deduzidas (para N ≥ 10⁷)

1. **Número de janelas necessário para cobertura completa**  
   `k*(N) ≈ 5,5·log N`  
   *Complexidade logarítmica – altamente eficiente.*

2. **Maior âncora necessária**  
   `p_max(N) ≈ (10,3 ± 0,5)·log N·log log N`  
   *O coeficiente estabiliza entre 10 e 11 para N grande.*

3. **Saturação exponencial da fração de não cobertos** (Lema 2 confirmado)  
   `P(C não coberto por U_k) ≈ exp(-α(N)·k)`, com `α(N) ∼ 3,23 / log N`.

4. **Decaimento exponencial do gap máximo**  
   `gap_max(k) ∼ G₀·exp(-β·k)`, com `β ≈ 0,05` independente de N (após escala).

---

## 6. Impacto na série de artigos



- **Artigos 5 e 6 (álgebra e espectral):** Os experimentos validam a separação entre camada algébrica (soma constante, eixos de `W_i`) e camada aritmética (HR⁻). A saturação rápida mostra que a geometria multieixo é suficiente para tornar o gargalo apenas representacional, não aritmético.

- **Artigo 7 (configuração canônica):** A descoberta de que a âncora `5` cobre ~16% dos `C` está diretamente ligada ao par canônico `(C-1, 5C+1)` com `C-1 = 5` (ou seja, `C=6`). Isso explica a anomalia do resíduo `C ≡ 6 (mod 30)` (único caso com `C=6`). O papel especial do primo 5 na herança ativa é agora numericamente quantificado.

- **Artigo 8 (operador de transferência):** A eficiência da ordem crescente de âncoras sugere que o operador `ℒ_T` deve respeitar uma hierarquia de “tamanho” (primos menores primeiro). Isso pode ser usado para refinar a condição de ganho `γ(N) > log N / log(5N)`, já que as âncoras pequenas são responsáveis pela maior parte da cobertura.

- **Artigo 10 (este, experimental):** As leis de escala acima fornecem limites superiores explícitos para o esforço computacional do motor e uma base para conjecturas sobre a existência de infinitas âncoras que garantem a cobertura total.

---

## 7. Conjecturas e trabalhos futuros

Com base nos resultados, propomos:

1. **Conjectura da estabilidade de A_abs:** Para N → ∞, `p_max(N) / (log N·log log N) → A_∞` com `A_∞ ∈ [10, 11]`.

2. **Conjectura da linearidade logarítmica:** `k*(N) / log N` converge para uma constante `c_k ≈ 5,5`.

3. **Conjectura da universalidade da cobertura:** A curva de cobertura acumulada (em função da ordem normalizada) é invariante para todo N suficientemente grande.

**Trabalhos futuros sugeridos:**
- Estender as simulações até N = 10⁹ (amostragem estratificada) para confirmar as tendências.
- Investigar a estrutura dos últimos 1% de C não cobertos (aqueles que exigem as maiores âncoras) – será que eles se acumulam em classes modulares específicas?
- Refinar o modelo de Poisson usando `ρ(C)` individual (em vez da média) e incorporar a anticorrelação de –2,5% para reduzir o erro para < 5%.
- Tentar uma prova analítica da lei `k* ∼ c·log N` usando o método de crivo e a independência assintótica das janelas.

---

## 8. Referências aos scripts e dados

Todos os scripts estão disponíveis na pasta `ponto_de_parada/` (ou conforme organização local). Os principais são:

- `bandeira_ancora_absoluta_extendida.py` – gera os dados de base.
- `bandeira_experimento2_sequencia_ancoras.py` – gera os CSVs com sequência de âncoras e cobertura.
- `analisar_sequencias_ancoras.py` – produz relatórios e tabelas de marcos.
- `ordem_aleatorias_das_ancoras.py` – compara ordem crescente vs aleatória.
- `validacao_do_modelo_de_poisson.py` – valida o modelo de Poisson médio.
- `lei_empirica.py` – ajusta as leis de escala e gera gráficos.

Os dados brutos (CSVs) estão em `experimento2_resultados/` e os gráficos finais em arquivos `.png`.

---

## 9. Conclusão da síntese

Os experimentos 1 a 5 fornecem um retrato quantitativo detalhado do Motor de Herança Estrutural operando no regime absoluto (multieixo). As descobertas principais são:

- A cobertura completa de todos os `C` pares até 10⁸ é garantida com **apenas 105 âncoras** (primos até 587), e o número de janelas cresce apenas **logaritmicamente** com N.
- A ordem crescente de âncoras é quase ótima; qualquer ordem aleatória exige muito mais esforço.
- O gap máximo decai exponencialmente, confirmando a **saturação geométrica**.
- O modelo de Poisson com densidade `ρ(C) = 19/log²(C)` é uma boa heurística de primeira ordem, mas subestima ligeiramente a cobertura (devido à anticorrelação negativa).

Estes resultados validam as hipóteses estruturais dos artigos anteriores e abrem caminho para uma análise mais aprofundada da Hipótese Restritiva HR⁻ no contexto espectral do Artigo 6.

---

*Nota redigida em maio de 2026, como base para o Artigo 10 da série.*