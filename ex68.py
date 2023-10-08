import random
cont = contv = s = 0
print(30 * '-=')
print('VAMOS JOGAR PAR OU IMPAR')
print(30 * '-=')
while True:
    n = int(input('Diga um valor: '))
    escolha = input('Par ou Ímpar? [P/I]').strip().upper()
    if escolha == 'P':
        rnum = random.randint(0, 10)
        s = n + rnum
        r = s % 2
        if r == 0:
            contv += 1
            print(30 * '-')
            print(f'Você jogou {n} e o computador {rnum}. O total foi de {s}')
            print(30 * '-')
            print('Você ganhou!!! \nVamos jogar novamente...')
            print(50 * '-=')
        else:
            print(30 * '-')
            print('Você perdeu!!!')
            print(f'Você ganhou um total de {contv} partidas!')
            break
    elif escolha == 'I':
        rnum = random.randint(0, 10)
        s = n + rnum
        r = s % 2
        if r != 0:
            contv += 1
            print(30 * '-')
            print(f'Você jogou {n} e o computador {rnum}. O total foi de {s}')
            print(30 * '-')
            print('Você ganhou!!! \nVamos jogar novamente...')
            print(50 * '-=')
        else:
            print(30 * '-')
            print('Você perdeu!!!')
            print(f'Você ganhou um total de {contv} partidas!')
            break
    else:
        print('Escolha inválida. Por favor, escolha entre P ou I.')
        break
