num = int(input('Digite o número: '))
print(f'Unidade {num//1%10}')
print(f'Dezena {num//10%10}')
print(f'centeza {num//100%10}')
print(f'Milhar {num//1000%10}')