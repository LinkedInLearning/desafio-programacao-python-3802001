def ordenando_palavras(palavras):
    return ' '.join(sorted(palavras.split(), key=str.casefold))


# comandos usados na vídeo para referência
if __name__ == '__main__':
    print(ordenando_palavras('maçã LARANJA banana'))  # banana LARANJA maçã