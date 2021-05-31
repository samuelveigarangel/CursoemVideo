peso = float(input('Digite seu peso em kg: '))
alt = float(input('Digite sua altura em metros: '))
imc = peso/(alt*alt)
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade morbida')