from random import randint
from collections import Counter

def simular_dados(*dados, tentativas=1_000_000):
    contagens = Counter()
    for _ in range(tentativas):
        contagens[sum((randint(1, lados) for lados in dados))] += 1

    print('\nPROBABILIDADE DE RESULTADOS')
    for resultado in range(len(dados), sum(dados) + 1):
        print(f'{resultado}\t{contagens[resultado] * 100 / tentativas :0.2f}%')


# comandos usados na vídeo para referência
if __name__ == '__main__':
    simular_dados(4, 6, 6)
    # simular_dados(4, 6, 6, 20)