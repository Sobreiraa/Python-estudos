#Faça um programa que leia números inteiros no intervalo[0,50] e os armazene em uma lista com 10 posições. Preencha uma segunda lista apenas com os números ímpares da primeira lista. Imprima as duas listas.

lista_numeros = []
lista_impares = []

for numero in range(1,11):
    lista_numeros.append(int(input(f'Digite o {numero}° número da lista: ')))

for numero in lista_numeros:
    if numero % 2 == 1:
        lista_impares.append(numero)

print(f'Lista de números: {lista_numeros}')
print(f'Lista de números ímpares: {lista_impares}')