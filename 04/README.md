# Desafio #4: Encontre todos os itens

Seu objetivo é implementar uma função chamada `encontre_indices()`, que recebe uma lista de objetos e o item a ser encontrado como argumentos de entrada e retorna uma lista de índices onde esse item existe dentro da lista.

*Atenção*: Como o argumento de entrada pode ser uma lista de listas, a sua função deve ser capaz de percorrer listas multidimensionais para encontrar todas as instâncias do item, e os elementos da lista retornada também devem ser listas para indicar índices multidimensionais.

## Exemplo de entrada e saída

```console
>>> exemplo = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
>>> encontre_indices(exemplo, 2)
# [[0, 0, 1], [0, 1], [1, 1]]
>>> print(encontre_indices(exemplo, [1, 2, 3]))
# [[0, 0], [1]]
```