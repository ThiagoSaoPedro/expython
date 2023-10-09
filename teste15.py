lanche = ('Hamburguer', 'Pizza', 'Suco', 'Pudim')
for comida in lanche:
    print(f'{comida}')


for cont in range(0, len(lanche)):
    print(lanche[cont])
    print(cont)
    print(sorted(lanche))


a = (5, 4 ,9)
b = (7, 8, 5 , 4, 3, 2 ,1 )
c = a + b
print(c)
print(c.count(4))
print(c.index(5, 1))
