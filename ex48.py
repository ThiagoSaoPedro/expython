soma = 0
for a in range(1, 501, 2):
    if a % 3 == 0:
        soma = soma + a
print(f'A soma de todos os números solicitados é {soma}')