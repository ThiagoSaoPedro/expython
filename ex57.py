sexo = str(input('Digite seu sexo: [F/M]').upper())
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite seu sexo: [F/M]').upper())
if sexo == 'M':
    print('Você é do sexo masculino.')
else:
    print('Você é do sexo feminino.')