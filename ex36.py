import math
casa = int(input('Digite o valor da casa '))
salario = int(input('Digite seu salário '))
anos = int(input('Digite em quantos anos você pretende pagar '))
meses = anos * 12
prestacao = casa / meses
if prestacao >= salario * 0.3:
    print('Seu empréstimo foi negado!!! As parcelas ultrapassam o limite de 30% do seu salário!')
else:
    print('Seu empréstimo foi aprovado!!!')