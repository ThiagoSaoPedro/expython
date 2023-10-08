while True:
    n = int(input('Digite um número: [número menor que 0 para encerrar o programa]'))
    print(50 * '-')
    if n < 0:
        break
    cont = 0  # Reset do contador para cada número
    while cont < 10:
        cont += 1
        r = n * cont
        print(f'{n} x {cont} = {r}')
    print(50 * '-')
