# Camada Lean 4 — núcleo verificável da série Goldbach

Formalização em **Lean 4** da espinha combinatória/algebraica da série
"Conjectura de Goldbach — Uma Abordagem Unificada" (T. Bandeira, 2026).

O objectivo **não** é formalizar os 12 papers (boa parte deles é analítica,
condicional ou empírica). O objectivo é:

1. fixar com precisão as **definições** que toda a série usa (grade `G_{k,N}`,
   fita-dobra, acoplamento `Φ`, janela `W_i`, `HR⁻`/`HR⁺`, função de colisão);
2. **demonstrar** os resultados que a série apresenta como incondicionais e que
   são de facto elementares;
3. deixar explícito, sem ambiguidade, **o que é hipótese** e **o que é
   evidência empírica** — ver [`TrustLedger.md`](TrustLedger.md).

## Estado

- 11 módulos, **0 `sorry`**, **0 axiomas próprios**.
- Os únicos axiomas usados são os do próprio Lean (`propext`, `Quot.sound`) e,
  num único teorema, `Classical.choice` (indicador de primalidade).
- Sem Mathlib: compila *offline*, em segundos.

## Como compilar

A toolchain (Lean 4.36.0) já está em `.toolchain/` (ignorada pelo git).

```powershell
pwsh -File lean/build.ps1
```

Ou, com [elan](https://github.com/leanprover/elan) instalado:

```powershell
cd lean
lake build
```

Para inspeccionar os axiomas de cada teorema:

```powershell
cd lean
$env:LEAN_PATH = (Get-Location).Path
.toolchain/lean-4.36.0-windows/bin/lean Verificacao.lean
```

## Estrutura

| Módulo | Conteúdo | Origem |
|---|---|---|
| `Goldbach/Basico.lean` | `Primo`, `Par`, `Impar`, `TemRepGoldbach` | — |
| `Goldbach/Grade.lean` | grade `G_{k,N}`, janelas, **Lema da Soma Constante**, âncora, complemento, PAs, uniformidade modular, generalização `k×N` | Paper 04 |
| `Goldbach/Fita.lean` | fita-dobra, soma constante das colunas, diagonais (par alvo), dois pares por fita | Paper 07 §2 |
| `Goldbach/Acoplamento.lean` | `Φ` sob `3C = 2N`, soma constante `6C = 4N`, injetividade/sobrejetividade das coordenadas | Paper 07 §3 |
| `Goldbach/Trio.lean` | trio totalmente primo ⇒ 3 representações binárias + 1 ternária; somas explícitas e distintas | Paper 04 §6 |
| `Goldbach/Motor.lean` | `HR⁻`, `HR⁺`, `HR⁺ ⇒ HR⁻`, cadeia e Teorema do Motor | Paper 07 §8 |
| `Goldbach/Espectral.lean` | função de colisão `F`, soma espectral, `HR⁻ ⟺ F̂(0) > 0`, `0 ≤ F̂(0) ≤ 1` | Paper 08 §4–6 |
| `Goldbach/Heranca.lean` | enumeração completa da fita, passo de herança `+2`, cadeia certificada, eixos de `W_i` e sua soma `2·âncora`, limite `mod 4`, dupla leitura de `W_i` | Paper 07/08, análise de R‑1 |
| `Goldbach/Cadeia.lean` | obstrução do 3: nenhuma coordenada avança duas vezes; cadeia de transporte tem comprimento ≤ 2 | Paper 07, análise de R-1 |
| `Goldbach/Projecao.lean` | alcance exacto das janelas (membro menor ≤ n/4), classe `6 (mod 12)` da janela auto-consistente, falha de `HR⁺` em 18 | Paper 04/07, análise |
| `Goldbach.lean` | raiz, importa todos | — |

## Teoremas principais

```lean
-- Paper 04, Lema 3.1
theorem lema_soma_constante (N i : Nat) (hi : 1 ≤ i) :
    diagPrincipal N i = somaJanela N i ∧
    diagSecundaria N i = somaJanela N i ∧
    colunaCentral N i = somaJanela N i

-- Paper 04, Corolário 3.2 + Prop. 3.4
theorem corolario_ancora (N i : Nat) : 3 * grade N 1 i = somaJanela N i
theorem complemento_par (N i n : Nat) (hn : Impar n) (hle : n ≤ somaJanela N i) :
    Par (complemento N i n)

-- Paper 04, §6
theorem trio_d1_goldbach (N i : Nat)
    (hpa : Primo (grade N 0 (i - 1))) (hpb : Primo (grade N 1 i))
    (hpc : Primo (grade N 2 (i + 1))) :
    TemRepGoldbach (...) ∧ TemRepGoldbach (...) ∧ TemRepGoldbach (...)

-- Paper 07, Prop. 2.1 / 2.3
theorem fita_soma (N k eps : Nat) ... : fitaA k + fitaB N k eps = 4 * N - 2 * eps
theorem fita_diagonal (N k : Nat) ... : fitaA (k + 1) + fitaB N k 1 = 4 * N

-- Paper 07, Prop. 3.5
theorem phi_soma_externa (C k : Nat) (hk : 1 ≤ k) (hkC : k ≤ C) :
    phiLinha1 C k + phiLinha3 C k = 6 * C

-- Paper 07, Teorema 8.4
theorem teorema_motor (base : Nat) (par : Nat → Nat × Nat) (h : Cadeia base par) :
    ∀ j, TemRepGoldbach (base + 2 * j)

-- Paper 08, Teorema 6.4
theorem hrcol_iff_Fhat0_pos (K : Nat) (ext : Nat → Nat × Nat) :
    HRcol K ext ↔ 0 < Fhat0 K ext

-- Herança genuína (v. TrustLedger §5)
theorem parDiagonal_sobrejetiva (N x : Nat) (hx : Impar x) (h3 : 3 ≤ x)
    (hxN : x ≤ 2 * N - 1) :
    ∃ k, 1 ≤ k ∧ k ≤ N - 1 ∧ (parDiagonal N k).1 = x

theorem cadeia_certificada (f : Nat → Nat × Nat)
    (hpasso : ∀ j, Passo (f j) (f (j + 1)))
    (hcert : ∀ j, Primo (f j).1 ∧ Primo (f j).2) :
    ∀ j, TemRepGoldbach ((f 0).1 + (f 0).2 + 2 * j)

theorem eixo_extremos_soma (N i : Nat) (hi : 1 ≤ i) :
    grade N 0 (i - 1) + grade N 2 (i + 1) = 2 * grade N 1 i ∧ ...

theorem alvo_mod_quatro (N i : Nat) : (2 * grade N 1 i) % 4 = 2
```

## Duas notas de implementação

**Indexação.** O núcleo usa indexação **0-based** (`grade N r c = 2*(r*N + c) + 1`);
os enunciados das janelas usam a indexação **1-based** do artigo, de modo que
cada teorema corresponde literalmente ao seu homólogo no paper. O `ℕ` não é
fornecido pela prelude desta toolchain, por isso usa-se `Nat` explicitamente.

**Porquê sem Mathlib.** Os resultados formalizados são aritmética elementar;
`omega` resolve-os todos. Evita-se assim um `.lake` de vários GB e mantém-se a
verificação reprodutível *offline*. A camada analítica (Papers 05, 06, 10–12)
exigiria Mathlib e não está aqui.

## O que este projecto deliberadamente não faz

Não formaliza — nem assume — a Conjectura de Goldbach, `HR⁻`, GRH, Hardy–
Littlewood ou as leis de escala empíricas. Essas afirmações aparecem no
[`TrustLedger.md`](TrustLedger.md) classificadas como **condicionais** ou
**empíricas**, com a indicação de onde vivem nos papers.
