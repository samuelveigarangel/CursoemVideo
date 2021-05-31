aux = n = n2 = aux2 = aux3 = total = cont = 0
prod = ' '
while True:
    prod = str(input('Enter product name: '))
    n = float(input('Enter the product value: '))
    aux2 += n
    cont += 1
    if cont == 1:
        aux3 = n
        aux = prod
    elif n < aux2:
        aux3 = n
        aux = prod
    if n > 1000:
        total += 1
    resp = ' '
    while resp not in 'yn':
        resp = str(input('Continue ? [Y/N] ')).lower()[0].strip()
    if resp == 'n':
        break
print(f'Total sum of product: {aux2}. Product over $1000: {total}. Cheapest Product Name: {aux}')


