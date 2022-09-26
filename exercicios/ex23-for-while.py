#Faça um programa que simule o lançamento de dois dados, d1 e d2 N vezes, e tem como saída o número de cada dado e a relação entre eles (>, <, =) de cada lançamento.

import random

contagem = 0

quantidade_simulacao = int(input('Digite a quantidade para simulação: '))

while contagem <= quantidade_simulacao:

    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)

    print(dado1, dado2)

    if dado1 > dado2:
        print('Dado 1 é maior.')
    elif dado2 > dado1:
        print('Dado 2 é maior.')
    else:
        print('Os dois dados são iguais.')

    contagem += 1
