total = cont = 0
opcao = 'S'
n = int(input('Digite um número: '))
maior = menor = n

while opcao != 'N':
    cont += 1
    total = total + n

    if n > maior:
        maior = n

    if n < menor:
        menor = n

    opcao = str(input('Deseja digitar mais números? [N para não]: ')).upper()
    
    if opcao != 'N':
        n = int(input('Digite um número: '))

media = total / cont
print(f'A média foi {media:.1f}')
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')
