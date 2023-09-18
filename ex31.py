distancia = int(input('Digite a distância da sua viagem '))
if distancia <= 200:
    preco = float(distancia * 0.5)
    print('O preço da viagem será de: {:.2f}R$!'.format(preco))
else:
    preco = float(distancia * 0.45)
    print('O preço da viagem será de: {:.2f}R$!'.format(preco))
