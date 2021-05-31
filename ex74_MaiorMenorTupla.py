from random import sample
n = tuple(sample(range(100000), 5))
print(f'Numbers generated: {n}')
print(f'Number max: {max(n)}')
print(f'Number min: {min(n)}')