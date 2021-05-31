s = float(input('Digite seu salário: '))
print(f'Novo salário: {s*1.1 if s>1250 else s*1.15}')