expression = str(input('Enter your expression: '))
if expression.count('(') == expression.count(')'):
    if expression[0] == ')' or ')(' in expression:
        print('Wrong expression')
    else:
        print('Correct expression')
elif expression.count('(') != expression.count(')'):
    print('Wrong expression')