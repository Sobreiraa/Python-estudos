#Escreva um programa uqe leia 10 números e escreva o menor e o maior valor lido.
lista_numeros = []

for n in range(1,11):
    numero = int(input(f'Digite o {n}° número: '))
    lista_numeros.append(numero)
   
print(f'O maior número digitado foi {max(lista_numeros)} e o menor foi {min(lista_numeros)}')