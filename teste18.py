galera = [['João', 19],['Ana', 33], ['Joaquim', 33]]
dado = []
print(galera[0])
print(galera[0][1])
for p in galera:
    print(p[0])
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

galera.clear()

totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')