pessoas = []
dados = []
pmaior = 0
pmenor = 0
cont = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    dados.append(pessoas[:])
    cont += 1
    pessoas.clear()
    opcao = str(input('Deseja continuar? [S/N]').upper())
    if opcao == 'N':
        break
pmaior = pmenor = dados[0][1]
for p in dados:
    if p[1] > pmaior:
        pmaior = p[1]
    if p[1] < pmenor:
        pmenor = p[1] 

print(f'Os dados foram:\n {dados}')
print(f'Ao todo, você cadastrou {len(dados)}')
print(f'O maior peso foi {pmaior}')
print(f'O maior peso foi {pmenor}')