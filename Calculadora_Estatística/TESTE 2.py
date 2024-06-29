def determina_lmd():
    fac = [3, 7, 6, 10, 3, 1]
    elemento_m = 15
    # A função "min", "lambda" e "abs" encontram os valores da frequencia acumulada mais próximo do
    # elemento mediano. Determinando o limite inferior da CLASSE MEDIANA (C_md).
    lmd = min(fac, key=lambda x: abs(x - elemento_m))
    float(lmd)
    return lmd

determina_lmd()
print(determina_lmd())