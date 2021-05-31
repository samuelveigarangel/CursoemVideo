a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite o termo da razão: '))
termo = int(input('Digite o limite do termo: '))
for x in range(1, termo):
    print(f'Termo {x}: {a1+(x-1)*r}')