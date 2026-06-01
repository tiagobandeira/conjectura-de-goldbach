# -*- coding: utf-8 -*-
"""
Experimento 4 – Validação do modelo de Poisson
Usa os CSVs do Experimento 2 para comparar cobertura observada vs. predita.
Gera gráficos e tabelas.
"""

import csv
import math
import numpy as np
import glob

def carga_dados(N):
    """Carrega a sequência de âncoras e cobertos_count do CSV."""
    arquivo = f"experimento2_resultados/sequencia_ancoras_{N}.csv"
    ancoras = []
    cobertos = []
    with open(arquivo, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ancoras.append(int(row['ancora_p']))
            cobertos.append(int(row['cobertos_count']))
    return ancoras, cobertos

def predicao_poisson(C, k, rho_medio):
    """Probabilidade de C NÃO ser coberto após k âncoras."""
    # rho_medio = 19 / log²(C)  – mas podemos usar uma média sobre C
    return math.exp(-k * rho_medio)

def main():
    # Arquivos disponíveis
    arquivos = glob.glob("./experimento2_resultados/sequencia_ancoras_*.csv")
    Ns = [int(f.split('_')[-1].replace('.csv', '')) for f in arquivos]
    Ns.sort()

    resultados = []
    for N in Ns:
        ancoras, cobertos = carga_dados(N)
        total_C = (N // 2) - 1  # C pares de 4 a N
        k_lista = list(range(1, len(ancoras)+1))

        # Para cada C, o valor médio de rho (simplificação)
        # Vamos calcular a cobertura esperada integrando sobre C
        # Mas para simplificar, usamos um C médio: N/2
        C_medio = N / 2
        rho_medio = 19.0 / (math.log(C_medio)**2)

        # Cobertura observada em fração
        frac_obs = [c / total_C for c in cobertos]

        # Cobertura predita: 1 - exp(-k * rho_medio)
        frac_pred = [1 - math.exp(-k * rho_medio) for k in k_lista]

        # Erro médio
        erros = [abs(obs - pred) for obs, pred in zip(frac_obs, frac_pred)]
        erro_medio = np.mean(erros)
        resultados.append((N, erro_medio, frac_obs[-1], frac_pred[-1]))

        print(f"N={N:10,}: erro médio = {erro_medio:.5f}  |  cobertura final obs={frac_obs[-1]:.6f} pred={frac_pred[-1]:.6f}")

    # Salva resumo
    with open('experimento4_validacao_poisson.csv', 'w') as f:
        f.write("N,erro_medio,cobertura_obs_final,cobertura_pred_final\n")
        for N, err, obs, pred in resultados:
            f.write(f"{N},{err:.6f},{obs:.6f},{pred:.6f}\n")

    print("\nArquivo 'experimento4_validacao_poisson.csv' gerado.")

if __name__ == "__main__":
    main()