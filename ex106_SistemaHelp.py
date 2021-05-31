c = ('\033[m',          #0 - sem cores
     '\033[0;30;41m',   #1 - vermelho
     '\033[0;30;42m',   #2 verde
     '\033[0;30;43m',   #3 amarelho
     '\033[0;30;44m',   #4 azul
     '\033[0;30;45m',   #5 roxo
     '\033[7;30m'       #6 branco
     )

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'')
    print(c[6], end='')
    help(comando)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('Sistema de ajuda PyHelp', 0)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('Até Logo!', 1)