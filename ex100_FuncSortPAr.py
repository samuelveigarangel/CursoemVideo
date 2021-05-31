from random import randint as r
def sorteia(lst, a):
    for x in range(a):
        lst.append(r(1, 1000))
    print(f'Random numbers is: {lst}', end=' ')
    print('\n')

def somaPar(lst):
    soma = 0
    for x in range(len(lst)):
        if lst[x] % 2 == 0:
            soma += lst[x]
    print(f'Sum of Pairs is: {soma}')

numeros = list()
sorteia(numeros, 5)
somaPar(numeros)
