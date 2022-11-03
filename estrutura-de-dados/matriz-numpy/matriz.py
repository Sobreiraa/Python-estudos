import numpy as np

matriz = np.array([[2, 5, 7],
                   [1, 8, 9]])

print()
print('Imprimindo matriz completa: ')
print(matriz) # Matriz completa

print()
print('Quantidade de linhas e colunas: ')
print(matriz.shape) # Linhas e Colunas

print()
print('Primeira e segunda linha: ')
print(matriz[0]) # Primeira linha
print(matriz[1]) # Segunda linha

print()
print('Linha e coluna especifíca: ')
print(matriz[0][0]) # 2
print(matriz[1][1]) # 8

print()
print('Imprimindo as linhas da coluna e os elementos individuais da coluna ')
for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i][j])