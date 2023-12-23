dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
dados['sexo'] = 'M'
del dados['idade']



filme = {
    'titulo':'Star Wars',
    'ano':1997,
    'diretor':'George Lucas'
}
print(filme.values()) # mostra somente os resultados
print(filme.keys()) # mostra somente as chaves
print(filme.items()) # mostra todos os itens dentro do dicionário

for k,v in filme.items():
    print(f'O {k} é {v}')