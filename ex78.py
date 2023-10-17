v = []
menor = 0
maior = 0
for cont in range(0, 5):
    v.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        menor = maior = v[cont]
    else:
        if v[cont] > maior:
            maior = v[cont]
        if v[cont] < menor:
            menor = v[cont]
print(f'\nO menor digitado foi {menor} e está na(s) posição(oẽs) ' ,end='')
for p, n in enumerate(v):
    if n == menor:
        print(f'{p}...', end=' ')
print(f'O maior digitado foi {maior} e está na(s) posição(oẽs) ' ,end='')
for p, n in enumerate(v):
    if n == maior:
        print(f'{p}...', end=' ')
print('\n')