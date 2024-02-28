def encontre_indices(lista, item):
    lista_de_indices = []
    for indice, value in enumerate(lista):
        if value == item:
            lista_de_indices.append([indice])
        elif isinstance(lista[indice], list):
            for i in encontre_indices(lista[indice], item):
                lista_de_indices.append([indice] + i)
    return lista_de_indices



# comandos usados na vídeo para referência
if __name__ == '__main__':
    exemplo = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(encontre_indices(exemplo, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(encontre_indices(exemplo, [1, 2, 3]))  # [[0, 0], [1]]