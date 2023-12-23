def resumo(preço, aumento, redução):
    dobro = preço * 2
    metade = preço / 2
    mais = preço + ( preço * (aumento / 100))
    menos = preço - (preço * (redução / 100))

    print('-' * 30)
    print('Resumo do valor'.center(30))
    print('-' * 30)
    print(f'Valor análisado: R${preço},00')
    print(f'Dobro do valor: R${dobro},00')
    print(f'Metade do valor: R${metade},00')
    print(f'Valor agregado com {aumento}% do valor: R${mais}')
    print(f'Valor desagregado com {redução}% do valor: R${menos}')