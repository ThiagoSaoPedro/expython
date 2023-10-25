from datetime import datetime


info = {}

info['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
info['Idade'] = datetime.now().year - nasc
info['ctps'] = int(input('Carteira de trabalho (0 = não tem): '))
print(40 * '-=')

if info['ctps'] == 0:
    for k, v in info.items():
        print(f'- {k} tem o valor {v}')
else:
    info['Ano de contratação'] = int(input('Digite o ano da contratação: '))
    info['Salário'] = float(input('Digite seu salário: R$ '))
    info['Aposentadoria'] = info['Idade'] + ((info['Ano de contratação'] + 35) - datetime.now().year)
    for k, v in info.items():
        print(f'- {k} tem o valor {v}')
