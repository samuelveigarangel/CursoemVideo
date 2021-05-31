import random
lista = ['João', 'Samuel', 'Rafael', 'Giuliano']
print(f'Número 1: {lista[0]}, Número 2: {lista[1]}, Número 3: {lista[2]}, Número 4: {lista[3]}')
random.shuffle(lista)
print(f'Lista ordenada: {lista}')
