def area(largura, comprimento):
    tamanho = largura * comprimento
    print(f'A área de um terreno {largura:1f} x {comprimento:1f} é de {tamanho:2f}')


print('   CONTROLE DE TERRENOS   ')
print(25 * '-')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m):'))
area(largura, comprimento)