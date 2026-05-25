# Lucas Geométrico para Wi* — par canônico (e1, e3) = (C−1, 5C+1)
# Artigo 7 da série: Crivo Canônico e Certificado Geométrico
# Sem libs externas — roda no celular

# ─────────────────────────────────────────────
# Ferramentas aritméticas básicas
# ─────────────────────────────────────────────

def fatores_primos(n):
    """Retorna o conjunto dos fatores primos distintos de n."""
    f = set()
    if n < 2:
        return f
    d = 2
    while d * d <= n:
        if n % d == 0:
            f.add(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        f.add(n)
    return f

def pow_mod(base, exp, mod):
    """Exponenciação modular rápida."""
    resultado = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            resultado = resultado * base % mod
        base = base * base % mod
        exp //= 2
    return resultado

def eh_primo_miller(n, testemunhas=None):
    """Miller-Rabin determinístico para n < 3.2×10^18."""
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False
    # Conjunto determinístico cobrindo n < 3,215,031,751
    if testemunhas is None:
        testemunhas = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in testemunhas:
        if a >= n:
            continue
        x = pow_mod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

# ─────────────────────────────────────────────
# Teste de Lucas (primalidade por N−1)
# ─────────────────────────────────────────────

def lucas_primo(n):
    """
    Teste de Lucas completo para n.
    Condição: existe a tal que:
      (1) a^(n−1) ≡ 1  (mod n)
      (2) a^((n−1)/q) ≢ 1  (mod n)  para todo fator primo q de n−1

    Retorna: dict com resultado, testemunha a, fatores de n−1, passos
    Se n−1 não é completamente fatorável (n muito grande sem fator pequeno),
    reporta falha de fatoração.
    """
    if n < 2:
        return {'primo': False, 'motivo': 'n < 2', 'n': n}
    if n == 2:
        return {'primo': True, 'motivo': 'n = 2', 'n': n, 'testemunha': None}
    if n % 2 == 0:
        return {'primo': False, 'motivo': 'par', 'n': n}

    nm1 = n - 1
    qs = fatores_primos(nm1)

    # Tentamos testemunhas a = 2, 3, 5, ... até 200
    for a in range(2, min(n, 201)):
        # Condição (1)
        if pow_mod(a, nm1, n) != 1:
            continue
        # Condição (2): a^((n-1)/q) ≢ 1 para todos os q
        ok = True
        falha_q = None
        for q in qs:
            if pow_mod(a, nm1 // q, n) == 1:
                ok = False
                falha_q = q
                break
        if ok:
            return {
                'primo': True,
                'n': n,
                'testemunha': a,
                'fatores_nm1': sorted(qs),
                'nm1': nm1,
                'motivo': 'Lucas OK'
            }

    # Se nenhuma testemunha funcionou, usamos Miller-Rabin como fallback
    mr = eh_primo_miller(n)
    return {
        'primo': mr,
        'n': n,
        'testemunha': None,
        'fatores_nm1': sorted(qs),
        'nm1': nm1,
        'motivo': 'sem testemunha Lucas — Miller-Rabin usado'
    }

# ─────────────────────────────────────────────
# Par canônico Wi* e certificado geométrico
# ─────────────────────────────────────────────

def par_canonico(C):
    """
    Fórmula fechada do Artigo 7, Proposição 2.3:
      e1 = C − 1      (L1[i*], crescente)
      e3 = 5C + 1     (L3[i*], decrescente)
      soma = 6C = 2M+
      i* = C/2 − 1    (0-based)
    """
    assert C >= 4 and C % 2 == 0, "C deve ser par ≥ 4"
    istar = C // 2 - 1
    e1 = C - 1
    e3 = 5 * C + 1
    return istar, e1, e3

def certificado_lucas_geometrico(C):
    """
    Aplica o Teste de Lucas a e1 = C−1 e e3 = 5C+1.
    Retorna o certificado completo do Artigo 7, Seção 10.
    """
    istar, e1, e3 = par_canonico(C)
    soma = e1 + e3  # deve ser 6C

    r1 = lucas_primo(e1)
    r3 = lucas_primo(e3)

    hr_menos = r1['primo'] and r3['primo']

    return {
        'C': C,
        'istar_0based': istar,
        'istar_1based': istar + 1,
        'e1': e1,
        'e3': e3,
        'soma_6C': soma,
        'soma_ok': soma == 6 * C,
        'e1_lucas': r1,
        'e3_lucas': r3,
        'HR_menos': hr_menos,
        '2M_mais': 6 * C,
        'goldbach_alvo': f"{e1} + {e3} = {soma}",
    }

# ─────────────────────────────────────────────
# Relatório formatado
# ─────────────────────────────────────────────

def formatar_lucas(r, label):
    status = "✓ PRIMO" if r['primo'] else "✗ composto"
    t = r.get('testemunha')
    fat = r.get('fatores_nm1', [])
    motivo = r.get('motivo', '')
    linhas = [
        f"  {label} = {r['n']}  →  {status}",
        f"    motivo   : {motivo}",
    ]
    if t:
        linhas.append(f"    testemunha a = {t}")
        linhas.append(f"    n−1 = {r.get('nm1')}  =  fatores primos: {fat}")
    return "\n".join(linhas)

def rodar(C_max=300, so_hr=False):
    print("=" * 65)
    print(" LUCAS GEOMÉTRICO Wi* — Certificado Canônico de Goldbach")
    print(" Par: (e1, e3) = (C−1, 5C+1)   |   soma = 6C = 2M+")
    print("=" * 65)
    print()

    hr_casos = []

    for C in range(4, C_max + 1, 2):
        cert = certificado_lucas_geometrico(C)

        if so_hr and not cert['HR_menos']:
            continue  # mostra só os que disparam HR-

        marca = "★ HR-" if cert['HR_menos'] else "     "
        print(f"{marca}  C={C:>4}  i*={cert['istar_1based']:>3}  "
              f"e1={cert['e1']:>6}  e3={cert['e3']:>6}  "
              f"2M+={cert['2M_mais']:>6}  "
              f"e1∈P={'✓' if cert['e1_lucas']['primo'] else '✗'}  "
              f"e3∈P={'✓' if cert['e3_lucas']['primo'] else '✗'}")

        if cert['HR_menos']:
            hr_casos.append(C)

    print()
    print("=" * 65)
    print(f" HR- disparou em {len(hr_casos)} casos até C={C_max}:")
    print(f"  C = {hr_casos}")
    print()
    print(" Goldbach certificado geometricamente:")
    for C in hr_casos[:10]:  # mostra os 10 primeiros detalhados
        cert = certificado_lucas_geometrico(C)
        print(f"  6C = {6*C:>5}  →  {cert['goldbach_alvo']}")
    if len(hr_casos) > 10:
        print(f"  ... e mais {len(hr_casos)-10} casos.")

def detalhar(C):
    """Exibe o certificado completo de Lucas Geométrico para um C."""
    cert = certificado_lucas_geometrico(C)
    print()
    print("=" * 55)
    print(f" CERTIFICADO GEOMÉTRICO DE LUCAS — C = {C}")
    print("=" * 55)
    print(f"  Acoplamento Φ :  3C = {3*C}  =  2N = {2*(3*C//2)}")
    print(f"  i* (1-based)  :  {cert['istar_1based']}")
    print(f"  e1 = C−1      :  {cert['e1']}")
    print(f"  e3 = 5C+1     :  {cert['e3']}")
    print(f"  soma = 6C     :  {cert['soma_6C']}  {'✓' if cert['soma_ok'] else '✗'}")
    print(f"  Alvo Goldbach :  2M+ = {cert['2M_mais']}")
    print()
    print(" — Teste de Lucas em e1 —")
    print(formatar_lucas(cert['e1_lucas'], 'e1'))
    print()
    print(" — Teste de Lucas em e3 —")
    print(formatar_lucas(cert['e3_lucas'], 'e3'))
    print()
    hr = cert['HR_menos']
    if hr:
        print(f" HR- : ✓ DISPARA  →  {cert['goldbach_alvo']}  é par de Goldbach certificado")
    else:
        print(" HR- : ✗ não dispara")
    print()

# ─────────────────────────────────────────────
# Execução
# ─────────────────────────────────────────────

print()
print("─── Tabela completa C = 4..100 ───")
rodar(C_max=100)

print()
print("─── Tabela estendida C = 4..500 (só HR-) ───")
rodar(C_max=500, so_hr=True)

print()
print("─── Certificados detalhados para os primeiros casos HR- ───")
primeiros_hr = [C for C in range(4, 101, 2)
                if certificado_lucas_geometrico(C)['HR_menos']]
for C in primeiros_hr[:5]:
    detalhar(C)
