'''Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz
matriz = [3, 4, 1],
         [3, 1, 5]'''


import numpy as np

matriz = np.array([[3, 4, 1],
                  [3, 1, 5]])

soma = 0

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        soma += matriz[i][j]
    
print(f'Soma da matriz: {soma}')

