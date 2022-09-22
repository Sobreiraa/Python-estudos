import random

def jogo_adivinhacao():

    print('-' * 35)
    print('Bem vindo ao jogo de Adivinhação.')
    print('-' * 35)

    numero_secreto = random.randint(1,101)
    total_de_tentativas = 0
    pontos = 0

    print('''Dificuldades:
    [1] - Fácil (20 Tentativas e 2000 pontos)
    [2] - Médio (10 Tentativas e 1000 pontos)
    [3] - Difícil (5 Tentativas e 500 pontos)''')

    nivel_dificuldade = int(input('Qual nível de dificuldade você deseja? '))

    if nivel_dificuldade == 1:
        total_de_tentativas = 20
        pontos = 2000
    elif nivel_dificuldade == 2:
        total_de_tentativas = 10
        pontos = 1000
    elif nivel_dificuldade == 3:
        total_de_tentativas = 5
        pontos = 500
    else:
        print('Você chutou um número menor que 1 e maior que 3, tera apenas 1 tentativa.')
        total_de_tentativas = 1
        pontos = 2000
        
    for rodada in range(1, total_de_tentativas+1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute_usuario = int(input('Chute um número entre 1 e 100: '))
        print('Voce digitou', chute_usuario)

        if chute_usuario < 1 or chute_usuario > 100:
            print('Você deve digitar um número entre 1 e 100')
            continue

        acerto = numero_secreto == chute_usuario
        maior = chute_usuario > numero_secreto
        menor = chute_usuario < numero_secreto

        if acerto:
            print(f'Parabéns, você acertou e fez {pontos} pontos.')
            break
        else:
            if maior:
                print('Não foi dessa vez, você chutou um número maior do que o número secreto.')
            elif menor:
                print('Não foi dessa vez, você chutou um número menor do que o número secreto.')
            pontos_perdidos = abs(numero_secreto - chute_usuario)
            pontos -= pontos_perdidos  

        print()

if __name__ == "__main__":
    jogo_adivinhacao()
