def determina_mediana_agrupada():

    total_n = pega_fi_total()
    elemento_mediano = total_n / 2
    frequencia_acumulada = pega_fac()


    # A função "min", "lambda" e "abs" encontram os valores da frequencia acumulada mais próximo do
    # elemento mediano. Determinando o limite inferior da CLASSE MEDIANA (C_md).
    lmd = min(frequencia_acumulada, key=lambda x: abs(x - elemento_mediano))
    float(lmd)


    posicao = -1
    for i in range(len(frequencia_acumulada)):
        if elemento_mediano <= frequencia_acumulada[i]:
            posicao = i
            break
    freq_inserido = pega_fi_inserido()
    freq_fi_escolhida = freq_inserido[posicao]

    limites = pega_limites_inferiores()
    limites_selecionados = limites[:2]
    amplitude, *tail = limites_selecionados
    for a in tail:
        amplitude -= a
    amplitude = amplitude * (-1)


    MDagrupada = (lmd + ((elemento_mediano - frequencia_acumulada) / posicao) *
                  amplitude)
    float(MDagrupada)
    print(f'A mediana desses dados agrupados, corresponde a: {MDagrupada}\n')
    return MDagrupada