from random import randint
import time
n1 = randint(0, 10)
print('Thinking in a number')
time.sleep(2)
print('I thought')
n2 = int(input('Enter a number of 0 to 10: '))
count = 0
while n1 != n2:
    count += 1
    n2 = int(input('You miss. Enter again: '))
print(f'HIT. You need of  {count+1} attempts')