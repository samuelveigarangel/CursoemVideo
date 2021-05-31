n = int(input('Digite um número: '))
count = 0
a = 1
if n == 1 and n == 0 and n == -1:
    print('Numero n primo')
else:
    for x in range(1, n):
        if n%1 == 0 and n%x == 0:
            count += 1
            if count == 2:
              a = 0
    print('numero primo' if a == 1 else 'numero n primo')