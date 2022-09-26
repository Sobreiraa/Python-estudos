#Faça um programa que calcule e mostre a soma dos 50 primeiros números pares

soma = 0

for numero in range(0, 101, 2):
    print(numero)
    soma += numero

print(soma)
