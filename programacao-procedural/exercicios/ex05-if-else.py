#Faça um programa que receba a altura e o sexto de uma pessoa. Calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde H corresponde à altura):
# *Homens (72.7 * h) - 58
# *Mulheres (62.1 * h) - 44,7

altura = float(input('Digite sua altura: '))
sexo = str(input('Qual seu sexo? [M]/[F] ')).strip().upper()

peso_ideal = 0
print(sexo[0])

if sexo[0] == 'M': 
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é {peso_ideal:.2f} Kg')
elif sexo[0] == 'F': 
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é {peso_ideal:.2f} Kg')
else:
    print('Você digitou um sexo inválido.')