#Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.


from math import sqrt

while True:
    numero = int(input('Digite um número: '))

    if numero <= 0:
        print('O número digitado tem que ser maior que 0')
        break

    print(f'Quadrado do número {numero} é {numero*numero}.')
    print(f'Cubo do número {numero} é {numero*numero*numero}.')
    print(f'Raiz quadrada do número {numero} é {sqrt(numero):.0f}')