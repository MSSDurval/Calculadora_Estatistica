import numpy as np


def calcula_amostraMediana_impar():
    print(f'Insira os valores correspondentes a amostra dos dados para calcular a mediana dos mesmos,'
          f' separados por espaço:')
    amostra_dados = np.array(input().split(), dtype=int)
    organiza_amostra = sorted(amostra_dados)    # Amostra em ordem crerscente
    count = len(organiza_amostra)      # Tamanho da amostra (n)
    elem_mediano = int((count + 1) / 2)
    posicao_elemento = amostra_dados[elem_mediano - 1]   # O -1 faz a varíavel considerar o indice zero do array como 1
    mediana_impar = int(posicao_elemento)
    amostra_ordenada = ', '.join(map(str, organiza_amostra))    # Retira os colchetes do array "organiza_dados"
    print(f'A mediana da amostra {amostra_ordenada}, é o número: {mediana_impar}.')
    return mediana_impar


def calcula_amostraMediana_par():
    print(f'Insira os valores correspondentes a amostra dos dados para calcular a mediana dos mesmos,'
          f' separados por espaço:')
    dados_amostrais = np.array(input().split(), dtype=int)
    organiza_dados = sorted(dados_amostrais)    # Amostra em ordem crescente
    count = len(organiza_dados)   # Tamanho da amostra (n)
    calculo_md1 = int(count / 2)       # Calculo da primeira mediana
    calculo_md2 = int((count / 2) + 1)     # Calculo da segunda mediana
    # O "-1" faz a varíavel considerar o indice zero do array como 1:
    elemento_md1 = organiza_dados[calculo_md1 - 1]     # Elemento Mediano 1
    elemento_md2 = organiza_dados[calculo_md2 - 1]     # Elemento Mediano 2
    soma_elementos = (elemento_md1 + elemento_md2) / 2
    mediana_par = int(soma_elementos)
    amostra_ordenada = ', '.join(map(str, organiza_dados))   # Retira os colchetes do array "organiza_dados"
    print(f'A mediana da amostra {amostra_ordenada}, resulta no número: {mediana_par}.')
    return mediana_par


