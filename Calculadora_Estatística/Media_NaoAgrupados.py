def calcula_amostraMedia():
    import numpy as np
    # A função calcula_amostraMedia, pede a amostra dos dados ao usuário e retorna a média dessa amostra.
    print(f'Insira os valores correspondentes a amostra dos dados, separados por espaço:')
    rol_dados = np.array(input().split(), dtype=int)
    count = len(rol_dados)
    r_media = sum(rol_dados)/count
    print(f'A média da amostra inserida é:', r_media, '\n')
    return r_media
