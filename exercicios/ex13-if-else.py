#Faça um programa que receba a altura e o peso de uma pessoa e mostre qual a classificação dessa pessoa.

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

if altura < 1.20:
    if peso <= 60:
        print('Classificação A')
    elif peso > 60 and peso <= 90:
        print('Classificação D')
    else:
        print('Classificação G')
elif altura >= 1.20 and altura <= 1.70:
    if peso <= 60:
        print('Classificação B')
    elif peso > 60 and peso <= 90:
        print('Classificação E')
    else:
        print('Classificação H')
else:
    if peso <= 60:
        print('Classificação C')
    elif peso > 60 and peso <= 90:
        print('Classificação F')
    else:
        print('Classificação I')