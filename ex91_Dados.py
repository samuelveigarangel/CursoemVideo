from random import randint as r
print('Values: ')
players = dict()
for i in range(4):
    players[f'Player {i+1}'] = r(1, 6)
    print(f'The player {i+1} got {players[f"Player {i+1}"]}')
sortedDict = sorted(players.items(), key=lambda x: x[1], reverse=True)
print('-'* 30)
print('Winners'.center(30))
print('-'* 30)
for i in range(4):
    print(f'{i+1}°', " got ".join(map(str, sortedDict[i])))