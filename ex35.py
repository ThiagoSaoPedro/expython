r1 = float(input('Digite o 1 segmento '))
r2 = float(input('Digite o 2 segmento '))
r3 = float(input('Digite o 3 segmento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triangulo')
else:
    print('Os segmentos não podem formar um triangulo')