#Faça um programa que receba dois números e mostre qual deles é o maior, assim como a diferença existente entre ambos.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
diferenca = numero1 - numero2

if numero1 > numero2:
    print(f'O maior número digitado entre os dois foi {numero1}')
    print(f'A diferença entre {numero1} e {numero2} é {diferenca}')
elif numero1 < numero2:
    print(f'O maior número digitado entre os dois foi {numero2}')
    print(f'A diferença entre {numero1} e {numero2} é {diferenca}')
else:
    print('Os dois números são iguais.')