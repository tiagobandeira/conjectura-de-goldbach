/-
  Goldbach.lean — raiz do projecto.

  Formalização em Lean 4 do núcleo verificável da série "Conjectura de
  Goldbach — Uma Abordagem Unificada" (T. Bandeira, 2026).

  Todo o projecto usa apenas o núcleo do Lean 4 (sem Mathlib), de modo que
  `lake build` funciona offline e a verificação é rápida.
-/
import Goldbach.Basico
import Goldbach.Grade
import Goldbach.Fita
import Goldbach.Acoplamento
import Goldbach.Trio
import Goldbach.Motor
import Goldbach.Espectral
import Goldbach.Heranca
import Goldbach.Cadeia
import Goldbach.Projecao
