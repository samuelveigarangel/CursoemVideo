pessoa = dict()
aux = dict()
cad = list()
soma = 0
while True:
    pessoa.clear()
    pessoa['name'] = str(input('Digite seu nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite seu sexo [F/M]: ')).upper().split()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro. Digite F para feminino e M para masculino.')
    pessoa['idade'] = int(input('Digite sua idade: '))
    soma += pessoa['idade']
    cad.append(pessoa.copy())
    while True:
        op = str(input('Deseja continuar [S/N]: ')).upper().split()[0]
        if op in 'SN':
            break
        print('Erro. Digite "S" para sair e "N" para continuar.')
    if op == 'N':
        break

print(f'Foram cadastradas {len(cad)} pessoas')
print(f'A media de idade é: {soma/len(cad)}')

for x in cad:
    if x['sexo'] == 'F':
       print(f'lista das mulheres: {x["name"]}')

for x in cad:
    if x['idade'] >= soma/len(cad):
        print(f'Lista das pessoas acima da idade media: {x}')
