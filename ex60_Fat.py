n = int(input('Enter a number for factorial: '))
x = n
while x > 0:
    x -= 1
    if x >= 1:
     n *= x
print(f'Factorial: {n}')