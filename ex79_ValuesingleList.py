n = []
j = x = 0
o = ' '
while True:
    n.append(int(input('Enter a number: ')))
    if n.count(n[j]) > 1:
        print('Duplicate value')
        del n[j]
        j -= 1
    j += 1
    x += 1
    if x > 4:
        o = str(input('Do you want continue [Y/N]:  ')).lower()[0]
        x = 0
        if o == 'n':
            break
n.sort()
print(f'ordered list: {n}')

#Other
"""
n1 = list()
while True: 
    n = (int(input('Enter a number: ')))
    if n not in n1:
        n.append(n)
    
"""
