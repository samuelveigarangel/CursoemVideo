sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Informe seu sexo novamente [M/F]: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso.')