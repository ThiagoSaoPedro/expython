cont = cont50 = cont20 = cont10 = cont1 = 0
print(50 * '-')
print('CAIXA ELETRÔNICO')
valor = int(input('Digite o valor do saque: '))
while True:
    if valor % 50 >= int(0):
        cont50 = int(valor / 50)
        valor = valor % 50
        if valor == 0:
            break
    if valor % 20 >= int(0):
        cont20 = int(valor / 20)
        valor = valor % 20
        if valor == 0:
            break
    if valor % 10 >= int(0):
        cont10 = int(valor / 10)
        valor = valor % 10
        if valor == 0:
            break
    if valor % 1 >= int(0):
        cont1 = int(valor / 1)
        valor = valor % 1
        if valor == 0:
            break
if cont50 > 0:
    print(f'Total de {cont50} cédulas de R$50')
if cont20 > 0:
    print(f'Total de {cont20} cédulas de R$20')
if cont10 > 0:
    print(f'Total de {cont10} cédulas de R$10')
if cont1 > 0:
    print(f'Total de {cont1} cédulas de R$1')
