def calcula_amostraMedia():
    import numpy as np
    # A função calcula_amostraMedia, pede a amostra dos dados ao usuário e retorna a média dessa amostra.
    print(f'Insira os valores correspondentes a amostra dos dados, separados por espaço:')
    rol_dados = np.array(input().split(), dtype=float)
    rol_ordenado = sorted(rol_dados)
    count = len(rol_ordenado)  # Conta o tamanho da amostra (n)
    r_media = sum(rol_ordenado)/count
    int(r_media)
    print(f'A média da amostra inserida é: {r_media}.')
    return r_media
