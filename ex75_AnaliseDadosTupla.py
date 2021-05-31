tupla = (int(input('insira um número:')), int(input('insira um número:')), int(input('insira um número:')), int(input('insira um número:')))
print(f'Number 9 show {tupla.count(9)} Times')
if 3 in tupla:
    print(f'Number 3 was  entered in the position: {tupla.index(3)+1}')
print(f'Numbers par:')
for x in range(len(tupla)):
    if tupla[x] % 2 == 0:
        print(f'{tupla[x]}', end= ' ')