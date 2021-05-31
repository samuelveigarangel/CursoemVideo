def bigger(*lst):
    print(f'{"  ".join(map(str, lst))}')
    print(f' The bigger number of list is: {max(lst)}')


bigger(10, 9, 8, 7, 6)
