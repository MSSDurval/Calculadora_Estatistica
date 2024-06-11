import numpy as np


# A função "entrada_classe" pede os limites inferiores de uma distribuicao de frequencia
def entrada_classe():

    print(f'Insira os valores dos limites inferiores de cada classe, separados por espaço: ')
    classe = np.array(input().split(), dtype=int)
    return classe


# a função "entrada_frequenciaFI" pede os valores totais de cada classe da distribuição de frequência
def entrada_freuqenciaFI():

    global frequencia_fi
    print(f'Agora insira os valores que compoem a frequência absoluta (Fi), separados por espaço: ')
    frequencia_fi = np.array(input().split(), dtype=int)
    return frequencia_fi


# a função "calcula_frequenciaFAC" calcula a frequêcia acumulada e retorna o resultado.
def calcula_frequenciaFAC():

    frequencia_fac = sum(frequencia_fi)
    print(f'\nA frequência acumulada (FAC) total dessa distribuição de frequência é: {frequencia_fac}.')
    return frequencia_fac

