ext = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'twenty']
while True:
    n = int(input('Enter a number Between 0 and 20: '))
    if 0 <= n <= 20:
        print(f'You typed {ext[n]}')
        break
    print('Type it again. Enter a number Between 0 and 20: ')
