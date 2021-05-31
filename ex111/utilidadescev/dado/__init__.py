from ex111.utilidadescev import moeda, dado
def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print('Erro')
        else:
            valido = True
            return float(entrada)




'''    valido = False
    while not valido:
        preco = str(input('Digite seu preço: '))
        if preco.isalpha():
            print('Dado inválido')
        else:
            valido = True
            return float(preco)'''