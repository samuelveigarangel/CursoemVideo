name = list()
nota = list()
y = 0
while True:
    name.append(str(input("Student's name: ")))
    for i in range(2):
        nota.append(float(input('Enter student grade: ')))
    name.append(nota[:])
    nota.clear()
    o = ' '
    while o not in 'yn':
        o = str(input('Do you want continue: [Y/N] ')).lower().split()[0]
        if o not in 'yn':
            print('Wrong anwser. Type Again!')
    if o == 'n':
        break
print('No. Student        Average'.center(20))
print('-' * 30)
for i in range(1, len(name), 2):
    y += 1
    print(y, ' ', "".join(map(str, name[i-1])), '        ', sum(name[i])/len(name[i]))
y = 0
while y != 999:
    y = int(input('Show which students grade: (999 to exit) '))
    if y != 999:
        print(name[y*2-1])