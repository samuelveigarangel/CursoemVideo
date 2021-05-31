n = list()
n_par = list()
n_impar = list()
x = 0
while True:
    n.append(int(input('Enter a number: ')))
    if n[x] % 2 == 0:
        n_par.append(n[x])
    elif n[x] % 2 == 1:
        n_impar.append(n[x])
    x += 1
    o = ' '
    if x > 4:
        x = 0
        while o not in 'yn':
            o = str(input('Do you want continue ? [Y/N] ')).lower().split()[0]
            if o not in 'yn':
                print('Wrong answer. Type again.')
        if o == 'n':
            break
print(n)
print(n_par)
print(n_impar)
