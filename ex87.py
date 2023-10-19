matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somac = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))

for l in range(0, 3):
    somac += matriz[l][2]

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[1][c] > maior:
            maior = matriz[1][c]

print(40 * '=')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(40 * '=')
print(f'A soma dos valores da terceira coluna é {somac}')
print(f'A soma de todos os valores pares digitados é {somap}')
print(f'O maior valor da segunda linha é {maior}')