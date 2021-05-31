from math import hypot
L1 = float(input('Digite o cateto oposto: '))
L2 = float(input('Digite o cateto adjacente: '))
print(f'Hipotenusa: {hypot(L1, L2):.3f}')