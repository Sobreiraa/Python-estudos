#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

trabalhador = {}

trabalhador['nome'] = str(input('Nome: '))
nascimento = int(input('Nascimento: '))
trabalhador['idade'] = datetime.now().year - nascimento
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))


if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - datetime.now().year)

print('-=' * 25)

for k, v in trabalhador.items():
        print(f'- {k} tem o valor {v}')