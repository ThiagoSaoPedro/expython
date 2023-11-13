def contador(i=0, f=0, p=0):
    c = 1
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim!')


contador(0,100,1)
