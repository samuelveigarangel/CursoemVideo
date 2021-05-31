n = int(input('Enter terms fibonacci number: '))
t1 = 0
t2 = 1
aux = 0
cont = 0
aux2 = 0
print(0, end='-')
if n > 1:
    print(1, end='-')
while cont < n-2:
    tn = t1+t2
    print(f'{tn}', end='-')
    if aux2 == 0:
       t1 = tn
       aux = 0
       aux2 = 1
    if aux == 1:
        t2 = tn
        aux = 0
        aux2 = 0
    aux += 1
    cont+= 1
print('Finish')