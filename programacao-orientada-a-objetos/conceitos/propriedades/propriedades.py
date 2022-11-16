'''
POO - Propriedades - Properties

Getters e setters são usados principalmente para manipulação dos atributos.
Getters são para retornar o valor do atributo, e os setters para modificar o valor de algum atributo.

É necessário tomar muito cuidado ao utilizar setters, pois nem sempre queremos modificar o valor de algum atributo privado, como o titular de uma conta, pois o titular nunca muda.

'''

class Conta:

    contador = 0

    def __init__(self, titular: str, saldo: float, limite: float) -> None:
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
    
    # Getters e Setters

    @property
    def get_numero(self) -> int:
        return self.__numero
    
    @property
    def get_titular(self) -> str:
        return self.__titular
    
    @get_titular.setter
    def set_titular(self, titular) -> None:
        self.__titular = titular
    
    @property
    def get_saldo(self) -> float:
        return self.__saldo
    
    @get_saldo.setter
    def set_saldo(self, saldo) -> None:
        self.__saldo = saldo
    
    @property
    def get_limite(self) -> float:
        return self.__limite
    
    @get_limite.setter
    def set_Limite(self, limite) -> None:
        self.__limite = limite
    
    # Métodos

    def extrato(self) -> str:
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor) -> None:
        self.__saldo += valor
    
    def sacar(self, valor) -> None:
        self.__saldo -= valor

    def transferir(self, valor, destino) -> None:
        self.__saldo -= valor
        destino.__saldo += valor

conta1 = Conta('Matheus', 200, 500)
conta2 = Conta('Sobreira', 500, 800)

# TESTANDO

print('-=' * 50)

print(conta1.extrato())
print(conta2.extrato())

print('-=' * 50)

soma = conta1.get_saldo + conta2.get_saldo
print(f'O saldo das duas contas é {soma}')

print('-=' * 50)

conta1.set_Limite = 9999999999
conta2.set_titular = 'matheussssssssssss'

print(conta1.__dict__)
print(conta2.__dict__)
