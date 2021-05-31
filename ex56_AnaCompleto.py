idade = 0
idade1 = 0
idade_aux = 0
count = 0
for x in range(0, 4):
    nome = (str(input('Digite seu nome: ')))
    idade = (int(input('Digite sua idade: ')))
    sexo = (str(input('Digite seu sexo : '))).strip().lower()
    if idade < 20:
        count += 1
    if idade1 < idade and sexo == 'm':
        idade1 = idade
        pessoa = idade
        nomeaux = nome
    idade_aux += idade
print(f'Pessoa mais velha: {nomeaux}. Pessoas com menos de 20: {count}. Idade media: {idade_aux/4}')
