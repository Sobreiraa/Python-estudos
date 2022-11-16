#Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda se 2 e assim por diante

numero = int(input('Digite um número inteiro entre 1 e 7: '))

if numero > 0 and numero <=7:
    if numero == 1:
        print('Hoje é domingo.')
    elif numero == 2:
        print('Hoje é segunda-feira.')
    elif numero == 3:
        print('Hoje é terça-feira.')
    elif numero == 4:
        print('Hoje é quarta-feira.')
    elif numero == 5:
        print('Hoje é quinta-feira.')
    elif numero == 6:
        print('Hoje é sexta-feira.')
    else:
        print('Hoje é sábado.')
else:
    print('Número inválido.')
    