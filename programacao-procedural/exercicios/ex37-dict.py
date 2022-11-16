#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

print('Valores sorteados: ')

jogo = {'jogador_1': randint(1,6),
        'jogador_2': randint(1,6),
        'jogador_3': randint(1,6),
        'jogador_4': randint(1,6)}

ranking = ()
    
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('Ranking: ')

for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(0.5)
