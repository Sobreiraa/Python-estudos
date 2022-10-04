#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Digite seu nome: '))
aluno['media'] = float(input('Qual sua média? '))

if aluno['media'] > 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=' * 25)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')