#Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100. Escolhe números aleatórios entre 1 e 100, e mostre na tela a pergunta: 'Qual é a soma de a + b?', onde a e b são números aleatórios. Peça a resposta. Faça 5 perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas, além de quantas vezes o aluno acertou.

import random

acerto = 0

for i in range(1,6):

    numero1 = random.randint(1,101)
    numero2 = random.randint(1,101)
    resultado_final = numero1 + numero2

    resultado_usuario = int(input(f'Qual é a soma de {numero1} + {numero2}? '))
    print(f'Resultado: {resultado_final}')

    if resultado_usuario == resultado_final:
        acerto += 1
        print('Parabéns, você acertou.')
    else:
        print('Infelizmente você errou.')
    
print(f'Você acertou {acerto} de 5')
    



