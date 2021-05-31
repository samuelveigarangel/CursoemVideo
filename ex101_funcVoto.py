from datetime import datetime


def voto(age):
    if datetime.now().year - age < 18:
        return f'Your age is {datetime.now().year - age}. STATUS: Denied.'
    elif 18 <= datetime.now().year - age <= 69:
        return f'Your age is {datetime.now().year - age}. STATUS: Required.'
    elif datetime.now().year - age > 69:
        return f'Your age is {datetime.now().year - age}. STATUS: Optional.'


print(voto(int(input('Enter your birth date: '))))
