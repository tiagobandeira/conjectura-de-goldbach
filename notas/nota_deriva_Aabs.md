# Nota Técnica: Deriva de A_abs e Crescimento de k_abs — Resultados Estendidos até N = 10⁸

**Série:** Motor de Herança Estrutural — Conjectura de Goldbach  
**Autor:** Tiago Bandeira  
**Data:** Maio de 2026  
**Status:** Nota de descoberta (Artigo 10 – abordagem experimental)

---

## Resumo

A extensão do experimento de âncora absoluta para múltiplos N entre 10⁶ e 10⁸ revelou dois comportamentos não triviais:

1. **A constante `A_abs` não é estável** – varia entre 6,9 e 10,9, com possível tendência a estabilizar na faixa 10–11 para N ≥ 10⁷, mas com um salto em 10⁸ (10,94).  
2. **O número de janelas `k_abs` necessário para cobertura completa (gap máximo = 2) cresce aproximadamente como `5,5·log N`**, ou seja, **logaritmicamente** com o limite superior N.

Adicionalmente, confirma-se que a **fração de C cobertos atinge 100%** (gap ≤ 2), validando o critério de parada.

---

## 1. Dados brutos da extensão

| N           | p_abs | A_abs | k_abs | log N | k_abs / log N |
|-------------|-------|-------|-------|-------|---------------|
| 1.000.000   | 269   | 7,415 | 55    | 13,82 | 3,98          |
| 2.000.000   | 269   | 6,932 | 55    | 14,51 | 3,79          |
| 5.000.000   | 389   | 9,218 | 75    | 15,42 | 4,86          |
| 10.000.000  | 449   | 10,021| 85    | 16,12 | 5,27          |
| 20.000.000  | 479   | 10,097| 90    | 16,81 | 5,35          |
| 50.000.000  | 509   | 9,987 | 95    | 17,73 | 5,36          |
| 100.000.000 | 587   | 10,938| 105   | 18,42 | 5,70          |

**Observações:**

- Entre 10⁷ e 5×10⁷, `A_abs` permanece praticamente constante (≈10,0).  
- O valor `A_abs = 10,94` em 10⁸ pode ser um desvio estatístico ou o início de uma deriva muito lenta.  
- `k_abs / log N` cresce de ~4 para ~5,7, sugerindo que a lei `k_abs ∼ c·log N` é compatível, com `c` aumentando lentamente ou convergindo para ≈5,5.

---

## 2. Interpretação dos achados

### 2.1 A ilusão da constante `A_abs ≈ 10`

A regra prática `p_max ≈ 10·log N·log log N` é útil como **limite superior folgado** para N ≥ 10⁷, mas **não é uma constante universal**. A deriva observada (7,4 → 10,9) é de aproximadamente 47% entre 10⁶ e 10⁸, indicando que o teto de busca cresce **ligeiramente mais rápido** que `log N·log log N`.

**Conjectura empírica:**  
`A_abs(N) → A∞` com `A∞` entre 10 e 11, ou então `A_abs(N) ∼ c·log log N` (crescimento ainda mais lento). Mais pontos (N = 2×10⁸, 5×10⁸) serão necessários para decidir.

### 2.2 Crescimento logarítmico de `k_abs`

O número de janelas necessárias escala como `k_abs ∼ (5,5 ± 0,5)·log N`. Isto é **extremamente favorável** para o motor: para N = 10⁹, estima-se `k_abs ≈ 5,5·log(10⁹) ≈ 5,5·20,7 ≈ 114` janelas. Para N = 10¹², cerca de 150 janelas.

**Implicação:** A complexidade do scanner (número de passos para cobrir todos os C) cresce apenas polilogaritmicamente, não linearmente.

### 2.3 Cobertura total (gap máximo = 2) implica fração 1

Os valores de `frac_cobertura` são todos 0,999996 ou superiores, e para N ≥ 10⁷ são exatamente 1 (dentro da precisão inteira). Isso mostra que o critério `gap_max ≤ 2` é equivalente à cobertura de todos os C pares no intervalo, sem exceções.

---

## 3. Próximos experimentos (roteiro)

Com base no que os dados já sugerem, os seguintes experimentos são prioritários para gerar novas descobertas:

### 🔬 Experimento 2 – Análise da sequência completa de âncoras

**Objetivo:** Entender não apenas a maior âncora, mas **todas** as âncoras usadas até a cobertura completa.

**Procedimento:** Modificar o script para salvar a lista `ancoras_usadas` (em ordem de uso).  
**Perguntas a responder:**
- Quantas âncoras são necessárias para cobrir 50% dos C? 90%? 99%?  
- Existe uma âncora “herói” que cobre muitos C sozinha?  
- Qual a distribuição da eficiência (cobertura por âncora)? Segue uma lei de potência?

**Valor:** Permite projetar um algoritmo de cobertura guloso e possivelmente reduzir ainda mais `k_abs`.

### 🔬 Experimento 3 – Ordem das âncoras importa?

**Objetivo:** Testar se a ordem crescente (a atual) é ótima ou se uma ordem aleatória/ordenada por cobertura poderia reduzir `k_abs` ou `p_max`.

**Procedimento:** Embaralhar a lista de âncoras e repetir o processo de saturação. Comparar `k_abs` e `p_max` resultantes.  
**Hipótese:** Se a ordem não importar, a cobertura é “comutativa” – o que indicaria independência total. Se importar, podemos buscar a ordem ótima.

### 🔬 Experimento 4 – Validação do modelo de Poisson

**Objetivo:** Comparar a cobertura observada com a predição do modelo `P(não coberto) = exp(-k·ρ(C))`, onde `ρ(C) ≈ 19 / log²(C)` (fração de Wi ativas).

**Procedimento:** Para um N fixo (ex: 10⁷), calcular, para cada C, o número esperado de ativações após k janelas e comparar com o observado.  
**Métrica:** Teste de Kolmogorov‑Smirnov para os gaps de cobertura.

**Valor:** Se confirmado, o modelo de Poisson com descorrelação (correlação 2,5%) torna‑se uma heurística quantitativa para a saturação.

### 🔬 Experimento 5 (opcional) – Extrapolação para N = 2×10⁸ e 5×10⁸

**Objetivo:** Verificar se `A_abs` continua subindo (passando de 11) ou se retorna à faixa 10–11.

**Custo:** Estimado em ~20 minutos para 2×10⁸, ~2 horas para 5×10⁸ (com busca de âncora até 2000). Viável em uma máquina com 16 GB RAM.

---

## 4. Conclusão parcial

Os dados estendidos mostram que:

- O teto de busca `p_max` cresce **um pouco mais rápido** que `log N·log log N`, com `A_abs` variando entre 7 e 11.  
- O número de janelas `k_abs` escala **logaritmicamente** com N – um resultado forte a favor da eficiência do motor.  
- Não há “C teimosos” que exijam âncoras extraordinariamente grandes: a cobertura é sempre completa com menos de 110 janelas até 10⁸.

A próxima fase experimental deve focar na **estrutura interna da cobertura** (Experimentos 2–4), para transformar observações empíricas em um modelo preditivo.

---

*Nota redigida em maio de 2026, com base nos outputs do script `bandeira_ancora_absoluta_extendida.py`.*