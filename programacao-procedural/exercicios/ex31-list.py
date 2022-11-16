#Faça um programa que possua uma lista denominado A que armazene 6 números inteiros. O programa deve executar os seguintes passos:
# Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5 e 7.
# Armazene em uma variável inteira simples, a soma entre os valores das posições A[A], A[1] e A[5] da lista e mostre na tela esta soma.
# Modifique a lista na posição 4, atribuindo a esta posição o valor 100
# Mostre na tela cada valor da lista A, um em cada linha

lista_A = [1, 0, 5, -2, -5, 7]
print(f'Lista de números: {lista_A}')
soma_lista = lista_A[0] + lista_A[1] + lista_A[5]
print(f'Soma das posições solicitadas: {soma_lista}')
lista_A[4] = 100
print(f'Lista de números atualizada: {lista_A}')

for numero in lista_A:
    print(f'{numero}', end='\n')

