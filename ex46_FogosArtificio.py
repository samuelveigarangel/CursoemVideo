import time
n = str(input('Digite acender para comecar a queima de fogos: '))
for x in range(10, -1, -1):
    print(f'{x} segundos para queima')
    time.sleep(1)
print('BOOOMMM')