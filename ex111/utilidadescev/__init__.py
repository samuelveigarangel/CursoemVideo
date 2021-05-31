from ex111.utilidadescev import moeda, dado


def resumo(preco=0, taxa=0, taxa_diminuir=0):
    print(moeda(preco))
    print(f'Aumentou em {taxa}%, preço novo {aumentar(preco, taxa, True)}')
    print(f'Diminuiu em {taxa_diminuir}%, preço novo: {diminuir(preco, taxa_diminuir, True)}')
    print(f'Dobro do preço {dobro(preco, True)}')
    print(f'Metade do preço: {metade(preco, True)}')


def aumentar(preco=0, taxa=0, form=False):
    '''
      Metodo Aumentar preço conforme a taxa fornecida
    :param preco: Paramentro para preço do produto
    :param taxa:  Paramentro para taxa a ser aumentada em cima do produto
    :param form: Paramentro para formatação do preço
    :return:
    '''
    res = preco + (preco*taxa/100)
    return res if not form else moeda(res)

def diminuir(preco=0, taxa=0, form=False):
    '''
        Metodo Diminuir preço conforme a taxa fornecida
    :param preco: Paramentro para preço do produto
    :param taxa:  Paramentro para taxa a ser diminuida em cima do produto
    :param form: Paramentro para formatação do preço
    :return:
    '''
    res = preco - (preco*taxa/100)
    return res if not form else moeda(res)


def dobro(preco=0, form=False):
    '''
       Metodo para dobrar o preço
    :param preco: paramentro para preço do produto
    :param form:  parametro para formatação do preço
    :return:
    '''
    res = preco*2
    return res if not form else moeda(res)


def metade(preco=0, form=True):
    '''
      Metodo para dividir o preço em dois.
    :param preco: Paramentro para preço do produto
    :param form: Parametro para formatação do preço
    :return:
    '''
    res = preco/2
    return res if not form else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')