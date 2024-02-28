import re
import collections


def contar_palavras(caminho_do_arquivo):
    with open(caminho_do_arquivo, 'r', encoding='utf-8') as file:
        todas_palavras = re.findall(r"(\w+)", file.read())
        todas_palavras = [palavra.upper() for palavra in todas_palavras]
        print(f'\nNúmero total de palavras: {len(todas_palavras)}')

        contagem_palavras = collections.Counter(todas_palavras)

        print('\n20 palavras mais comuns:')
        for palavra in contagem_palavras.most_common(20):
            print(f'{palavra[0]}\t{palavra[1]}')


# comandos usados na vídeo para referência
if __name__ == '__main__':
    contar_palavras('artigo.txt')