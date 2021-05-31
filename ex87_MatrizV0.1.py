import numpy as np
n = list()
n1 = list()
soma = soma2 = 0
for i in range(3):
    for j in range(3):
        print(f'Insert in row {i} column {j}')
        n.append(int(input('Enter a number: ')))
    n1.append(n[:])
    n.clear()
for i in range(3):
    for j in range(3):
        if n1[i][j] % 2 == 0:
            soma += n1[i][j]
        if j == 2:
            soma2 += n1[i][2]
print(np.matrix(n1))
print(f'Sum of pares: {soma}')
print(f'Sum of 3 column: {soma2}')
print(f'Max of 2 row{max(n1[1])}')