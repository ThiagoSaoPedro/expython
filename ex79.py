lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opcao = str(input('Quer continuar [S/N]').lower())
    if opcao == 'n':
        lista.sort()
        break
print(lista)