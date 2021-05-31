from time import sleep
n1 = float(input('Enter a number: '))
n2 = float(input('Enter another number: '))
x = False
while not x:
    option = int(input('Select the option:\n 1. Sum\n 2. Multiply\n 3. Max\n 4. New numbers\n 5. Exit\n '))
    if option == 1:
        print(f'Sum: {n1+n2}')
        sleep(2)
    elif option == 2:
        print(f'Mutiply: {n1*n2}')
        sleep(2)
    elif option == 3:
        print(f'Max number: {max(n1, n2)}')
        sleep(2)
    elif option == 4:
        n1 = float(input('Enter a number: '))
        n2 = float(input('Enter another number: '))
    elif option == 5:
        print('Exiting...')
        x = True
    else:
        print('Wrong Option. Try again.')