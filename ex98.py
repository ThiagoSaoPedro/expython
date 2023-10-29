def contador(inicio, fim, passo):
    if passo == 0:
        print('Passo precisa ser maior que 0')
    if fim < inicio:
        if passo < 0:
            for v in range(inicio, fim - 1, passo):
                print(v, end=' ')
            print()
        if passo > 0:
            for v in range(inicio, fim - 1, passo * (-1)):
                print(v, end=' ')
            print()
    elif fim > inicio:
        if passo > 0:
            for v in range(inicio, fim + 1, passo):
                print(v, end=' ')
                v += passo
            print()
        if passo < 0:
            for v in range(inicio, fim + 1, passo * (-1)):
                print(v, end=' ')
                v += passo
            print()
print(83 * '-=')
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
print(83 * '-=')
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)
print(83 * '-=')
print('Agora é sua vez de personalizar a contagem!!!')
i = int(input('Início '))
f = int(input('Fim '))
p = int(input('Passo '))
print(83 * '-=')
contador(i, f, p)