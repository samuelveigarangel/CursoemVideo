def fat(num, show=False):
    f = 1
    for x in range(num, 0, -1):
        f *= x
        if show:
            if x == 1:
                print(f'{x} = ', end='')
            else:
                print(x, end=' x ')
    return f


print(fat(20, show=True))
