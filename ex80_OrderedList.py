n = []
for x in range(5):
    y = int(input('Enter a number: '))
    if x == 0 or y > n[-1]:
        n.append(y)
    else:
        pos = 0
        while pos < len(n):
            if y <= n[pos]:
                n.insert(pos, y)
                break
            pos +=1
print(n)


