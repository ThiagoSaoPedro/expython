def teste():
    print(f'Na função teste, n vale {n}')
    x = 8 # escopo local
    print(f'Na função teste, x vale {x}')

#programa principal
n = 2 # escopo global
print(f'No programa principal n vale {n}')
