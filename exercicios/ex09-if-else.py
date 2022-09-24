#Uma empresa vendo o mesmo produto para quatro estados diferentes. Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15% e MS 8%). Faça um programa em que o usuário entre com o valor e o estado de destino do produto. O programa deve retornar o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.

valor = int(input('Digite o valor do produto: R$ '))
estado = str(input('Digite o estado em que o produto será levado: ')).upper()

imposto = 0
valor_imposto = 0
preco_final = 0

if estado == 'MG':
    imposto = 7
    valor_imposto = (valor * imposto) / 100
    preco_final = valor + valor_imposto
    print(f'Valor final a ser pago é de R$ {preco_final:.2f}')
elif estado == 'SP':
    imposto = 12
    valor_imposto = (valor * imposto) / 100
    preco_final = valor + valor_imposto
    print(f'Valor final a ser pago é de R$ {preco_final:.2f}')
elif estado == 'RJ':
    imposto = 15
    valor_imposto = (valor * imposto) / 100
    preco_final = valor + valor_imposto
    print(f'Valor final a ser pago é de R$ {preco_final:.2f}')
elif estado == 'MS':
    imposto = 8
    valor_imposto = (valor * imposto) / 100
    preco_final = valor + valor_imposto
    print(f'Valor final a ser pago é de R$ {preco_final:.2f}')
else:
    print('Estado inválido')
