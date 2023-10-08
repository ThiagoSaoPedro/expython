n = s = cont = 0
while True:
    n = int(input('Digite um número: [999 para parar]'))
    cont += 1
    if n == 999:
        break
    s += n
print(f'foram digitados {cont} e a soma vale {s}')