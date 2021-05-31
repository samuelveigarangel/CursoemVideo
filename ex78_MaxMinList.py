lista = []
for x in range(5):
    lista.append(int(input('Enter a number: ')))
print(f'The max value: {max(lista)} Index max: {lista.index(max(lista))}. The min value: {min(lista)} Index min: {lista.index(min(lista))}')