aux = False
cont = 0
n = []
while aux != True:
    n.append(int(input('Enter a number: ')))
    cont += 1
    q = str(input('Continue ? [Y/N]')).strip().lower()[0]
    if q == 'n':
        aux = True
print(f'Average: {sum(n)/cont}. Max value: {max(n)}. Min value: {min(n)}')