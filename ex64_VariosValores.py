cont = n = a =0
while n != 999:
    n = int(input('Enter a number: '))
    if n < 999:
        a += n
        cont += 1
print(f'Typed numbers: {cont}. Sum of numbers: {a}')