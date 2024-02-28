import pickle


def salvar_dicio(dict_para_exportar, caminho_do_arquivo):
    with open(caminho_do_arquivo, 'wb') as arquivo:
        pickle.dump(dict_para_exportar, arquivo)

def carregar_dicio(caminho_do_arquivo):
    with open(caminho_do_arquivo, 'rb') as arquivo:
        return pickle.load(arquivo)


# comandos usados na vídeo para referência
if __name__ == '__main__':
    dicio_teste = {1: 'a', 2: 'b', 3: 'c'}
    salvar_dicio(dicio_teste, 'dicio.pickle')
    dicio = carregar_dicio('dicio.pickle')
    print(dicio)  # {1: 'a', 2: 'b', 3: 'c'}