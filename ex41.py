anonasc = int(input('Digite o ano em que você nasceu '))
idade = 2023 - anonasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade >= 26:
    print('Classificação: MASTER')