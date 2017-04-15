import random

lista = [random.randint(0,1) for i in range(100)]

print('Aguila: {} \nBandera: {}'.format(lista.count(0),lista.count(1)))