#Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: "Empréstimo não concedido.", caso contrário imprima: "Empréstimo concedido."

print('Bem vindo ao Banco Inter')
nome = str(input('Digite seu nome: '))
salario = int(input('Digite seu salário: '))
prestacao = int(input('Qual valor da prestação: '))

porcentagem_salario = (salario * 20) / 100

if porcentagem_salario >= prestacao:
    print(f'{nome} seu empréstimo não foi concedido.')
else:
    print(f'{nome} seu empréstimo foi concedido.')
