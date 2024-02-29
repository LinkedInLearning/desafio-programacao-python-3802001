import os
import re
from urllib.parse import urlsplit, urlunsplit
from urllib.request import urlretrieve


def baixar_arquivos(primeira_url, output_dir):
    # cria o diretório se não existir
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    protocolo, dominio, caminho, filtro, fragmento = urlsplit(primeira_url)

    atual = re.findall(r'[0-9]+', caminho)[-1]

    contador, erros = 0, 0
    while erros < 3:
        proximo = str(int(atual) + contador)
        if atual[0] == '0':  # adiciona os zeros à esquerda
            proximo = '0' * (len(atual) - len(proximo)) + proximo
        novo_caminho = caminho.replace(atual, proximo)
        proxima_url = urlunsplit([protocolo, dominio, novo_caminho, filtro, fragmento])
        try:
            arquivo_destino = os.path.join(output_dir, os.path.basename(proxima_url))
            urlretrieve(proxima_url, arquivo_destino)
            print(f'Arquivo {os.path.basename(proxima_url)} baixado com sucesso de {proxima_url}')
        except IOError:
            print(f'Não foi possivel encontrar {proxima_url}')
            erros += 1
        contador += 1


# comandos usados na vídeo para referência
if __name__ == '__main__':
    url = 'https://jtemporal.com/images/gitfichas/001.jpg'
    baixar_arquivos(url, 'imagens')