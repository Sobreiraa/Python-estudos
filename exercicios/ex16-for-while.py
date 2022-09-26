#Faça um programa que peça ao usuário para digitar 10 valores e some-os.

numero = 0
soma = 0
for n in range(1,11):
    numero = int(input(f'Digite o {n}° número '))
    soma += numero

print(f'A soma dos números digitados é {soma}')
