# python native imports
from itertools import cycle
from random import randint, choice

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

print(placa_generator(10))