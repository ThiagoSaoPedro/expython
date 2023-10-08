homem = mulherjovem = adulto = 0
print(30 * '=-')
print('CADASTRANDO PESSOAS!!!')
print(30 * '=-')
while True:
    i = int(input('Digite a idade dessa pessoa: '))
    s = str(input('Digite o sexo dessa pessoa [F\M]: ')).upper().strip()
    if i >= 18:
        adulto += 1
    if s == 'M':
        homem += 1
    if s == 'F' and i < 20:
        mulherjovem += 1
    opcao = str(input('Se deseja cadastrar mais uma pessoa digite [S]')).upper()
    if opcao != 'S':
        print(f'Foram cadastradas {adulto} pessoa(s) com mais de 18 anos')
        print(f'Foram cadastrado(s) {homem} homem(s)')
        print(f'Foram cadastrada(s) {mulherjovem} mulhere(s) com menos de 20 anos')
        break

    