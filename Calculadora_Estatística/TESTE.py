def determina_posicao_fi():
    freq_acm = [2, 6, 13, 18, 23, 30]
    elem_mediano = 15

    posicao = -1
    for i in range(len(freq_acm)):
        if elem_mediano <= freq_acm[i]:
            posicao = i
            break
    return posicao


def determina_fi_escolhido():
    posicao = determina_posicao_fi()
    freq_inserido = [2, 4, 7, 5, 5, 7]
    freq_fi_escolhida = freq_inserido[posicao]
    return freq_fi_escolhida

determina_fi_escolhido()
print(determina_fi_escolhido())