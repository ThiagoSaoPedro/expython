pessoa = []
cont = 0
while True:
    nome = str(input('Nome: '))
    n1 = int(input('Nota 1: '))
    n2 = int(input('Nota 2: '))
    media = ((n1 + n2) / 2)
    pessoa.append([nome, n1, n2, media])
    cont += 1
    opcao = str(input('Quer continuar? [N para não]').upper())
    if opcao == 'N':
        break
print(cont)
print(30 * '=')
print(f'{"N⁰":<4}{"NOME":<10}{"MÉDIA":<8}')
print(30 * '=')
for i in range(0, cont):
    print(f'{i:<4}{pessoa[i][0]:<10}{pessoa[i][3]}')
print(30 * '=')
while True:
    escolha = int((input('Digite o número do aluno que deseja saber as notas')))
    print(f'Nota 1 = {pessoa[escolha][1]} \nNota 2 = {pessoa[escolha][2]}')
    opcao2 = str(input('Quer continuar? [N para não]').upper())
    if opcao2 == 'N':
        break
