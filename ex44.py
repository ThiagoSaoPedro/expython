preco = int(input('Digite o preço das suas compras: '))
pagamento = int(input('[ 1 ] à vista dinheiro/cheque \n[ 2 ] à vista no cartão \n[ 3 ] 2x no cartão \n[ 4 ] 3x ou mais no cartão \nQual é a opção? '))
if pagamento == 1:
    preco = preco * 0.9
    print(f'Você obteve um desconto de 10% e deverá pagar {preco:.0f},00R$')
elif pagamento == 2:
    preco = preco * 0.95
    print(f'Você obteve um desconto de 5% e deverá pagar {preco:.0f},00R$')
elif pagamento == 3:
    print(f'Você não obteve desconto e terá que pagar o valor cheio de {preco:.0f},00R$')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    preco = preco * 1.2
    print(f'Você terá 20% de juros e terá que pagar o total de {preco:.0f},00R$')
else:
    print('OPÇÃO INVÁLIDA')