import random
cont = 0
rnum = random.randint(0, 10)
num = int(input('Digite um número de 0 a 10 '))
while rnum != num:
    num = int(input('Digite um número de 0 a 10 '))
    cont += 1
print(f'Você acertou! Foram {cont} tentativas')
