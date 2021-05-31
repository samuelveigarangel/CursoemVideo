while True:
    n = int(input('Enter the number to show multiplication table: '))
    if n < 0:
        print('Finish')
        break
    for i in range(1, 11):
        print(f'{n}x{i} = {n * i}')