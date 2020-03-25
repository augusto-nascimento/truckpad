# python native imports
from itertools import cycle
from random import randint, choice
from decimal import Decimal

# django
from django.contrib.gis.geos import Point

# Third-party app imports
from model_mommy.recipe import Recipe
from faker import Faker

# project imports
from nucleo.models import Veiculo, Motorista, TerminalVeiculo

faker = Faker('pt_BR')

def placa_generator(n=1):
    
    placa_list = []
    characters = [chr(i) for i in range(65, 91)]
    for i in range(n):
        placa = ''
        for c in range(3):
            placa += choice(characters)
        placa += str(randint(1, 9999)).zfill(4)
        placa_list.append(placa)
    
    return placa_list

def data_saida():
    date = [None, None]
    for i in range(10):
        date.append(
            faker.date_time_between(start_date='-30d', end_date='now')
        )
    return date

def local():
    point = faker.local_latlng(country_code='BR')
    return Point(float(point[0]), float(point[1]))

motorista = Recipe(
    Motorista,
    nome=cycle(faker.name() for i in range(10000)),
    data_nascimento=cycle(faker.date_between(start_date='-60y', end_date='-18y') for i in range(10000))
)

veiculo = Recipe(
    Veiculo,
    placa=cycle(placa_generator(10000)),
    proprietario=cycle([True, False, None])
)

terminal_veiculo = Recipe(
    TerminalVeiculo,
    possui_carga=cycle([True, False, None]),
    entrada=cycle(faker.date_time_between(start_date='-7d', end_date='now') for i in range(10)),
    saida=cycle(data_saida()),
    origem=cycle(local() for i in range(1000)),
    destino=cycle(local() for i in range(1000))
)