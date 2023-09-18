a = int(input('Digite o valor de a '))
b = int(input('Digite o valor de b '))
c = int(input('Digite o valor de c '))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor número é: {}'.format(menor))
print('O maior número é: {}'.format(maior))