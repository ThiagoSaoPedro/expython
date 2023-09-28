contp = 0
contmais = 0
contmenos = 0
for v in range(1, 6):
    contp += 1
    peso = float(input(f'Digite o peso da {contp} pessoa '))
    if v == 1:
        contmais = peso
        contmenos = peso
    else:
        if peso > contmais:
            contmais = peso
        if peso < contmenos:
            contmenos = peso
print(f'O maior peso foi {contmais:.1f}')
print(f'O menor peso foi {contmenos:.1f}')