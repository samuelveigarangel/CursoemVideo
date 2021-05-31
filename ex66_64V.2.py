cont = a = 0
while True:
    n = int(input('Enter a number: '))
    if n == 999:
        break
    a += n
    cont += 1

print(f'Typed numbers: {cont}. Sum of numbers: {a}')