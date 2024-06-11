import Calculo_Frequencia_Acumulada as Dist_frequencia


def pega_xi():
    xi = Dist_frequencia.entrada_classe()
    return xi


def pega_fi():
    fi = Dist_frequencia.entrada_freuqenciaFI()
    return fi


def pega_fac():
    fac = Dist_frequencia.calcula_frequenciaFAC()
    return fac


def cria_mediana():
    import numpy as np
    classe_xi = pega_xi()
    frequencia_absoluta = pega_fi()
    freq_fac = pega_fac()
    elemento_mediano =