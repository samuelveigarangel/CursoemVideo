from _datetime import date
ano = int(input('Digite o ano: '))
print('Este ano é bissexto' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else 'Este ano não é bissexto')