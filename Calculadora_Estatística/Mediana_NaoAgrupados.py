import numpy as np


def calcula_amostraMediana_impar():
    print(f'Insira os valores correspondentes a amostra dos dados para calcular a mediana dos mesmos,'
          f' separados por espaço:')
    amostra_dados = np.array(input().split(), dtype=int)
    count = len(amostra_dados)      # Tamanho da amostra (n)
    elem_mediano = int((count + 1) / 2)
    posicao_elemento = amostra_dados[elem_mediano - 1]  # O -1 faz a varíavel considerar o indice zero como 1
    mediana_impar = posicao_elemento
    print(f'A mediana da amostra de dados fornecida, constitui pelo número:', mediana_impar)
    return mediana_impar


def calcula_amostraMediana_par():
    print(f'Insira os valores correspondentes a amostra dos dados para calcular a mediana dos mesmos,'
          f' separados por espaço:')
    dados_amostrais = np.array(input().split(), dtype=int)
    count = len(dados_amostrais)   # Tamanho da amostra (n)
    elemento_md1 = int(count / 2)       # Calculo da primeira mediana
    elemento_md2 = int((count / 2) + 1)     # Calculo da segunda mediana
    posicao_md1 = dados_amostrais[elemento_md1 - 1]     # Elemento Mediano 1
    posicao_md2 = dados_amostrais[elemento_md2 - 1]     # Elemento Mediano 2
    soma_medianas = (posicao_md1 + posicao_md2) / 2
    mediana_par = soma_medianas
    print(f'A mediana da amostra de dados fornecida, constitui pelo número:', mediana_par)
    return mediana_par


