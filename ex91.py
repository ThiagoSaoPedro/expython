import random
from time import sleep
from operator import itemgetter
jogo = {
    'Jogador 1': random.randint(1,6),
    'Jogador 2': random.randint(1,6),
    'Jogador 3': random.randint(1,6),
    'Jogador 4': random.randint(1,6),
}
ranking = []
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) 
print(40 * '-')
for k, v in enumerate(ranking):
    print(f'{k+1} lugar: {v[0]} com {v[1]}')
    sleep(1)