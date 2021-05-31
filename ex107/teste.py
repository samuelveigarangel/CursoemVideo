import moeda

p = float(input('Digite o preço: '))
print(f'A metade de R$ {p} é R$ {moeda.metade(p)}')
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}')
print(f'Aumentando em 20%, temos R$ {moeda.aumentar(p, 20)}')
print(f'Diminuindo 10%, temos R$ {moeda.diminuir(p, 10)}')
