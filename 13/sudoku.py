from itertools import product


def resolver_sudoku(sudoku):
    for (linha, coluna) in product(range(0, 9), repeat=2):
        if sudoku[linha][coluna] == 0:  # encontra célula vazia
            for num in range(1, 10):
                permitido = True  # confere se o número é permitido na linha/coluna/sudoku parcial
                for i in range(0, 9):
                    if num in (sudoku[i][coluna], sudoku[linha][i]):
                        permitido = False
                        break  # quando o número não é permitido na linha ou coluna
                for (i, j) in product(range(0, 3), repeat=2):
                    if sudoku[linha - linha % 3 + i][coluna - coluna % 3 + j] == num:
                        permitido = False
                        break  # quando o número não é permitido na permitido sudoku parcial
                if permitido:
                    sudoku[linha][coluna] = num
                    if tentativa := resolver_sudoku(sudoku):
                        return tentativa
                    sudoku[linha][coluna] = 0
            return False  # quando não é possível colocar um número na célula
    return sudoku


def mostrar_sudoku(sudoku):
    # troca zeros por asteriscos
    sudoku = [['*' if num == 0 else num for num in linha] for linha in sudoku]
    print()
    for linha in range(0, 9):
        if ((linha % 3 == 0) and (linha != 0)):
            print('-' * 33)  # desenha linha horizontal
        for coluna in range(0, 9):
            if ((coluna % 3 == 0) and (coluna != 0)):
                print(' | ', end='')  # desenha linha vertical
            print(f' {sudoku[linha][coluna]} ', end='')
        print()
    print()

sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# comandos usados na vídeo para referência
if __name__ == '__main__':
    mostrar_sudoku(sudoku)
    resolvido = resolver_sudoku(sudoku)
    mostrar_sudoku(resolvido)