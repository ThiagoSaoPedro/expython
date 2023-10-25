dados = {}
gols = []
cont  = 1
total = 0
dados['Nome'] = str(input('Qual o nome do jogador '))
partidas = int(input('Quantas partidas ele jogou? '))
for v in range(0, partidas):
    gols.append(int(input(f'Quantos gols ele marcou na partida {cont}? ')))
    cont += 1
    total += gols[v]
dados['Gols'] = gols
dados['Total'] = total

print(dados)
print(30 * '-=')
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print(30 * '-=')
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas')
for k, v in enumerate(gols):
    print(f'   => Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {total} gols')