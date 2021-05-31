from datetime import date
a = 0
b = 0
for x in range(0, 3):
    ano = int(input(f'Digite seu ano de nascimento da pessoa {x+1}: '))
    if (date.today().year - ano) >= 18:
        a += 1
    else:
        b += 1
print(f'Maiores de idade {a} \n Menores de idade {b}')