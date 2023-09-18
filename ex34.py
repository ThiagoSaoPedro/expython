salario = int(input('Digite seu salário: '))
if salario > 1250:
    salario = salario * 1.1
    aumento = 10
else:
    salario = salario * 1.15
    aumento = 15
print('Aumento de {} por cento, seu novo salário é {:.2f}'.format(aumento, salario))