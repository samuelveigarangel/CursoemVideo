def contador():
    z = 0
    print('Counting from 1 to 10 of 1 in 1.')
    for x in range(1, 11):
        print(x, end=' ')
    print('\n')
    print('Counting from 10 to 1 of 2 in 2')
    for x in range(10, 0, -2):
        print(x, end=' ')
    print('\n')
    print('Your turn')
    a = int(input('Start: '))
    b = int(input('End: '))
    c = int(input('Step: '))
    if b < a:
        b -= 1
        if c > 0:
            c *= -1
    for x in range(a, b, c):
        print(x, end=' ')

contador()