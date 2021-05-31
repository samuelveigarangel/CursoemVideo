aux = aux2 = aux3 = 0
while True:
    gender = ' '
    age = int(input('Age: '))
    while gender not in 'mf':
         gender = str(input('Gender: ')).strip().lower()[0]
    if age <= 18:
        aux += 1
    if gender == 'm':
        aux2 += 1
    if age < 20 and gender == 'f':
        aux3 += 1
    n = str(input('Continue ? [Y/N]')).strip().lower()[0]
    if n == 'n':
        break
print(f'Under 18: {aux}. Gender male: {aux2}. Female under 20: {aux3}')