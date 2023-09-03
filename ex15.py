kms = float(input('Digite a quantidade de kms rodados'))
dias = float(input('Digite a quantidade de dias alugados'))
pkms = kms  * 0.15
pdias = dias * 60
preco = pdias + pkms
print('O total a pagar é {} reais'.format(preco))