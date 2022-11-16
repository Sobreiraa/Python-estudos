'''
POO - Herança (Inheritance)

A ideia de herança é de reaproveitar código e também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente nós extendemos outra classe que passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

OBS: Quando uma classe herda de outra classe, ela herda TODOS os atributos e métodos da classe herdada. Para que funcione a herança, devemos utilizar o construtor da classe Pai.

A classe herdada é conhecida por:
    * [PESSOA] *
    - Super Classe
    - Classe Mãe
    - Classe Pai
    - Classe Base
    - Classe genérica

E quando a classe herda de outra é chamada:
    * [Cliente, Funcionário] *
    - Sub Classe
    - Classe Filha
    - Classe Específica

Sobrescrita demétodo ocorre quando reescrevemos um método presente na super classe em classes filhas.
'''

class Pessoa:

    def __init__(self, nome: str, sobrenome: str, cpf: int) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def mostra_dados(self) -> str:
        return f'Nome: {self.__nome} {self.__sobrenome}, CPF: {self.__cpf}'


class Cliente(Pessoa):
    '''Cliente herda de Pessoa'''
    def __init__(self, nome: str, sobrenome: str, cpf: int, renda: float) -> None:
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda    

class Funcionario(Pessoa):
    '''Funcionário herda de Pessoa'''
    def __init__(self, nome: str, sobrenome: str, cpf: int,  matricula: int) -> None:
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula
    
    ''' 01° FORMA
    def mostra_dados(self) -> str:
        return super().mostra_dados(), f'Matrícula: {self.__matricula}'
    '''
    
    # 02° FORMA
    def mostra_dados(self) -> str:
        return f'Nome: {self._Pessoa__nome}, Matrícula {self.__matricula} '
        

# TESTANDO

cliente1 = Cliente('Matheus', 'Sobreira', 70372990144, 1500)
funcionario1 = Funcionario('Lucas', 'Gagliasso', 95578890155, 1234)

print(cliente1.mostra_dados())
print(funcionario1.mostra_dados())

'''
print(cliente1.__dict__)
print(funcionario1.__dict__)
'''