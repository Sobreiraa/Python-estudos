# Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e altura. Crie os métodos públicos necessário para sets e gets e também um método para imprimir os dados de uma pessoa.

class Pessoa:

    def __init__(self, nome: str, idade: int, altura: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ GETTERS E SETTERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    @property
    def get_nome(self) -> str:
        return self.__nome
    
    @get_nome.setter
    def set_nome(self, valor) -> None:
        self.__nome = valor.title().strip()
    
    @property
    def get_idade(self):
        return self.__idade
    
    @get_idade.setter
    def set_idade(self, valor) -> None:
        self.__idade = valor
    
    @property
    def get_altura(self) -> float:
        return self.__altura 
    
    @get_altura.setter
    def set_altura(self, valor) -> None:
        self.__altura = valor

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ MÉTODO PÚBLICO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def mostra_pessoa(self) -> None:
        print(f'{self.__nome} tem {self.__idade} anos e uma altura de {self.__altura:.2f} m.')


# TESTANDO 

pessoa1 = Pessoa('matheus', 21, 1.70)
pessoa1.mostra_pessoa()
pessoa1.set_nome = 'sobreira      '
pessoa1.set_altura = 1.79
pessoa1.set_idade = 22
print(pessoa1.set_nome)
print(pessoa1.get_idade)
print(pessoa1.get_altura)
pessoa1.mostra_pessoa()