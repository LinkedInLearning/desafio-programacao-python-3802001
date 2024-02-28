import time
import random

def jogo_de_espera():
    objetivo = random.randint(2, 4)  # tempo de espera em segundos
    print(f'\nSeu objetivo é de {objetivo} segundos')

    input(' ---Pressione Enter para começar--- ')
    inicio = time.perf_counter()

    input(f'\n...Pressione Enter de novo depois de {objetivo} segundos...')
    decorrido = time.perf_counter() - inicio

    print(f'\nTempo decorrido: {decorrido :.3f} segundos')
    if decorrido == objetivo:
        print('(Impressionante! Tempo perfeito!)')
    elif decorrido < objetivo:
        print(f'Eita! Rápido demais! Faltava ({objetivo - decorrido :.3f} segundos)')
    else:
        print(f'Iiii... Devagar demais... Sobrou ({decorrido - objetivo :.3f} segundos)')


# comandos usados na vídeo para referência
if __name__ == '__main__':
    jogo_de_espera()