nome = str(input('Digite seu nome completo: ')).strip()
print(f'Nome maiúsculo: {nome.upper()}')
print(f'Nome minusculo: {nome.lower()}')
print(f'Quantidade de letras: {len(nome)-nome.count(" ")}')
print(f'Qnt letras primeiro nome: {nome.find(" ")}')