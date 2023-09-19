nasc = int(input('Digite o ano em que nasceu '))
idade = 2023 - nasc
print(f'Quem nasceu em {nasc} tem {idade} em 2023')
if idade < 18:
    faltam = 18 - idade
    print(f'Ainda faltam {faltam} anos para o alistamento obrigatório')
    anoalist = nasc + 18
    print(f'Seu alistamento sera {anoalist}')
elif idade == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE!!!')
else:
    fazem = idade - 18
    print(f'Voce deveria ter se alistado há {fazem} anos')
    anoalist = nasc + 18
    print(f'Seu alistamento foi {anoalist}')

