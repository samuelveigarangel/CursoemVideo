player = dict()
player['name'] = str(input('Enter the name of the player: '))
matches = int(input(f'Enter the number of matches from {player["name"].upper()[0]+player["name"].lower()[1:]}: '))
player['goals'] = list()
for x in range(matches):
    player['goals'].append(int(input(f'How many goals in the match {x+1}: ')))
for x in range(len(player['goals'])):
    print(f'In match {x+1} the player {player["name"]} scored {player["goals"][x]}')
player['total'] = sum(player['goals'])
print(f'Total of {player["total"]} goals')
