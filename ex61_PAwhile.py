a1 = int(input('Enter first term: '))
r = int(input('Enter number of reason: '))
termo = int(input('Enter the term limit: '))
x = 1
y = 0
while x <= termo:
    print(f'Term {x}: {a1 + (x - 1) * r}')
    x += 1
    if x == termo + 1:
        y = int(input('Do you want show more terms?'))
        termo += y
        if y == 0:
            break
