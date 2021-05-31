v = int(input('Digite a velocidade: '))
if v <= 80:
    print('Velocidade dentro do limite')
else:
    print(f'Velocidade acima do limite. Valor da multa: R$ {(v-80)*7}')