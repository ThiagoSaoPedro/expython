dados = {'nome':'Pedro', 'idade':25} #ou dados = dict()
print(dados['nome'])
dados['sexo'] = 'M'
del dados['idade']



filme = {
    'titulo':'Star Wars',
    'ano':1997,
    'diretor':'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}')