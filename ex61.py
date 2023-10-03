primeiro_termo = float(input("Digite o primeiro termo da progressão aritmética: "))
razao = float(input("Digite a razão da progressão aritmética: "))
cont = 1
progressao_aritmetica = []
while cont <10:
    cont += 1
    termo = primeiro_termo + cont * razao   
    progressao_aritmetica.append(termo)
    
print("Os primeiros 10 termos da progressão aritmética são:")
for termo in progressao_aritmetica:
    print(termo)
