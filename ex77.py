palavras = ('Lavagem', 'Secagem', 'Ouvido', 'coraçao')
for p in palavras:
    print(f'\n Na palavra {p.upper()} temos, ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
print('\n')