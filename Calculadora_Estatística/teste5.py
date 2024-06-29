def cria_fucao1():
    variavel1 = 10
    variavel2 = 20
    return variavel1, variavel2


def chama_funcao1():
    variavel_a, _ = cria_fucao1()
    print(variavel_a)


chama_funcao1()