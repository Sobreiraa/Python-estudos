#Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação:

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.6 and imc <= 24.9:
    print('Você está saudável.')
elif imc >= 25 and imc <= 29.9:
    print('Peso em excesso')
elif imc >= 30 and imc <= 34.9:
    print('Obesidade Grau I')
elif imc >= 35.0 and imc <= 39.9:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III')