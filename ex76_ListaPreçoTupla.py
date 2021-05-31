itens = ('Book', '12.95', 'Pencil', '2.95', 'Pen', '3.50')
print('-'* 40)
print(f'{"Price list":^40}')
print('-'* 40)
for x in range(len(itens)):
    if x % 2 == 0:
        print(f'{itens[x]:.<30}', end=' $ ')
    else:
        print(itens[x])

print('-'* 40)


"""for x in range(0, len(itens), 2):
    print(f'{itens[x]:.<30}$ {itens[x+1]}')
"""