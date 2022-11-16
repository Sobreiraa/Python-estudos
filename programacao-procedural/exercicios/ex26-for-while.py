#Faça um programa que peça um número para que mostre a sua tabuada com o resultado na tela.

numero_usuario = int(input('Digite um número para ver sua tabuada: '))

for numero in range(1,11):
    print(f'{numero_usuario} x {numero} = {numero_usuario*numero}')