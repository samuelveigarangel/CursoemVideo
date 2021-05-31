frase = str(input('Digite a frase: ')).strip().lower().replace(" ", "")
f2 = ''
for x in range(len(frase), 0, -1):
    f2 += frase[x-1]
if f2 == frase:
    print('Polidromo')
else:
    print('Não é polidromo')