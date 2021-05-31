teams = ['Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
         'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
         'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
         'América-MG', 'Chapecoense', 'Vitória', 'Paraná']

print(f'The firts 5 teams: {teams[0:5]}')

print('\n')
print(f'Alphabetical Teams: {sorted(teams)}')
print('\n')

print(f'The last 4 places: {teams[-4:]}')

print('\n')
print(f'Chapecoense is in the position: {teams.index("Chapecoense")+1}')