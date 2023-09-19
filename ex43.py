peso = float(input('Digite seu peso atual: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print(f'Seu IMC é: {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está em sobrepeso!')
elif 30 <= imc < 40:
    print('Você está obeso!')
elif imc >= 40:
    print('Voce está em obesidade mórbida')
else:
    print('Dados inválidos!')