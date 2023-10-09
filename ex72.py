numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez'
, 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número entre zero a vinte: '))
if n < 0 or n > 20:
    while True:
        print('Opção inválida, o número tem que ser de 0 a 20')
        n = int(input('Digite um número entre zero a vinte: '))
        if n >= 0 and n <= 20:
            break
print(numeros[n])
