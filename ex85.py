#impar = []
#par = []
#lista = []
#for v in range(0, 7):
#    n = (int(input('Digite um número: ')))
#    if n % 2 == 0:
#        par.append(n)
#    else:
#        impar.append(n)
#par.sort()
#impar.sort()
#lista.append(par[:])
#lista.append(impar[:])
#print(lista)

num = [[], []]
valor = 0
for v in range(0, 7):
    valor = (int(input('Digite um número: ')))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(num)


