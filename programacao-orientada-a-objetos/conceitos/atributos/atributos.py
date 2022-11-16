'''
Atributos -> Representam as características do objeto, ou seja, pelos atributos nós conseguimos representar computacionalmente os estados de um objeto.

Em python, dividimos os atributos em 3 grupos:
    - Atributos de Instância: Criado no método construtor
    - Atributos de Classe: Criado na classe, pode ser utilizado por todos os métodos
    - Atributos Dinâmicos: Atributo que pode ser criado em tempo de execução
'''

# Classes com Atributo de Instância Publicos

class ContaCorrente:

    #Atributo de classe
    variacao = 51
    contador = 0

    # Atributo de instância
    def __init__(self, limite, saldo):
        self.id = ContaCorrente.contador + 1
        self.limite = limite
        self.saldo = saldo
        ContaCorrente.contador = self.id

# Classes com Atributo de Instância Privados
class Acesso:
    
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha #Atributo privado

    def mostra_senha(self):
        print(self.__senha)

conta1 = ContaCorrente(100, 500)
conta2 = ContaCorrente(200, 100)

# Atributos Dinâmicos

conta1.nome = 'Matheus'

print(conta1.nome) # Não é comum de se utilizar.
'''print(conta2.nome) # AttributeError pois não criou um atributo dinâmico'''

print(conta1.__dict__)
print(conta2.__dict__)

del conta1.nome
print(conta1.__dict__)


