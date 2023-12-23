def leia(msg):
    while True:
        valor = input(msg).replace(',', '.')
        if valor.replace('.', '').isdigit():
            return float(valor)
        else:
            print('Valor inválido. Tente novamente.')