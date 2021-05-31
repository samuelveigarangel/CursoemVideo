from datetime import date
idade1 = int(input('Idade do atleta: '))
atual = date.today().year
idade = atual - idade1
if idade <= 9:
    print('MIRIM')
elif  idade <= 14:
    print('INFANTIL')
elif idade <=19:
    print('Junior')
elif idade <= 25:
    print('SENIOR')
elif idade > 25:
    print('MASTER')
