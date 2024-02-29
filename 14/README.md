# Desafio #14: Compactar arquivos em um ZIP

Seu objetivo é implementar uma função chamada `compactar()`, que recebe três argumentos de entrada: o caminho para o diretório que você deseja incluir, uma lista de extensões de arquivo de interesse e um caminho para o arquivo de saída resultante.

## Exemplo de entrada e saída

Usando o diretório incluído de imagens e arquivos de texto como entrada:

```console
>>> compactar('para_compactar', ['.jpg','.txt'], 'minhas-fotos.zip')
```