def fatorial(n, show):
    resultado = 1
    while True:

        if show == 0:
            while n > 0:
                resultado = resultado * n
                n -= 1
            break
        elif show == 1:
            while n >= 2:
                resultado = resultado * n
                print(f'{n} x ', end = '')
                n -= 1
            print('1 =', end=' ')
            break
    print(resultado)

fatorial(5, 1)


