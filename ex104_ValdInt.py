def leiaInt(num):
    value = 0
    while True:
        value = input(num)
        if value.isnumeric():
            return value
        else:
            print('\033[0;31mErr! Type again\033[m')


n = leiaInt('Enter a number: ')
print(f'Your number is: {n}')