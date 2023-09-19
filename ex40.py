n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2

if 0 <= media < 5:
    print(f'Sua média foi {media} e você foi reprovado!')
elif 5 <= media < 7:
    print(f'Sua média foi {media} e você está em recuperação!')
elif 7 <= media <= 10:
    print(f'Sua média foi {media} e você está aprovado!')
else:
    print('Você digitou valores inválidos')