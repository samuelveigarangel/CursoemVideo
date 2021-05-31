num = int(input('Digite um numero qualquer: '))
choice = int(input('Escolha 1 para conversão binária\nEscola 2 para conversao octal\nEscolha 3 para conversao hexadecimal\n '))
if choice == 1:
    print(bin(num)[2:])
elif choice == 2:
    print(oct(num)[2:])
elif choice == 3:
    print(hex(num)[2:])
else:
    print('Digite novamente opcao correta')