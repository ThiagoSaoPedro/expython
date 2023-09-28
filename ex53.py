frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.strip()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(frase, inverso)
if frase == inverso:
    print('Sua frase é um palíndromo')
else:
    print('Sua frase não é um palíndromo') 