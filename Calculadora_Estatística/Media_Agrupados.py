import Calculo_Frequencias as Frequencia


# As funçoes, pega_classe, pega_frequenciaFi e pega_frequenciaFAC recebem a classe (Xi),
# a frequencia absoluta e a frequencia acumulada da distribuição de frequência inserida pelo usuário

# Classe (Xi)
def pega_limite():
    limite_classe = Frequencia.entrada_limiteinferior()
    return limite_classe


# Total do FI
def pega_totalFi():
    fi_total = Frequencia.determina_freuqencia_absoluta()
    return fi_total


# FAC
def pega_frequenciaFAC():
    frequencia_fac = Frequencia.cria_fac()
    return frequencia_fac


# Após a função cria_media calcula a média desses dados, multilicando o a frequencia absoluta com o limite inferior de
# cada classe.
def cria_media():
    import numpy as np
    limite_infeior = pega_limite()
    total_fi = pega_totalFi()
    multiplicacao_XiFi = np.multiply(limite_infeior, Frequencia.frequencia_fi)
    soma_parcial = sum(multiplicacao_XiFi)
    media_agrupada = soma_parcial/total_fi
    print(f'A média dessa relação de dados é de: {media_agrupada}.')
    return media_agrupada
