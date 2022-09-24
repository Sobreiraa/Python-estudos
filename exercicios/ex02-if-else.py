#Leia um número fornecido pelo usuário e verifique se este número é par ou ímpar.

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'Número {numero} é par.')
else:
    print(f'Número {numero} é ímpar.')
