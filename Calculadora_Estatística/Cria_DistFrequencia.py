import numpy as np
# A pega_classe pede os valores de uma distribuicao de frequencia e retorna a frequencia acumulada
def entrada_classe():

    print(f'Insira os valores dos limites inferiores de cada classe, separados por espaço: ')
    classe = np.array(input().split(), dtype=int)
    return classe

#
def entrada_freuqenciaFI():

    global frequencia_fi
    print(f'Agora insira os valores que compoem a frequência absoluta (Fi), separados por espaço: ')
    frequencia_fi = np.array(input().split(), dtype=int)
    return frequencia_fi


def calcula_frequenciaFAC():

    frequencia_fac = sum(frequencia_fi)
    print(f'\nA frequência acumulada (FAC) total dessa distribuição de frequência é:', frequencia_fac)
    return frequencia_fac

