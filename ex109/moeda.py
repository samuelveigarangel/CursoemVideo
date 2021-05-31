def aumentar(preco, taxa, form=False):
    '''
      Metodo Aumentar preço conforme a taxa fornecida
    :param preco: Paramentro para preço do produto
    :param taxa:  Paramentro para taxa a ser aumentada em cima do produto
    :param form: Paramentro para formatação do preço
    :return:
    '''
    res = preco + (preco*taxa/100)
    return res if not form else moeda(res)

def diminuir(preco, taxa, form=False):
    '''
        Metodo Diminuir preço conforme a taxa fornecida
    :param preco: Paramentro para preço do produto
    :param taxa:  Paramentro para taxa a ser diminuida em cima do produto
    :param form: Paramentro para formatação do preço
    :return:
    '''
    res = preco - (preco*taxa/100)
    return res if not form else moeda(res)


def dobro(preco, form=False):
    '''
       Metodo para dobrar o preço
    :param preco: paramentro para preço do produto
    :param form:  parametro para formatação do preço
    :return:
    '''
    res = preco*2
    return res if not form else moeda(res)


def metade(preco, form=True):
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