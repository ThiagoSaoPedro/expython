l = []
lpar = []
limpar = []
while True:
    l.append(int(input('Digite um número: ')))
    opcao = str(input('Quer continuar [S/N]').lower())
    if opcao == 'n':
        break
for v in l:
    if v % 2 == 0:
        lpar.append(v)
    else:
        limpar.append(v)
print(l)
print(lpar)
print(limpar)
