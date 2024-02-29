import os
from zipfile import ZipFile

def compactar(pasta, lista_extensoes, caminho_resultado):
    with ZipFile(caminho_resultado, 'w') as zip_resultante:
        for raiz, _, arquivos in os.walk(pasta):
            caminho_relativo = os.path.relpath(raiz, pasta)
            for arquivo in arquivos:
                _, ext = os.path.splitext(arquivo)
                if ext.lower() in lista_extensoes:
                    zip_resultante.write(
                        os.path.join(raiz, arquivo),
                        arcname=os.path.join(caminho_relativo, arquivo)
                    )


# comandos usados na vídeo para referência
if __name__ == '__main__':
    compactar('para_compactar', ['.jpg','.txt'], 'minhas-fotos.zip')