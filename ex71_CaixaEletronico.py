n = int(input('Enter withdrawn amount: '))
notas50 = n//50
notas20 = (n%50)//20
notas10 = ((n%50)%20)//10
notas1 = (((n%50)%20)%10)//1
print(f'Amount $50: {notas50}. Amount $20: {notas20}. Amount $10: {notas10}. Amount $1: {notas1} ')