km = float(input('Digite distancia percorrida em km:'))
print(f'R${km*0.5 if km <= 200 else km*0.45}')
