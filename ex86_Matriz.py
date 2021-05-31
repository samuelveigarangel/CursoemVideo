import numpy as np
n = list()
n1 = list()
soma = 0
for i in range(3):
        for j in range(3):
            print(f'Insert in row {i} column {j}')
            n.append(int(input('Enter a number: ')))
        n1.append(n[:])
        n.clear()

print(np.matrix(n1))