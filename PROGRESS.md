# Progresso da Pesquisa – Motor de Herança Estrutural

*Última atualização: Junho de 2026 (v2.7.8)*

Este arquivo documenta o **estado atual** da investigação, separando resultados já consolidados (incondicionais) das conjecturas e lacunas abertas.

---

## ✅ Resultados incondicionais (provados)

- Soma constante da fita (`2M⁻` nas colunas, `2M⁺` nas diagonais) e acoplamento `Φ` com `3C=2N` (Papers 04, 07).
- Invariante Âncora e peso `Ω_N^*` oracle‑free (Paper 05).
- Desigualdade estrutural: `μ_comp > μ_global > μ_primo` (Paper 06).
- Motor de Herança: estrutura direcional de `σ`, identidade dos pares diagonais, unicidade do passo `δ=1` (Paper 07).
- Sistema dinâmico `(X_N,μ_N,T)` com espectro discreto puro e entropia zero (Paper 08).
- Equivalência `HR⁻ ⟺ F̂(0) > 0` e cancelamento de todas as frequências não nulas (`ŵ(j)→0`, via Green‑Tao‑Ziegler) – Paper 08.
- **Leis de escala empíricas** (até `N=10⁹`):  
  - `k*(N) ≈ 6,3 log N` (convergente a partir de `N≥10⁷`)  
  - `p_max(N) ≈ 11,8 log N log log N` (coeficiente `A_abs` estabiliza em ~11,8)  
  (Papers 10 e 11, estendido na versão 2.7.8)
  - ⚠️ **Escopo:** as duas leis referem-se aos alvos `n ≡ 0 (mod 12)` — um sexto
    dos pares —, não a todos os pares. Para todo par a ordem exigida é
    `log²n · log log n`: medição exaustiva até `10⁸` dá `max g(n) = 1093`
    (Paper 10, Subsecção 3.5; `lean/TrustLedger.md`, E‑5).
- **Quase‑independência das ativações** no regime absoluto: correlação média < 0,4%, decrescente com `N` (Paper 10).
- **Decaimento exponencial do gap máximo**: `gap_max(k) ≈ G_0 e^{-βk}`, com `β≈0,20` estável (verificado até `10⁸`) – Paper 11.
- **Derivação analítica das constantes geométricas**:  
  - Número efetivo de eixos independentes: `n_ef = 36/π² ≈ 3,6476` (obtido do produto euleriano excluindo o primo 3).  
  - Constante de janelas ativas: `c = 4 n_ef C₂ ⟨𝔖⟩ ≈ 21`, consistente com dados empíricos.  
  (Notas `nota_derivacao_beta_kstar_v2.md` e `verificar_constante_c.py`)

---

## 🔄 Resultados condicionais / heurísticos

- **Conjectura da Âncora Absoluta** (Paper 10, atualizada na v3.0): todo número par suficientemente grande é soma de dois primos com o menor primo `O(log M log log M)`. Suportada por evidência até `10⁹`.
- **Separação estrutural** do gap: eliminação do gap exige `O(log log N)` âncoras; eliminação dos pontos isolados residuais exige `O(log N)` âncoras – isso explica `k* ∼ 6,3 log N` e mostra que o union bound ingênuo (`O(log³ N)`) é pessimista (Papers 11 e 12).
- **Prova condicional sob GRH** (Paper 12):  
  *Se a Hipótese de Riemann Generalizada for verdadeira, então o processo guloso atinge cobertura total para todo N suficientemente grande, implicando HR⁻ e, pelo Teorema do Motor, a Conjectura de Goldbach (forte).*  
  Esta prova usa a cota inferior `ρ_eixo(C) ≥ c₀ / log² C` que a GRH fornece, e o argumento dos dois regimes (âncoras pequenas via Mertens, eliminação das classes mod 8).
- **Cota inferior `ŵ(0) > 0`** (positividade da componente de frequência zero): equivale à Conjectura de Goldbach; pode ser provada sob GRH (condicional) ou aceita como heurística empírica.

---

## ⚪ Lacunas abertas

- Provar `ŵ(0) > 0` **incondicionalmente** – o obstáculo central.
- Formalizar rigorosamente a propriedade de mistura do processo de cobertura a partir da descorrelação espectral (Paper 08 + nilsequências).
- Refinar o modelo de Poisson incorporando a correlação positiva residual de 0,3% para melhorar a predição da variância (a média já é acertada).
- Extensão das simulações para `N=10^{10}` (por amostragem) para confirmar a convergência de `A_abs` e `β`.

---

## 📊 Resumo visual (atualizado para v2.7.8)

```text
                              Goldbach
                                 ↑
                    ┌────────────┴────────────┐
                    │   ŵ(0) > 0  (em aberto) │ ← equivalente a Goldbach
                    └────────────┬────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
   Incondicional:         Condicional:              Empírico (v2.7.8):
   - HR⁻ ↔ F̂(0)>0         - ŵ(0)>0 sob GRH          - Leis de escala até 10⁹
   - ŵ(j≠0)→0             - Prova condicional       - Decaimento exp. do gap
   - Espectro discreto       da cobertura total     - Correlação <0,4%
   - Motor + invariantes     (Paper 12)             - n_ef = 36/π², c ≈ 21
   - Derivação de n_ef, c
```

---

## Próximos passos

- Finalizar o Paper 12 (transformar o esboço em artigo formal, com a prova condicional sob GRH bem estruturada).
- Divulgar os resultados (preprints, repositório, contato com a comunidade).
- Explorar a possibilidade de uma prova incondicional usando apenas a heurística de Hardy‑Littlewood (sem GRH) ou técnicas de crivo mais avançadas.

---

## 🔬 Camada de verificação formal (Lean 4)

O repositório inclui agora `lean/`: formalização em Lean 4 do **núcleo
combinatório/algebraico** da série — sem Mathlib, sem `sorry`, sem axiomas
próprios (`propext`, `Quot.sound` apenas).

- **87 teoremas verificados** por máquina, em 11 módulos.
- Cobre: Lema da Soma Constante, Invariante Âncora, paridade do complemento,
  estrutura das progressões aritméticas e generalização `k×N` (Paper 04);
  fita‑dobra, diagonais e acoplamento `Φ` (Paper 07 §2–3); Teorema do Motor
  (Paper 07 §8); equivalência espectral `HR⁻ ⟺ F̂(0) > 0` (Paper 08 §6);
  e a camada de herança — enumeração completa da fita, passo `+2`, cadeia
  certificada, eixos de `W_i` e limite `mod 4`.
- [`lean/TrustLedger.md`](lean/TrustLedger.md) mapeia **cada afirmação** dos 12
  papers ao seu estatuto (provado / condicional / empírico) e registra
  4 erratas (**E‑1…E‑4**) e 2 observações sobre economia lógica (**R‑1**, **R‑2**),
  incluindo a anatomia do colapso de `HR⁻` (ver R‑1, continuação).

Compilar: `powershell -ExecutionPolicy Bypass -File lean\build.ps1`.

Para detalhes históricos de versões, veja o [`CHANGELOG.md`](CHANGELOG.md).