l1 = float(input('Digite o lado 1 do triangulo: '))
l2 = float(input('Digite o lado 2 do triangulo: '))
l3 = float(input('Digite o lado 3 do triangulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
     print('EQUILÁTERO. Todos os lados iguais')
    elif l1 == l2 or l1 == l3 or l3 == l2:
     print('ISÓSCELES. Dois lados iguais')
    elif l1 != l2 != l3:
     print('ESCALENO. Todos os lados diferentes')
else:
    print('Triangulo impossivel')