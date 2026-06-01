import re
import csv

def extrair_gaps_do_log(arquivo_log):
    with open(arquivo_log, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    dados = []
    n_atual = None

    for linha in linhas:
        # Linha exata: "N = 1,000,000" (começa com N, espaço, igual, espaço)
        if re.match(r'^N\s*=\s*[\d,]+', linha):
            # extrai o número após a igualdade
            num_str = re.search(r'[\d,]+', linha).group(0).replace(',', '')
            n_atual = int(num_str)
            continue

        if n_atual is None:
            continue

        # Linhas que contêm "k=" e "gap_max="
        if 'k=' in linha and 'gap_max=' in linha:
            # Exemplo: "  k=   1  p=      5  gap_max=   10  cobertura=0.206514"
            k_match = re.search(r'k=\s*(\d+)', linha)
            p_match = re.search(r'p=\s*(\d+)', linha)
            gap_match = re.search(r'gap_max=\s*(\d+)', linha)
            if k_match and p_match and gap_match:
                k = int(k_match.group(1))
                p = int(p_match.group(1))
                gap = int(gap_match.group(1))
                dados.append((n_atual, k, p, gap))

    # Remove duplicatas (mesmo N e mesma ordem)
    vistos = set()
    unicos = []
    for n, k, p, g in dados:
        chave = (n, k)
        if chave not in vistos:
            vistos.add(chave)
            unicos.append((n, k, p, g))
    return unicos

# Extrai
dados = extrair_gaps_do_log('log_ancora_v2.txt')

# Salva CSV
with open('experimento5_gaps_consolidado_v2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['N', 'ordem', 'ancora', 'gap_max'])
    writer.writerows(dados)

print(f"Extraídos {len(dados)} registros únicos.")
for i in range(min(5, len(dados))):
    print(dados[i])