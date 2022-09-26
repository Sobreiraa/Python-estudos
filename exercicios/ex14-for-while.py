#Faça um programa que escreva na tela, de 1 até 100 pulando de 1 em 1, 2 vezes. A primeira vez deve usar a estrutura de repetição for e a segunda while.

#Usando o laço FOR:
import time

for n in range(1,101):
    print(n)
    time.sleep(0.2)

#Usando o laço WHILE:

contagem = 1

while contagem <= 100:
    print(contagem) 
    contagem += 1
    time.sleep(0.2)

    