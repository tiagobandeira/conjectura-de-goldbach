# Compila o projecto Lean 4 sem depender de elan/lake.
#
# Uso (PowerShell 7):      pwsh -File lean/build.ps1
# Uso (Windows PowerShell): powershell -ExecutionPolicy Bypass -File lean\build.ps1
#
# A toolchain foi extraida em lean/.toolchain/lean-4.36.0-windows/.
# Se voce tiver elan instalado, `lake build` dentro de lean/ tambem funciona.

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$toolchain = Join-Path $root '.toolchain\lean-4.36.0-windows'
$lean = Join-Path $toolchain 'bin\lean.exe'

if (-not (Test-Path $lean)) {
    Write-Error "Toolchain Lean nao encontrada em $toolchain. Rode: python lean/download_toolchain.py"
}

$env:PATH = "$(Join-Path $toolchain 'bin');$env:PATH"
$env:LEAN_PATH = $root

$files = @(
    'Goldbach\Basico.lean',
    'Goldbach\Grade.lean',
    'Goldbach\Fita.lean',
    'Goldbach\Acoplamento.lean',
    'Goldbach\Trio.lean',
    'Goldbach\Motor.lean',
    'Goldbach\Espectral.lean',
    'Goldbach\Heranca.lean',
    'Goldbach\Cadeia.lean',
    'Goldbach\Projecao.lean',
    'Goldbach.lean'
)

$erros = 0
$falhas = @()
$sw = [Diagnostics.Stopwatch]::StartNew()
foreach ($f in $files) {
    $caminho = Join-Path $root $f
    $olean = $caminho -replace '\.lean$', '.olean'
    Write-Host "==> $f" -ForegroundColor Cyan
    & $lean -o $olean $caminho
    if ($LASTEXITCODE -ne 0) {
        $erros++
        $falhas += $f
        Write-Host "    FALHOU (codigo $LASTEXITCODE)" -ForegroundColor Red
    }
}

$segundos = [math]::Round($sw.Elapsed.TotalSeconds, 1)
Write-Host ''
if ($erros -eq 0) {
    Write-Host "Build OK: $($files.Count) modulos, 0 erros, $segundos s." -ForegroundColor Green
} else {
    Write-Host "Build com $erros modulo(s) em erro: $($falhas -join ', ')" -ForegroundColor Red
    exit 1
}
