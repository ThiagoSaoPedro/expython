import random
rnum = random.randint(0, 5)
num = int(input('Digite um número de 0 a 5 '))
if num == rnum:
    print('Meus parabéns, o número é {}, você acertou!!!'.format(rnum))
else:
    print('Você errou ou enviou um número inválido. Boa sorte na próxima!!!')