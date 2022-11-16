'''
POO - Abstração e Encapsulamento

 O grande objetivo da POOO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados de usuário.
 
'''

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
    
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}.')
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo.')
    
    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente.')
        else:
            print('O valor precisa ser positivo.')
    
    def transferir(self, valor, conta_destino):
        self.__saldo -= valor

        conta_destino.__saldo += valor

conta1 = Conta('Matheus', 500, 250)
conta1._Conta__titular = 'Lucas' # Mesmo os atributos privados conseguimos modificar o valor // PROIBIDO

conta2 = Conta('Maria', 800, 350)

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()