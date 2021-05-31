n = list()
num = [[], []]
for x in range(7):
    n = int(input('Enter a number: '))
    if n% 2 == 0:
        num[0].append(n)
    elif n% 2 == 1:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Even numbers in ascending order: {num[0]}. Par numbers in ascending order: {num[1]}')