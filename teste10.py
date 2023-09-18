nome = str(input('Qual seu nome?'))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Que nome comum!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Um nome feminino...')
else:
    print('Seu nome é relativamente normal')
print('tenha um bom dia {}!'.format(nome))