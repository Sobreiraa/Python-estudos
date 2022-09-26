#Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente.

numero_usuario = int(input('Digite um número inteiro: '))

if numero_usuario > 0:
    for numero in range(numero_usuario, -1, -1):
        print(numero)
else:
    print('Número inválido')