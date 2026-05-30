# Progresso da Pesquisa – Motor de Herança Estrutural

*Última atualização: Maio de 2026 (v2.7.7)*

Este arquivo documenta o **estado atual** da investigação, separando resultados já consolidados (incondicionais) das conjecturas e lacunas abertas.

---

## ✅ Resultados incondicionais (provados)

- Soma constante da fita (`2M⁻` nas colunas, `2M⁺` nas diagonais) e acoplamento `Φ` com `3C=2N` (Papers 04, 07).
- Invariante Âncora e peso `Ω_N^*` oracle‑free (Paper 05).
- Desigualdade estrutural: `μ_comp > μ_global > μ_primo` (Paper 06).
- Motor de Herança: estrutura direcional de `σ`, identidade dos pares diagonais, unicidade do passo `δ=1` (Paper 07).
- Sistema dinâmico `(X_N,μ_N,T)` com espectro discreto puro e entropia zero (Paper 08).
- Equivalência `HR⁻ ⟺ F̂(0) > 0` e cancelamento de todas as frequências não nulas (`ŵ(j)→0`, via Green‑Tao‑Ziegler) – Paper 08.
- **Leis de escala empíricas** (até `N=10⁸`):  
  - `k*(N) ≈ 5,5 log N`  
  - `p_max(N) ≈ 10,3 log N log log N`  
  (Papers 10 e 11)
- **Quase‑independência das ativações** no regime absoluto: correlação média < 0,4%, decrescente com `N` (Paper 10).
- **Decaimento exponencial do gap máximo**: `gap_max(k) ≈ G_0 e^{-βk}`, com `β≈0,20` estável (Paper 11).

---

## 🔄 Resultados condicionais / heurísticos

- **Conjectura da Âncora Absoluta** (Paper 10): todo par par suficientemente grande é soma de dois primos com o menor primo `O(log M log log M)`. Suportada por evidência até `10⁸`.
- **Separação estrutural** do gap: eliminação do gap exige `O(log log N)` âncoras; eliminação dos pontos isolados residuais exige `O(log N)` âncoras – isso explica `k* ∼ 5,5 log N` e mostra que o union bound ingênuo (`O(log³ N)`) é pessimista (Paper 11).
- **Cota inferior `ŵ(0) > 0`** (positividade da componente de frequência zero): equivale à Conjectura de Goldbach; pode ser provada sob GRH (trabalho futuro).

---

## ⚪ Lacunas abertas

- Provar `ŵ(0) > 0` incondicionalmente (ou mesmo sob GRH) – este é o obstáculo central.
- Estender as simulações até `N=10⁹` para confirmar a estabilização de `A_abs` e `β`.
- Refinar o modelo de Poisson incorporando a correlação positiva residual de 0,3% para melhorar a predição da variância (já a média é acertada).
- Formalizar a propriedade de mistura do processo de cobertura a partir da descorrelação espectral (Paper 08 + nilsequências).

---

## 📊 Resumo visual (atualizado)

```text
                              Goldbach
                                 ↑
                    ┌────────────┴────────────┐
                    │   ŵ(0) > 0  (em aberto)  │ ← equivalente a Goldbach
                    └────────────┬────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
   Incondicional:         Condicional:              Empírico (v2.7.7):
   - HR⁻ ↔ F̂(0)>0         - ŵ(0)>0 sob GRH          - Leis de escala
   - ŵ(j≠0)→0             - Conjectura da           - Decaimento exp. do gap
   - Espectro discreto       Âncora Absoluta        - Correlação <0,4%
   - Motor + invariantes                             - Separação estrutural
```

---

## Próximos passos

- Provar `ŵ(0) > 0` condicionalmente (GRH) ou explorar recorrência ergódica para contornar GRH.
- Submeter os Papers 10 e 11 para publicação (como preprints).
- Realizar simulações amostrais até `N=10⁹` para verificar a estabilidade das constantes.

---

Para detalhes históricos de versões, veja o [`CHANGELOG.md`](CHANGELOG.md).