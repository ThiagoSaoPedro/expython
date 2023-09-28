idademed = 0
velho = 0
cont = 0
soma = 0
contm = 0

for v in range(1, 5):
    cont += 1
    print(f'Digite o nome da {cont}ª pessoa')
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]: ').upper()
    soma += idade

    if sexo == 'M':
        if cont == 1:
            velho = idade
        elif idade > velho:
            velho = idade

    if sexo == 'F' and idade < 20:
        contm += 1

idademed = soma / 4

print(f'A média de idade das pessoas é {idademed:.1f}')
print(f'A idade do homem mais velho é {velho}')
print(f'Quantidade de mulheres com menos de 20 anos: {contm}')
