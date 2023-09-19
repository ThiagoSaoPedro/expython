num = int(input('Digite um número inteiro '))
escolha = int(input('Escolha uma das bases para conversão:\n[ 1 ] Converter para BÍNARIO \n[ 2 ] Converter para OCTAL\n[ 3 ] Converter para HEXADECIMAL '))
if escolha == 1:
    n = bin(num)
    print(f'O número {num} em binário é: {n[2:]}')
elif escolha == 2:
    n = oct(num)
    print(f'O número {num} em octal é: {n[2:]}')
elif escolha == 3:
    n = hex(num)
    print(f'O número {num} em hexadecimal é: {n[2:]}')
else:
    print('Escolha inválida. Por favor, selecione uma opção válida (1, 2 ou 3).')