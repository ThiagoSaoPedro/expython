nome = str(input('Digite seu nome completo '))
separado = nome.split()
print('Muito prazer em te connhecer!')
print('Seu primeiro nome é {}'.format(separado[0]))
print('Seu ultimo nome é {}'.format(separado[len(separado)-1]))