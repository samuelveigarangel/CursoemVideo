from random import randint
cont = 0
while True:
    p = ' '
    while p not in 'eo':
        p = str(input('Evens or Odds:')).strip().lower()[0]
        if p not in 'eo':
            print('Wrong. Enter Evens or Odds')

    n = int(input('Enter a number: '))
    c = randint(1, 10)
    print(f'Computer chose: {c}')

    if p == 'e':
        if (c+n) % 2 == 0:
            print('You win')
            cont += 1
        else:
            print('You lose')
            break
    if p == 'o':
        if (c+n) % 2 == 1:
            print('You win')
            cont += 1
        else:
            print('You lose')
            break
print(f'You won {cont} times')