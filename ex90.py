aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = str(input(f'Média de {aluno["Nome"]}: '))
print()
for k, v in aluno.items():
    print(f'{k} é igual a {v}')