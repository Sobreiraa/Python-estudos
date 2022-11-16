#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Flamengo', 'Corinthians', 'Athletico PR', 'Atlético MG', 'Bragantino', 'Goiás', 'América MG', 'São Paulo', 'Botafogo', 'Santos', 'Fortaleza', 'Ceará', 'Coritiba', 'Cuiabá', 'Avaí', 'Atlético GO', 'Juventude')

print(f'Lista de times do brasileirão: {times}.')
print('-' * 110)
print(f'Os cinco primeiros são: {times[:5]}.')
print('-' * 110)
print(f'Os 4 últimos são: {times[16:]}.')
print('-' * 110)
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O inter está na {times.index("Internacional")+1}° posição.')