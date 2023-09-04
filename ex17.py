import math
co = float(input('Digite o valor do cateto oposto '))
ca = float(input('Digite o valor do cateto adjascente '))
hi = math.hypot(co, ca)
print('A hipotenusa do triângulo é {:.2f}'.format(hi))