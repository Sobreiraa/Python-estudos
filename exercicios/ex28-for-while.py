#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

import random

print('-' * 25)
print('Vamos jogar PAR ou ÍMPAR')
print('-' * 25)

soma = 0
vitorias = 0

while True:
    numero_usuario = int(input('Digite um número: '))
    numero_computador = random.randint(1,50)
    soma = numero_usuario + numero_computador
    par_impar = str(input('Par ou Ímpar? [P/I] ')).upper()

    print('-' * 25)
    if soma % 2 == 0:
        print(f'Você jogou {numero_usuario} e o computador {numero_computador}. Total deu {soma} PAR')
        if par_impar == 'P':
            print('Parabéns, você venceu!')
            vitorias += 1
        else:
            print(f'Game Over. Você venceu {vitorias} vezes.')
            break
    else:
        print(f'Você jogou {numero_usuario} e o computador {numero_computador}. Total deu {soma} ÍMPAR')
        if par_impar[0] == 'I':
            print('Parabéns, você venceu!')
            vitorias += 1
        else:
            print(f'Game Over. Você venceu {vitorias} vezes.')
            break