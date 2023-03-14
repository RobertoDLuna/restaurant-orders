import csv

# Importando os dados do arquivo


def get_data(path):
    with open(path) as file:  # abrindo o arquivo
        file_readed = csv.reader(file)  # leitura de arquivo
        # converte para um array, contendo arrays
        #  com as informaçoes de cada linha
        data = [row for row in file_readed]
    return data


# teste
# print(get_data('data/orders_1.csv'))

def analyze_log(path_to_file):
    raise NotImplementedError
