# Escreva um código que apresenta a classe Pessoa, com atributos nome, edenreço e telefone, e também o método imprimir. O método imprimir deve mostrar na tela os valores de todos os atributos.

class Pessoa:

    def __init__(self, nome: str, endereco: str, telefone: int) -> None:
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ GETTERS E SETTERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @property
    def get_nome(self) -> str:
        return self.__nome
    
    @get_nome.setter
    def set_nome(self, valor) -> None:
        self.__nome = valor
    
    @property
    def get_endereco(self) -> str:
        return self.__endereco
    
    @get_endereco.setter
    def set_endereco(self, valor) -> None:
        self.__endereco = valor
    
    @property
    def get_telefone(self) -> int:
        return self.__telefone
    
    @get_telefone.setter
    def set_telefone(self, valor) -> None:
        self.__telefone = valor
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MÉTODOS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def imprimir(self) -> str:
        print(f'Nome: {self.__nome}')
        print(f'Endereço: {self.__endereco}')
        print(f'Telefone: {self.__telefone}')
    
    def __str__(self) -> str:
        print(f'{self.__nome}, {self.__endereco}, {self.__telefone}')


# TESTANDO

pessoa1 = Pessoa('Matheus', 'Rua 78 qd 39 lt 15 - Jundiai', 62992375566)
pessoa1.imprimir()

print(pessoa1.get_nome)
print(pessoa1.get_endereco)
print(pessoa1.get_telefone)

pessoa1.set_nome = 'MATHEUS'
pessoa1.set_endereco = 'RUA 38 QD 44 LOTE 120'
pessoa1.set_telefone = '40028922'

pessoa1.imprimir()

pessoa1.__str__()
