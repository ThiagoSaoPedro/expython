vel = int(input('Digite a velocidade do seu carro: '))
if vel > 80:
    multa = str((vel - 80) * 7)
    print('Você foi multado em ' + multa + ',00R$!')
else:
    print('Você está dentro do limite de velocidade, aproveite sua viagem!')