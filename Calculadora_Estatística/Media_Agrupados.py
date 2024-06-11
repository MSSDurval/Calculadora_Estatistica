import Calculo_Frequencia_Acumulada as distribuicao_frequencia


# As funçoes, pega_classe, pega_frequenciaFi e pega_frequenciaFAC recebem a classe (Xi),
# a frequencia absoluta e a frequencia acumulada da distribuição de frequência inserida pelo usuário

# Classe (Xi)
def pega_classe():
    classe = distribuicao_frequencia.entrada_classe()
    return classe


# Fi
def pega_freuqnciaFi():
    frequencia_fi = distribuicao_frequencia.entrada_freuqenciaFI()
    return frequencia_fi


# FAC
def pega_frequenciaFAC():
    frequencia_fac = distribuicao_frequencia.calcula_frequenciaFAC()
    return frequencia_fac


# Após função cria_media calcula a média desses dados, multilicando o a frequencia absoluta com o limite inferior de
# cada classe.
def cria_media():
    import numpy as np
    classe = pega_classe()
    frequencia_fi = pega_freuqnciaFi()
    frequencia_fac = pega_frequenciaFAC()
    multiplicacao_XiFi = np.multiply(classe, frequencia_fi)
    total_parcial = sum(multiplicacao_XiFi)
    media_agrupada = total_parcial/frequencia_fac
    return print(f'A média dessa relação de dados é de: {media_agrupada}.')
