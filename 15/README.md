# Desafio #15: Baixar arquivos sequenciais

Seu objetivo é implementar uma função `baixar_arquivos()`, que recebe dois argumentos de entrada: a URL para a primeira imagem de uma sequência e o caminho para o diretório de destino onde salvar as imagens baixadas.

## Exemplo de entrada e saída

Usando o exemplo a URL a seguir que hospeda 3 imagens, sendo a primeira imagem encontrada em [https://jtemporal.com/images/gitfichas/001.jpg](https://jtemporal.com/images/gitfichas/001.jpg).


```console
>>> url = 'https://jtemporal.com/images/gitfichas/001.jpg'
>>> download_files(url, './images')
```