import random


def sorteia():
    n = 0
    while n < 5:
        lista.append(random.randint(1, 10))
        n += 1
    print(lista)


def somar(num):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(soma)


lista = []
sorteia()
somar(lista)