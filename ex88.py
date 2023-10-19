import random
n = int(input('Digite a quantidade de jogos que deseja: '))
rnum = 0
jogo = []
for v in range(0, n):
    for j in range(0, 6):
        rnum = random.randint(0, 60)
        jogo.append(rnum)
    print(jogo)
    jogo.clear()


