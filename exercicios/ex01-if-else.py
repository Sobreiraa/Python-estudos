#Faça um programa que receba dois números e mostre qual deles é o maior.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

if numero1 > numero2:
    print(f'O maior número digitado entre os dois foi {numero1}')
elif numero1 < numero2:
    print(f'O maior número digitado entre os dois foi {numero2}')
else:
    print('Os dois números são iguais.')