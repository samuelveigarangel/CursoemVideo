casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
anos = int(input('Informe em quantos anos voce ira pagar: '))
emprestimo = anos*12
if casa/emprestimo <= salario*0.3:
    print('Emprestimo aprovado')
else:
    print('Emprestimo reprovado')