#def soma(a, b):
#    s = a + b
#    print(s)
#
#soma(4,5)
#soma(5,9)

def contador(*num):
    print(num)
    for valor in num:
        print(valor)
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)