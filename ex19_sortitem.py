import random
lista = ['João', 'Samuel', 'Rafael', 'Giuliano']
print(f'Número 1: {lista[0]}, Número 2: {lista[1]}, Número 3: {lista[2]}, Número 4: {lista[3]}')
n = random.randint(0,3)
print(f'O numero sorteado foi: {n+1}. Aluno: {lista[n]}')
