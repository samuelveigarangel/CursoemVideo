a = dict()
a["Name"] = str(input('Enter your name: '))
a["Average"] = float(input('Type your Average: '))
if a['average'] >= 7:
    a['Status'] = 'Approved'
elif a['average'] < 7:
    a['Status'] = 'Disapproved'
for k, v in a.items():
    print(f'{k} is {v}')