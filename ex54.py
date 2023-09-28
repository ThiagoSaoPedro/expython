contp = 0
contmais = 0
contmenos = 0
for v in range(1, 8):
    contp += 1
    ano = 2023 - int(input(f'Digite o ano em que a {contp} pessoa nasceu: '))
    if ano >= 18:
        contmais += 1
    elif ano < 18:
        contmenos += 1
print(f'Ao todo tivemos {contmais} pessoas maiores de idade')
print(f'Ao todo tivemos {contmenos} pessoas menores de idade')
