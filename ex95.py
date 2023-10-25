lista = []

codigo = 1

while True:
    cont  = 1
    gols = []
    total = 0
    dados = {}
    dados['Nome'] = str(input('Qual o nome do jogador: '))
    partidas = int(input('Quantas partidas ele jogou? '))
    for v in range(0, partidas):
        gols.append(int(input(f'Quantos gols ele marcou na partida {cont}? ')))
        cont += 1
        total += gols[v]
    dados['Gols'] = gols
    dados['Total'] = total
    lista.append(dados.copy())
    while True:
        opcao = str(input('Deseja continuar [S / N]: ')).upper()
        if opcao == 'S':
            break
        elif opcao == 'N':
            break
        else:
            print('Opção inválida, utilize somente S ou N')
    if opcao == 'N':
        break
    codigo += 1

print(15 * '-=')
print(f'{"COD":<4}{"Nome":<15}{"Gols":^20}{"Total":^6}')
print(45 * '-')

for i, jogador in enumerate(lista):
    print(f'{i+1:<4}{jogador["Nome"]:<15}{str(jogador["Gols"]):^20}{jogador["Total"]:^6}')

while True:
    cod = int(input('Digite o código do jogador que deseja conferir os dados (999 para parar): '))

    if cod == 999:
        break

    if cod > 0 and cod <= len(lista):
        jogador = lista[cod - 1]
        print(f'LEVANTAMENTO DE DADOS DO {jogador["Nome"]}:')

        for i, gols in enumerate(jogador["Gols"]):
            print(f'No jogo {i + 1} fez {gols} gols.')
    else:
        print('Por favor, digite um código válido!')