lista = []
cont = 0
while True:
    lista.append(int(input('Digite um número: ')))
    cont += 1
    opcao = str(input('Quer continuar [S/N]').lower())
    if opcao == 'n':
        break
lista.sort(reverse=True)
print(f'Você digitou {cont} elementos')
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('A lista possui o número 5')