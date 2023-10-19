valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')

valores2 = []
for cont in range(0, 5):
    valores2.append(int(input('Digite um valor: ')))