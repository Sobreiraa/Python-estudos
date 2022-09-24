#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são:
# *Ter pelo menos 65 anos;
# *Ter trabalhado pelo menos 30 anos;
# *Ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input('Qual sua idade: '))
tempo_trabalho = int(input('Digite quanto tempo trabalhou: '))

if idade > tempo_trabalho:
    print('Avaliando aposentadoria...')
    if idade >= 65:
        print('Aposentadoria aprovada.')
    elif tempo_trabalho >= 30:
        print('Aposentadoria aprovada.')
    elif idade >= 60 and tempo_trabalho >= 25:
        print('Aposentadoria aprovada.')
    else:
        print('Não pode se aposentar no momento.')
else:
    print('Números inválidos')