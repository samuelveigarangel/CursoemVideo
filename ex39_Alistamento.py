from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
if date.today().year - ano < 18:
    print(f'Ainda Falta {18-(date.today().year - ano)} ano para se alistar')
elif date.today().year - ano > 18:
    print(f'Passou {(date.today().year - ano)-18} ano(s) da sua data de alistamento')
elif date.today().year - ano == 18:
    print('Esta no ano de voce se alistar')