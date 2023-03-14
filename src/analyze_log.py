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
# print(get_unique_foods(get_data('data/orders_1.csv')))

# Retornando dias unicos

def get_unique_days(data):
    # utilizando o i[2] para acessar a comida
    # array padrão de saida da get_data: ['nome', 'comida', 'dia']
    days_data = [element[2] for element in data]
    # utilando o set(array) pois não retornarão valores repetidos
    # transformando em um array de unique itens
    days_unique = set(days_data)
    return days_unique


# teste
# print(get_unique_days(get_data('data/orders_1.csv')))

# Retornando a contagem dos pedidos por cada pessoa


def get_food_count_by_person(data, person):
    # definindo o conjunto para os elem distintos
    count_food = {}

    # retornando as linhas onde a pessoa == person
    # utilizando o i[0] para localizar a pessoa na linha
    info_person = [elem for elem in data if elem[0] == person]
    # oara cada linha do info_person
    for row in info_person:
        # caso a comida ja exista no set
        if row[1] in count_food:
            # a key com o nome da comida recebe +1
            count_food[row[1]] += 1
        else:
            # caso não, cria a chave e acrescenta 1
            count_food[row[1]] = 1

    return count_food


# teste
# print(get_food_count_by_person(get_data('data/orders_1.csv'), 'maria'))


def analyze_log(path_to_file):
    raise NotImplementedError
