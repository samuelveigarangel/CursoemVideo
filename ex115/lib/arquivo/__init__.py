def create_file(name_arq):
    try:
        arq = open(name_arq, 'wt+')
    except FileNotFoundError:
        print('File created...')
        arq = open(name_arq, 'wt+')
