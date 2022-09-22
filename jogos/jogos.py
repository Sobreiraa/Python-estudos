import adivinhacao
import forca

def escolhe_jogo():
    print('-' * 27)
    print('Escolha o jogo que deseja')
    print('-' * 27)

    print('''Escolha o jogo que deseja
    [1] - Adivinhação
    [2] - Forca''')

    jogo = int(input('Qual jogo deseja? '))

    if jogo == 1:
        print('Adivinhação')
        adivinhacao.jogo_adivinhacao()
    elif jogo == 2:
        print('Forca')
        forca.jogo_forca()
    else:
        while jogo <= 0 or jogo > 2:
            print('''Escolha o jogo que deseja
    [1] - Adivinhação
    [2] - Forca''')
            jogo = int(input('Qual jogo deseja? '))
            if jogo == 1:
                print('Adivinhação')
                adivinhacao.jogo_adivinhacao()
            elif jogo == 2:
                print('Forca')
                forca.jogo_forca()

if __name__=="__main__":
    escolhe_jogo()