import csv


def unir_csv(arquivos, caminho_arquivo_resultante):
    # cria lista com todos campos
    campos = []
    for arquivo in arquivos:
        with open(arquivo, 'r', encoding='utf-8') as csv_entrada:
            campo = csv.DictReader(csv_entrada).fieldnames
            campos.extend(f for f in campo if f not in campos)

    # escreve dados no arquivo resultante com base na lista de campos
    with open(caminho_arquivo_resultante, 'w', encoding='utf-8', newline='') as csv_saida:
        escrita = csv.DictWriter(csv_saida, fieldnames=campos)
        escrita.writeheader()
        for arquivo in arquivos:
            with open(arquivo, 'r', encoding='utf-8') as csv_entrada:
                leitor = csv.DictReader(csv_entrada)
                for linha in leitor:
                    escrita.writerow(linha)


# comandos usados na vídeo para referência
if __name__ == '__main__':
    unir_csv(['turma1.csv', 'turma2.csv'], 'alunos.csv')