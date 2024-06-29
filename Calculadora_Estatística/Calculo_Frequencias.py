import numpy as np
frequencia_fi = None


# A função "entrada_limiteinferior" pede os limites inferiores de uma distribuicao de frequencia
def entrada_limiteinferior():
    print(f'Insira os valores dos limites inferiores de cada classe, separados por espaço: ')
    limit_inf = np.array(input().split(), dtype=float)
    return limit_inf


# Pede a frequencia absoluta (FI) ao usuário, mostra o que foi inserido
# e determina o total da distribuição de frequência.
def determina_freuqencia_absoluta():
    global frequencia_fi
    # Pede os valores de da frequência absoluta:
    print(f'Agora insira os valores que compoem a frequência absoluta (Fi), separados por espaço: ')
    frequencia_fi = np.array(input().split(), dtype=int)    # Frequencia absoluta, que é usada para outros calculos.
    # Retira os colchetes do array:
    mostra_frequencia_fi = ', '.join(map(str, frequencia_fi))
    print(f'\nO valores inseridos para a frequência absoluta foram os valores: {mostra_frequencia_fi}')
    # Determina o total da distribuicao, somando a frequencia Fi:
    frequencia_absoluta = sum(frequencia_fi)
    print(f'A frequência absoluta (Fi) ou total dessa distribuição de frequência é: {frequencia_absoluta}.')
    return frequencia_absoluta


# A função "cria_fac" calcula a frequêcia acumulada de cada clsse e retorna o resultado.
def cria_fac():
    freq_fi = frequencia_fi
    soma_entre_elementos = 0
    freq_fac = []
    # Itera sobre cada elemento da frequencia absoluta (fi). Para poder somar cada valor, um por um.
    for num in freq_fi:
        soma_entre_elementos += num
        freq_fac.append(soma_entre_elementos)
    # Retorna as frequencias acumuladas de CADA classe
    print(f'As frequências acumuladas (FAC) de cada classe desta distribuição de frequência é: {freq_fac}')
    return freq_fac


