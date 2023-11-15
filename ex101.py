import datetime

def voto(ano):
    idade = datetime.datetime.now().year - ano
    if idade >= 18:
        return 'Voto Obrigatório'
    elif 16 <= idade < 18:
        return 'Voto Opcional'
    else:
        return 'Você não pode votar'

n = voto(2012)
print(n)
c = voto(2007)
print(c)
m = voto(2005)
print(m)