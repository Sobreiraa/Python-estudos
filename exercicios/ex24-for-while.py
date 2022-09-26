#Faça um programa que leia vários números inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor número lido.

lista_numeros = []

while True:
    numero_usuario = int(input('Digite um número: ')) 
    lista_numeros.append(numero_usuario)

    if numero_usuario < 0:
        break

print(lista_numeros)
print(f'O maior número digitado foi: {max(lista_numeros)}')
print(f'O menor número digitado foi: {min(lista_numeros)}')