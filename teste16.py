num = [2, 5 , 9 , 1]
num[2] = 3
num.append(7) #adiciona o valor
num.sort() #ordena os valores
num.insert(2, 2) #insere um 2 na posição 2
num.remove(2) #remove os números 2
num.pop(2) #remove o segundo elemento da lista
if 4 in num:
    num.remove(4)
print(num)
print(f'Essa lista tem {len(num)} elementos')