n1 = int(input('Digite o primeiro número '))
n2 = int(input('Digite o segundo número '))
opcao = int(input('SELECIONE A OPÇÃO: \n [1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR \n [4] DIGITAR NOVAMENTE \n [5] SAIR DO PROGRAMA \n'))
while opcao != 5:   
    if opcao == 1:
        print(f'A soma dos dois números é {n1 + n2}')
    elif opcao == 2:
        print(f'A Multiplicação entre os dois números é igual {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print('Os números são iguais')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número '))
        n2 = int(input('Digite o segundo número '))
 
    opcao = int(input('SELECIONE A OPÇÃO: \n [1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR \n [4] DIGITAR NOVAMENTE \n [5] SAIR DO PROGRAMA \n'))
if opcao == 5:
    print('Adeus')

    