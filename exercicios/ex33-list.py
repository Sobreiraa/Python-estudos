#Faça um programa que leia uma lista de 8 posições e, em seguida, leia também dois valores X e Y quaisquer, correspondentes a duas posições na lista. Ao final, seu programa deverá escrever a soma dos valores encontrados na respectivas posições X e Y.

from operator import index

lista = []

for n in range(1,9):
    lista.append(int(input(f'Digite o {n}° número: ')))

num1 = int(input('Quer saber o número que está em qual posição? (n° entre 1 e 8) '))
num2 = int(input('Quer saber o número que está em qual posição? (n° entre 1 e 8) '))

if num1 < 1 or num1 > 8:
    print('Número inválido.')
elif num2 < 1 or num1 > 8:
    print('Número inválido.')
else:
    soma = index(lista[num1-1]) + index(lista[num2-1]) 
    print(f'A soma dos números na posição {num1} e {num2} é: {soma}')
