def ficha(name=False, goals=False):
    if not name:
        name = '<desconhecido>'
    if not goals:
        goals = 0
    print(f'The Player {name} scored {goals} goals')


ficha(str(input('Enter the name of the player: ')), str(input('Number of goals: ')))