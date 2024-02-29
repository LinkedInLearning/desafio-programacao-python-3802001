# Desafio #13: Solve a Sudoku

Seu objetivo é implementar uma função chamada `resolver_sudoku()`, que recebe como argumento de entrada uma lista bidimensional de listas representando um [quebra-cabeça de Sudoku](https://pt.wikipedia.org/wiki/Sudoku) não resolvido e retorna uma lista bidimensional de listas contendo a solução do quebra-cabeça.

*Atenção*: Zero é usado para representar uma célula vazia.

## Exemplo de entrada e saída

```console
>>> sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]
>>> resolver_sudoku(sudoku)
[[5, 3, 4, 6, 7, 8, 9, 1, 2],
 [6, 7, 2, 1, 9, 5, 3, 4, 8],
 [1, 9, 8, 3, 4, 2, 5, 6, 7],
 [8, 5, 9, 7, 6, 1, 4, 2, 3],
 [4, 2, 6, 8, 5, 3, 7, 9, 1],
 [7, 1, 3, 9, 2, 4, 8, 5, 6],
 [9, 6, 1, 5, 3, 7, 2, 8, 4],
 [2, 8, 7, 4, 1, 9, 6, 3, 5],
 [3, 4, 5, 2, 8, 6, 1, 7, 9]]
```

Como um desafio extra, implemente uma função mostrar_sudoku() para exibir uma grade 9x9 de números no estilo Sudoku:

```console
>>> mostrar_sudoku(sudoku)
 5  3  *  |  *  7  *  |  *  *  * 
 6  *  *  |  1  9  5  |  *  *  * 
 *  9  8  |  *  *  *  |  *  6  * 
---------------------------------
 8  *  *  |  *  6  *  |  *  *  3 
 4  *  *  |  8  *  3  |  *  *  1 
 7  *  *  |  *  2  *  |  *  *  6 
---------------------------------
 *  6  *  |  *  *  *  |  2  8  * 
 *  *  *  |  4  1  9  |  *  *  5 
 *  *  *  |  *  8  *  |  *  7  9  
```