import Calculo_Frequencias as Freq


def pega_limites_inferiores():
    limites_inferiores = Freq.entrada_limiteinferior()
    return limites_inferiores


def pega_soma_fi():
    soma_fi = Freq.determina_freuqencia_absoluta()
    return soma_fi


def pega_fac():
    fac = Freq.cria_fac()
    return fac


# def cria_elemediano():
#     total_n = pega_fi_total()
#     elemento_mediano = total_n/2
#     return elemento_mediano
#
#
# def determina_lmd():
#     frequencia_acumulada = pega_fac()
#     elemento_m = cria_elemediano()
#     # A função "min", "lambda" e "abs" encontram os valores da frequencia acumulada mais próximo do
#     # elemento mediano. Determinando o limite inferior da CLASSE MEDIANA (C_md).
#     lmd = min(frequencia_acumulada, key=lambda x: abs(x - elemento_m))
#     float(lmd)
#     return lmd
#
#
# def determina_amplitude():
#     limites = pega_limites_inferiores()
#     limites_selecionados = limites[:2]
#     amplitude, *tail = limites_selecionados
#     for a in tail:
#         amplitude -= a
#     amplitude = amplitude * (-1)
#     return amplitude
#
#
# # A função "determina_posicao_fi" itera sobre os valores da freuqencia acumulada,
# # para retornar a CLASSE MEDIANA no qual o elemento mediano se encontra.
# def determina_posicao_fi():
#     freq_acm = pega_fac()
#     elem_mediano = cria_elemediano()
#     posicao = -1
#     for i in range(len(freq_acm)):
#         if elem_mediano <= freq_acm[i]:
#             posicao = i
#             break
#     return posicao
#
#
# # Após determinar a classe mediana onde o elemento mediano se encontra,
# # a função "determina_fi_escolhido" usa essa posição para definir a
# # frequência absoluta daquela classe.
# def determina_fi_escolhido():
#     posicao = determina_posicao_fi()
#     freq_inserido = pega_fi_inserido()
#     freq_fi_escolhida = freq_inserido[posicao]
#     return freq_fi_escolhida
#
#
# def determina_mediana_agrupada():
#     limite_lmd = determina_lmd()
#     elemento_mediano_emd = cria_elemediano()
#     freuqncia_fac_escolhida = pega_fac()
#     frequencia_fi_escolhido = determina_fi_escolhido()
#     amplitude_h = determina_amplitude()
#     mediana_md = (limite_lmd + ((elemento_mediano_emd - freuqncia_fac_escolhida) / frequencia_fi_escolhido) *
#                   amplitude_h)
#     float(mediana_md)
#     print(f'A mediana desses dados agrupados, corresponde a: {mediana_md}\n')
#     return mediana_md

def determina_mediana_agrupada():
# Pega todas as frequencias:
    limite_inserido = pega_limites_inferiores()
    total_fi = pega_soma_fi()
    freq_fi = Freq.frequencia_fi
    frequencia_fac = pega_fac()
    print("\n\n")

# Determina o elemento mediado (E_md):
    elemento_mediano_emd = total_fi / 2
    print(f'EMD:{elemento_mediano_emd}')

# A função "min", "lambda" e "abs" encontram o valor da frequência acumulada (FAC) mais próximo do
# elemento mediano.
    fac_escolhido = min(frequencia_fac, key=lambda x: abs(x - elemento_mediano_emd))
    print(f'FAC:{fac_escolhido}')

# Determina o Limite inferior da classe mediana (L_md):
    # Cria um dicionario, onde o frequências acumuladas (FAC) são a CHAVE e o limites inferiores
    # os VALORES da chave.
    dicionario_fac_limite = dict(zip(frequencia_fac, limite_inserido))
    # Interamos chave por chave no dicionário até encontrar as frequências acumuladas (FAC),
    # que seja maior (ou igual) ao elemento mediano.
    escolhe_limite = [k for k in dicionario_fac_limite.keys() if k >= elemento_mediano]
    # Seleciona a freuqencia acumulada (FAC) mais PRÓXIMA do elemento mediano.
    lmd = min(escolhe_limite)
    # Seleciona o Limite Inferior (L_md) da frequencia acumulada.
    limite_lmd = dicionario_fac_limite[lmd]
    print(f'Limite:{dicionario_fac_limite} --->Chave selecionada:{escolhe_limite} --->Limite escolhido:{limite_lmd}')

# Itera sobre os valores da freuqencia acumulada,
# para retornar a CLASSE MEDIANA no qual o elemento mediano se encontra.
    posicao = -1
    for i in range(len(frequencia_fac)):
        if elemento_mediano_emd <= frequencia_fac[i]:
            posicao = i
            break

    freq_fi_escolhida = freq_fi[posicao]
    print(f'FI:{freq_fi_escolhida} --->posicao do FI:{posicao}')

# Determina amplitude (h):
    limites_selecionados = limite_inserido[:2]
    amplitude, *tail = limites_selecionados
    for a in tail:
        amplitude -= a
    amplitude_h = amplitude * (-1)    # O "-1" muda o sinal do valor
    print(f'h:{amplitude_h}')

# Calcula a mediana agrupada (MD):
    md_agrupada = limite_lmd + ((elemento_mediano_emd - fac_escolhido) / freq_fi_escolhida) * amplitude_h
    print(f'\nA mediana desses dados agrupados, corresponde a: {md_agrupada}\n')
    return md_agrupada
