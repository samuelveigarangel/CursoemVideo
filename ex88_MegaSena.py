from random import sample
n = int(input('How much do you want to bet: '))
numbers = list()
games = list()
for i in range(n):
    numbers.append(sample(range(1, 61), 6))
    games.append(f'Game {i+1}')
    games.append(numbers[:])
    numbers.clear()

print('-' * 27)
print('Lotery'.center(27))
print('-' * 27)
for i in range(1, n*2, 2):
    print(games[i-1], '->', " ".join(map(str, *games[i])))

