cont = n = r = 0
while n != 999:
    n = int(input('Digite um número [digite 999 para parar]'))
    cont += 1
    r = r + n
r = r - 999
print(f'Você digitou {cont} número(s) e a soma deles é {r}')