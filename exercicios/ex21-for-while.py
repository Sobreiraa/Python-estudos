#Faça um programa que leia um número inteiro positivo N e imprima todos os números pares de 0 até N em ordem crescente.

numero_usuario = int(input('Digite um número inteiro: '))

if numero_usuario > 0:
    for numero in range(0, numero_usuario+1, 2):
        print(numero)
else:
    print('Número inválido')