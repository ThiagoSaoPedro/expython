soma = 0
cont = 0
for v in range(1, 7):
    num = int(input('Digite um valor '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você digitou {cont} números válidos e a soma deles foi {soma}')