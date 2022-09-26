#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maior_idade = 0
menor_idade = 0

for n in range(1,8):
    ano_atual = 2022
    nascimento = int(input(f'Digite o ano de nascimento da {n}° pessoa: '))

    if ano_atual - nascimento <= 18:
      menor_idade += 1
    else:
        maior_idade += 1

print(f'Ao todo tivemos {maior_idade} pessoas maiores de idade e {menor_idade} menores de idade.')
