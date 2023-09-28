cont = 0
n = int(input('Digite um número '))
for v in range(1, n+1):
    if n % v == 0:
        cont += 1        
if cont == 2:
    print(f'Seu número é primo e só foi dividido por 1 e por ele mesmo!')
else:
    print(f'Seu número não é primo e foi dividido {cont} vezes')

    