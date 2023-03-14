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

# Retornando refeições unicas

def get_unique_foods(data):
    # utilizando o i[1] para acessar a comida
    # array padrão de saida da get_data: ['nome', 'comida', 'dia']
    foods_data = [element[1] for element in data]
    # utilando o set(array) pois não retornarão valores repetidos
    # transformando em um array de unique itens
    foods_unique = set(foods_data)
    return foods_unique


# teste
print(get_unique_foods(get_data('data/orders_1.csv')))


def analyze_log(path_to_file):
    raise NotImplementedError
