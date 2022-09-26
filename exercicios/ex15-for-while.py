#Faça um algoritmo utilizando o comando while, que mostre uma contagem regressiva na tela, iniciando em 10 e terminando em 0. Mostrar uma menasgem "Fim" após a contagem.

contagem = 10
while True:
    print(contagem)
    contagem -= 1
    if contagem <= 0:
        print(contagem)
        print('FIM')
        break
    