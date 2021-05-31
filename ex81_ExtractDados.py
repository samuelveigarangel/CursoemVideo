n = list()
while True:
    n.append(int(input('Enter a number:' )))
    o = str(input('Do you want continue ? [Y/N] ')).lower().split()[0]
    if o == 'n':
        break

print(f'Number of numbers: {len(n)}')
n.sort(reverse=True)
print(f'Descending Ordered Lista {n}')
if n.count(5) > 0:
    print('Number 5 is on the list')
else:
    print('Number 5 isnt on the list')