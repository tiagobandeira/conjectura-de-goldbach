# Verificação da posição canônica de Wi*
# Sem algoritmo de ordenação — só fórmula fechada
# Sem libs externas — roda no celular

def eh_primo(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True

def verificar_C(C):
    # Condição 3C = 2N
    if C % 2 != 0:
        return None  # C deve ser par
    N     = 3 * C // 2
    istar = C // 2 - 1   # 0-based
    M_mais = 6 * C       # 2M+

    # Fórmula fechada — sem ordenação
    e1 = C - 1           # L1[i*] no estado canônico
    e3 = 5 * C + 1       # L3[i*] no estado canônico (decrescente)
    soma = e1 + e3       # deve ser sempre 6C

    p1 = eh_primo(e1)
    p3 = eh_primo(e3)
    hr = p1 and p3

    return {
        'C': C, 'N': N, 'istar': istar + 1,  # 1-based para leitura
        'e1': e1, 'e3': e3, 'soma': soma,
        'e1_primo': p1, 'e3_primo': p3,
        'hr_menos': hr
    }

def rodar(C_max=100):
    print("Verificação canônica de Wi* — fórmula fechada")
    print("e1 = C-1  |  e3 = 5C+1  |  soma = 6C = 2M+")
    print()
    print(f"{'C':>4}  {'i*':>4}  {'e1':>6}  {'e3':>6}  {'soma':>6}  e1∈P  e3∈P  HR-")
    print("-" * 52)

    sucessos = []
    for C in range(4, C_max + 1, 2):
        r = verificar_C(C)
        p1 = "✓" if r['e1_primo'] else "✗"
        p3 = "✓" if r['e3_primo'] else "✗"
        hr = "✓" if r['hr_menos'] else "✗"
        print(f"  {r['C']:>3}  {r['istar']:>4}  {r['e1']:>6}  "
              f"{r['e3']:>6}  {r['soma']:>6}  {p1}     {p3}    {hr}")
        if r['hr_menos']:
            sucessos.append(C)

    print()
    print(f"HR- disparou em {len(sucessos)} casos:")
    print(f"  C = {sucessos}")
    print()
    print("Verificação da soma 6C = 2M+ (deve ser sempre True):")
    falhas_soma = [C for C in range(4, C_max+1, 2)
                   if verificar_C(C)['soma'] != 6*C]
    print(f"  Falhas: {falhas_soma if falhas_soma else 'nenhuma ✓'}")

rodar(C_max=500)
