print(25 * '-', '\nSequência de Fibonacci\n' + 25 * '-')
vezes = int(input('Quantos termos você deseja exibir? '))
t1 = 0
t2 = 1
print(f'{t1} - {t2}', end='')
cont = 3
while cont < vezes:
    t3 = t1 + t2
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - FIM')