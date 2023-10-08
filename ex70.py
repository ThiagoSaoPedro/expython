total = totmil = menor = cont = 0
barato = ''
while True:
    produto = input('Digite o nome do Produto: ')
    preço = float(input('Digite o Preço do produto em reais: '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar [S/N]: ').strip().upper()
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de 1000 reais!')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
