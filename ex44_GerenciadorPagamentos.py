valor = float(input('Digite o preço do produto: '))
pag = int(input('Escolha a forma de pagamento. \n 1. A vista/cheque (10% desc) \n 2. A vista no cartao (5% desc) \n 3. Ate 2x no cartao (S/ desc) \n 4. 3x+ no cartao (20% de juros)\n '))
if pag == 1:
    print(f'A vista \n Valor a pagar: {valor*0.90}')
elif pag == 2:
    print(f'A vista no cartao \n Valor a pagar: {valor*0.95}')
elif pag == 3:
    print(f'2x no cartao \n Valor a pagar: {valor/2} reais em 2 parcelas')
elif pag == 4:
    par = int(input('Total de parcelas: '))
    print(f'3x+ no cartao \n Valor a pagar: {(valor*1.20)/par} reais em {par} parcelas')
else:
    print('Opcao invalida, tente novamente!!')