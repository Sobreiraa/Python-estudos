#Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas. O usuário escolhe uma das opções e o seu programa pede então dois valores númericos e realiza a operação mostrando o resultado.

operacao = int(input('''Qual operação gostaria de realizar? 
[1] - Soma 
[2] - Subtração
[3] - Multiplicação
[4] - Divisão '''))

numero1 = 0
numero2 = 0
resultado = 0

if operacao > 0 and operacao <= 4:
    if operacao == 1:
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))
        resultado = numero1 + numero2
        print('Somando...')
        print(resultado)
    elif operacao == 2:
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))
        resultado = numero1 - numero2
        print('Subtraindo...')
        print(resultado)
    elif operacao == 3:
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))
        resultado = numero1 * numero2
        print('Multiplicando...')
        print(resultado)
    else:
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))
        resultado = numero1 / numero2
        print('Dividindo...')
        print(f'{resultado:.0f}')
else:
    print('Número inválido.')