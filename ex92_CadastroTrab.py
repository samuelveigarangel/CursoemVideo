from datetime import datetime
register = dict()
register['name'] = str(input('Type your name: '))
register['year'] = datetime.now().year - int(input('Enter your year of birth: '))
work = int(input('Enter your carteira de trabalho (0 não tem): '))
if work > 0:
    register['work'] = work
    register['hiring'] = int(input('Enter your year of hiring: '))
    register['salary'] = float(input('Enter your salary: '))
    register['retirement'] = register['year'] + ((register['hiring'] + 35) - datetime.now().year)
else:
    register['work'] = 0
for k, v in register.items():
    print(f'{k} has the value {v}')