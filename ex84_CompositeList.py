n = list()
n1 = list()
n2 = list()
x = 0

while True:
    n.append(str(input('Type your name: ')))
    n.append(int(input('Enter your Weight: ')))
    n1.append(n[:])
    n.clear()
    x += 1
    o = ' '
    if x > 1:
        while o not in 'yn':
            o = str(input('Do you want continue: [Y/N] ')).lower().split()[0]
            print(o)
            if o not in 'yn':
                print('Wrong anwser. Type Again')
    if o == 'n':
        break
    print(x)
print(f'Number of people: {len(n1)}')
aux = min(n1)
aux2 = max(n1)
n3 = list()
for i in range(len(n1)):
    if aux[1] == n1[i][1]:
        n2.append(n1[i])
    elif aux2[1] == n1[i][1]:
        n3.append(n1[i])
print(f'Lighter people: {n2}')
print(f'Heavier people {n3}')
