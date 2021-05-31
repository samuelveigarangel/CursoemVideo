import json
global date


def menu(*lst):
    c = 1
    for x in lst:
        print(f'{c} - {x}')
        c += 1
    while True:
        try:
            aux = int(input('Enter your option: '))
        except :
            print('Erro. Enter a valid option')
        else:
            if aux > len(lst) or aux <= 0:
                print('Erro. Enter a valid option')
            else:
                return aux

def see_register():
    try:
        arquivo = open('register.txt', 'r')
    except:
        print('Error reading from file')
    else:
        for x in arquivo.readlines():
            print(x, end='')
    finally:
        arquivo.close()


def register():
    name = str(input('Name: '))
    age = str(input('Age: '))
    try:
        arquivo = open('register.txt', 'at+')
    except:
        print('Error opening file for write')
    else:
        try:
            arquivo.writelines(f'{name:.<30} {age} years old\n')
        except:
            print('Error when registering')
        else:
            print('Registering successfully')
            arquivo.close()

