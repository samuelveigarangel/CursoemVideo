player = dict()
cad = list()
while True:
    player.clear()
    player['name'] = str(input('Enter name of the player: '))
    matches = int(input(f'Enter the number of matches from {player["name"]}: '))
    player['goals'] = list()
    for x in range(matches):
        player['goals'].append(int(input(f'    How many goals in the match {x+1}: ')))
    cad.append(player.copy())
    while True:
        op = str(input('Do you want continue [Y/N]: ')).upper().split()[0]
        if op in 'YN':
            break
        print('Erro. Type Y to continue or N to exit')
    if op == 'N':
        break
for p in cad:
    print(f'The player {p["name"]} has a use {sum(p["goals"])/matches} goals')