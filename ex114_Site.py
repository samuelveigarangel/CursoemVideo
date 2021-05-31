from urllib import request
import urllib


try:
    site = request.urlopen('http://www.pudim.com.br')
except:
    print('Erro!')
else:
    print('Ok!')