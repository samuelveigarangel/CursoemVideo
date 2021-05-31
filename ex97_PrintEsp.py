def escreva(txt):
    print('-'*len(txt))
    print(txt.center(len(txt)))
    print('-'*len(txt))

txt = str(input('Enter your text: '))
escreva(txt)