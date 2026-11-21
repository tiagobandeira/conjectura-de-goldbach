## Verificação Formal e Correção de Escopo: a série auditada por máquina

Esta release apresenta a versão **2.8.0**, que consolida a série sob uma nova
camada: a **verificação formal em Lean 4** do núcleo combinatório e algébrico dos
artigos, acompanhada de um **mapa de confiança** que classifica cada afirmação
como provada, condicional ou empírica. É também uma release de **correção**: o
domínio de validade das leis de escala é declarado explicitamente nos Papers 10,
11 e 12, e uma errata do Paper 04 é registada.

---

### O que há de novo

**Verificação formal (novo diretório `lean/`).** 87 teoremas verificados por
máquina, em 11 módulos, sem `sorry` e sem Mathlib. Cobrem:

- Lema da Soma Constante, Invariante Âncora, paridade do complemento,
  progressões aritméticas e generalização `k×N` (Paper 04);
- fita-dobra, diagonais e acoplamento `Φ` (Paper 07, §2–3);
- teorema do trio: primo ⇒ três representações binárias + uma ternária;
- Teorema do Motor (Paper 07, §8) e `HR⁺ ⇒ HR⁻`;
- equivalência espectral `HR⁻ ⟺ F̂(0) > 0` e `0 ≤ F̂(0) ≤ 1` (Paper 08, §6);
- alcance exato das janelas (membro menor `≤ n/4`) e `Φ` como reflexão.

**`lean/TrustLedger.md`.** Mapa afirmação por afirmação dos 12 artigos, com o
estatuto de cada uma (✅ provado em Lean · 🟡 provado no paper, não formalizado ·
🔵 condicional · ⚪ empírico), 5 erratas e 3 resultados negativos formalizados.

**Três resultados negativos, provados.** A formalização estabeleceu, sem margem
para interpretação: (i) a fita-dobra **enumera todos** os pares que somam `4N`,
logo «estar na fita» não restringe nada; (ii) a equivalência espectral é
tautológica — não usa nenhuma propriedade dos primos; (iii) a cadeia de
transporte **não itera**: como `3 | p(p+2)(p+4)`, uma cadeia certificada tem no
máximo dois passos.

**Correção de escopo (Papers 10, 11 e 12).** O script de cobertura marca um valor
de `C` quando `p + q ≡ 0 (mod 6)` e `C = (p+q)/6` é par, de modo que os alvos
cobertos são `n ≡ 0 (mod 12)` — **um sexto dos pares**, não todos. As leis
`k* ~ 6,3 log N` e `p_max ~ 11,8 log N log log N` são válidas nesse domínio;
para todos os pares a ordem exigida é `log² n · log log n`. Nova **Subsecção 3.5**
do Paper 10, com reprodução independente, contraexemplo (`g(60 119 912) = 1093`
contra `578` previstos) e a **Conjectura C′** restrita ao domínio.

**`scripts/lei_ancora_verificacao.py`.** Verificação independente e reproduzível
da lei da âncora: mede `g(n) = min{p : n − p primo}`, reproduz a tabela do
Paper 10 no domínio `n ≡ 0 (mod 12)` e documenta o contraexemplo fora dele.

**Errata do Paper 04 (registada, não silenciada).** O enunciado da Proposição 5.4
(`k = 4`: complemento «sempre par») contradiz a sua própria demonstração e a
tabela resumo do artigo: o complemento é **ímpar** (formalizado em
`complemento_k4_impar`).

---

### A série — resultados acumulados (até v2.8.0)

**Fundação geométrica e combinatória (Papers 01–06)**

- Grade `G₃,N` e Fita‑Dobra `F(2×N)` com soma constante nas colunas (`2M⁻`) e diagonais (`2M⁺`) — **verificado em Lean**.
- Invariante Âncora, estimador oracle‑free e resolução do Problema B do Crivo Geométrico.

**Motor de Herança Estrutural (Paper 07)**

- Acoplamento `Φ` entre fita e grade (`3C = 2N`) — soma constante `6C` **verificada em Lean**.
- Teorema do Motor, condicional a `HR⁻` — **verificado em Lean**.

**Reformulação Espectral (Paper 08)**

- Sistema dinâmico `(X_N, μ_N, T)` com espectro discreto puro e entropia zero.
- Equivalência incondicional `HR⁻ ⟺ F̂(0) > 0` — **verificada em Lean**.

**Leis de escala (Papers 10 e 11)**

- Leis empíricas até `N = 10⁹` para `k*` e `p_max`, **restritas ao escopo `n ≡ 0 (mod 12)`** (ver Subsecção 3.5 do Paper 10).
- Conjectura da Âncora Absoluta, na forma revista **C′** (escopo `0 mod 12`).
- Decaimento exponencial do gap máximo, `β ≈ 0,20`.

**Cobertura condicional (Paper 12)**

- Prova condicional sob GRH de que a cobertura total implica `HR⁻` e, portanto, Goldbach.

---

### O que esta série não é

A série **não** contém uma prova da Conjectura de Goldbach, e a formalização
torna essa fronteira explícita: o único enunciado em aberto é
`HR⁻`/`ŵ(0) > 0`, que é equivalente a Goldbach. Os três resultados negativos
acima explicam por que a rota geométrica não pode, por si só, fechar a lacuna:
reflexões e translações preservam somas e não veem primalidade — a geometria
**prescreve** os pares, a aritmética tem de garantir que eles são primos.

---

### Como reproduzir

```powershell
# verificação formal (87 teoremas, zero sorry)
powershell -ExecutionPolicy Bypass -File lean/build.ps1

# auditoria de axiomas
cd lean; $env:LEAN_PATH = (Get-Location).Path
.toolchain/lean-4.36.0-windows/bin/lean Verificacao.lean

# lei da âncora
python scripts/lei_ancora_verificacao.py 10000000
```

---

**Zenodo.** Após o arquivamento automático desta release, o DOI de *versão* será
novo; o DOI de *conceito* (`10.5281/zenodo.20195997`) permanece estável e continua
a apontar para a versão mais recente.
