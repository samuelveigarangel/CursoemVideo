n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua seguunda nota: '))
print(f'Sua média: {(n1+n2)/2}')
if (n1+n2)/2 < 5:
    print('REPROVADO')
elif (n1+n2)/2 >= 5 and (n1+n2)/2 <= 5.9:
    print('RECUPERACAO')
elif (n1+n2)/2 >= 7:
    print('Aprovado')