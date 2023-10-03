primeiro_termo = float(input("Digite o primeiro termo da progressão aritmética: "))
razao = float(input("Digite a razão da progressão aritmética: "))
cont = -1
progressao_aritmetica = []

while cont < 10:
    cont += 1
    termo = primeiro_termo + cont * razao
    progressao_aritmetica.append(termo)

print("Os primeiros 10 termos da progressão aritmética são:")
for termo in progressao_aritmetica:
    print(termo)

mais = 1
while mais > 0:
    mais = int(input('Quantos termos você quer mostrar a mais?'))
    
    if mais > 0:
        for _ in range(mais):
            cont += 1
            termo = primeiro_termo + cont * razao
            progressao_aritmetica.append(termo)
        
        print(f'Os próximos {mais} termos são:')
        for termo in progressao_aritmetica[-mais:]:
            print(termo)
