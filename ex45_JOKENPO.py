import random
jogador = str(input('Pedra, papel ou tesoura: ')).strip().lower()
computador = random.choice(list(['papel', 'pedra', 'tesoura']))
print('\nJO\nKEN\nPO')
print('\n')
print(f'Voce escolheu {jogador.upper()} e o computador escolheu {computador.upper()}')
if jogador== 'pedra':
    if computador == 'tesoura':
        print('VOCE GANHOU')
    if computador == 'pedra':
        print('VOCE EMPATOU')
    if computador == 'papel':
        print('VOCE PERDEU')
##############################################################
if jogador == 'tesoura':
    if computador == 'tesoura':
        print('VOCE EMPATOU')
    if computador == 'pedra':
        print('VOCE PERDEU')
    if computador == 'papel':
        print('VOCE GANHOU')
if jogador== 'papel':
    if computador == 'tesoura':
        print('VOCE PERDEU')
    if computador == 'pedra':
        print('VOCE GANHOU')
    if computador == 'papel':
        print('VOCE EMPATOU')