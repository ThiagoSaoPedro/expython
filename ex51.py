
primeiro_termo = float(input("Digite o primeiro termo da progressão aritmética: "))
razao = float(input("Digite a razão da progressão aritmética: "))
progressao_aritmetica = []

for i in range(10):
    termo = primeiro_termo + i * razao
    progressao_aritmetica.append(termo)

print("Os primeiros 10 termos da progressão aritmética são:")
for termo in progressao_aritmetica:
    print(termo)
