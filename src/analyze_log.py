import csv
import os

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
    days_data = [row[2] for row in data]
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
    info_person = [row for row in data if row[0] == person]
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

# Retornando prato mais pedido por maria

def most_requested_food_by_maria(data):
    maria_count_food = get_food_count_by_person(data, 'maria')
    maria_most_food_ordered = max(maria_count_food, key=maria_count_food.get)
    return maria_most_food_ordered

# Retornando quantas vezes arnaldo pediu hamburgueres


def count_requested_hamburguer_by_arnaldo(data):
    arnaldo_count_food = get_food_count_by_person(data, 'arnaldo')
    arnaldo_count_hamburguer = arnaldo_count_food['hamburguer']
    return arnaldo_count_hamburguer


# Retornando comida que joao nunca pediu


def food_joao_never_requested(data):
    unique_foods = get_unique_foods(data)
    joao_count_food = get_food_count_by_person(data, 'joao')
    food_joao_never_requested = set(
        [food for food in unique_foods if food not in joao_count_food.keys()]
    )
    return food_joao_never_requested

# Retornando doas que joão nunca foi na lanchonete


def days_that_joao_never_went(data):
    unique_days = get_unique_days(data)

    # filtra os arrays que contem joao
    foods_joao = [food for food in data if food[0] == 'joao']

    # retorna os dias de joao
    food_days_joao = [foods_joao[2] for foods_joao in foods_joao]

    # Retorna quais dias do joao não constam no dias unicos
    joao_not_food_days = set([
        day for day in unique_days if day not in food_days_joao
    ])

    return joao_not_food_days


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    if not os.path.isfile(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
    data = get_data(path_to_file)

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(str(most_requested_food_by_maria(data)) + '\n')
        file.write(str(count_requested_hamburguer_by_arnaldo(data)) + '\n')
        file.write(str(food_joao_never_requested(data)) + '\n')
        file.write(str(days_that_joao_never_went(data)))
