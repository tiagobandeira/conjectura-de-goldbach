"""Baixa e extrai a toolchain Lean 4 (Windows) para lean/.toolchain/.

Uso:
    python lean/download_toolchain.py

Necessário apenas se você não tiver elan instalado. Requer ~900 MB de download
e ~2,3 GB em disco. A versão está fixada em lean/lean-toolchain.
"""
import os
import ssl
import sys
import urllib.request
import zipfile

VERSAO = "4.36.0"
URL = (f"https://github.com/leanprover/lean4/releases/download/v{VERSAO}/"
       f"lean-{VERSAO}-windows.zip")

AQUI = os.path.dirname(os.path.abspath(__file__))
ZIP = os.path.join(AQUI, os.path.basename(URL))
OUT = os.path.join(AQUI, ".toolchain")


def main() -> int:
    os.makedirs(OUT, exist_ok=True)
    if not os.path.exists(ZIP):
        ctx = ssl.create_default_context()
        req = urllib.request.Request(URL, headers={"User-Agent": "curl/8"})
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            total = int(resp.headers.get("Content-Length") or 0)
            print(f"baixando {total / 1e6:.0f} MB", flush=True)
            feito = 0
            with open(ZIP, "wb") as fh:
                while True:
                    bloco = resp.read(1 << 20)
                    if not bloco:
                        break
                    fh.write(bloco)
                    feito += len(bloco)
    print("extraindo", flush=True)
    with zipfile.ZipFile(ZIP) as zf:
        zf.extractall(OUT)
    print("ok:", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
