#Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médidas de acordo com um valor número digitado pelo usuário:
# a) Ponderada: x + 2 * y + 3 * z / 6
# b) Harmônica: 1 / (1 / x) + (1 / y) + (1 / z) 
# c) Aritmética: x + y + z / 3

x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
z = int(input('Digite o valor de z: '))

medida = int(input('''Qual medida deseja calcular? 
[1] - Ponderada
[2] - Harmônica
[3] - Aritmética '''))

resultado = 0

if x > 0 and y > 0 and z > 0:
    if medida == 1:
        resultado = x + 2 * y + 3 * z / 6
        print(f'Resultado do cálculo da medida ponderada é {resultado:.2f}')
    elif medida == 2:
        resultado = 1 / (1 / x) + (1 / y) + (1 / z) 
        print(f'Resultado do cálculo da medida harmônica é {resultado:.2f}')
    elif medida == 3:
        resultado = (x + y + z) / 3
        print(f'Resultado do cálculo da medida aritmética é {resultado:.2f}')
    else:
        print('Medida inválida')
else:
    print('Números inválidos')

