def readint(msg):
    while True:
        try:
           n = int(input(msg))
        except:
            print('Erro! Enter a valid number')
            continue
        else:
            return n


def readfloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('Erro! Enter a valid number')
            continue
        else:
            return n


n = readint('Enter an integer: ')
n1 = readfloat('Enter a real number: ')
print(f'You Typed {n} and {n1}')