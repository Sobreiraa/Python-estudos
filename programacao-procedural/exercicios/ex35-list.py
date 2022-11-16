#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista_comleta = []
lista_pares = []
lista_impares = []

while True:
    lista_comleta.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar != 'S':
        break
    
for numero in lista_comleta:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print('-' * 50)
print(f'Lista completa: {lista_comleta}')
print('-' * 50)
print(f'Lista de pares: {lista_pares}')
print('-' * 50)
print(f'Lista impares: {lista_impares}')


    