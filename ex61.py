primeiro_termo = float(input("Digite o primeiro termo da progressão aritmética: "))
razao = float(input("Digite a razão da progressão aritmética: "))
cont = 0
progressao_aritmetica = []
while cont <9:
    termo = primeiro_termo + cont * razao 
    progressao_aritmetica.append(termo)
    cont += 1
    
print("Os primeiros 10 termos da progressão aritmética são:")
for termo in progressao_aritmetica:
    print(termo)
