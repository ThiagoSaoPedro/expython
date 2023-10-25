galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M ou F]')).upper()[0]
        if pessoa['Sexo'] in ['M', 'F']:
            break
        print('Erro! por favor digite apenas M ou F')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S ou N]')).upper()[0]
        if resp in ['S', 'N']:
            break
        print('Erro! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) ao todo temos {len(galera)} pessoas cadastradas!')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos')
print(f'C) As mulheres cadastradas foram :', end=', ')
for p in galera:
    if p['Sexo'] in 'Ff':
        print('{p["Nome"]}', end='')
print()
print(f'D) Lista das pessoas que estão acima da média de idade: ')
for p in galera:
    if p['Idade'] >= média:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()

