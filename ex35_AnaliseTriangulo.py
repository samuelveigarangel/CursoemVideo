r1 = float(input('Digite o lado: '))
r2 = float(input('Digite o lado: '))
r3 = float(input('Digite o lado: '))
if r1 < r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
    print(True)
else:
    print(False)