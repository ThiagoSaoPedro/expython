equipes = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo'
           , 'Fortaleza', 'Fluminense', 'Athletico-PR', 'Atlético-MG'
           , 'São Paulo', 'Cuiabá', 'Internacional', 'Corinthians'
           , 'Santos', 'Cruzeiro', 'Bahia', 'Vasco', 'Goiás'
           , 'Coritiba', 'América-MG')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {equipes}')
print('-=' * 15)
print(f'Os primeiros 5 foram: {equipes[0:5]}')
print('-=' * 15)
print(f'Os ultimos 4 foram: {equipes[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(equipes)}')
print('-=' * 15)
print(f'O Flamengo está na posição {equipes.index("Flamengo") + 1}')