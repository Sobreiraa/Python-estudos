#Fala um programa que leia um conjunto de números reais, armazenando em uma lista. Calcule o quadrado dos componentes desta lista, armazenando o resultado em outra lista. Os conjuntos têm 10 elementos cada, imprima todos os conjuntos.

lista_numeros = []
lista_quadrado = []

for numeros in range(1,11):
    lista_numeros.append(int(input(f'Digite o {numeros}° número: ')))
    quadrado = numeros * numeros
    lista_quadrado.append(quadrado)

print('-' * 75)
print(f'Lista de números: {lista_numeros}')
print('-' * 75)
print(f'Lista de números ao quadrado: {lista_quadrado}')