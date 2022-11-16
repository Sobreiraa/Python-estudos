'''
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

Quando subescrevemos um método presentan a classe pai em classes filhas estamos realizando uma sobrescrita de método (Overriding).

O Overriding é a melhor representação do polimorfismo.

'''

class Animal(object):

    def __init__(self, nome: str) -> None:
        self.__nome = nome
    
    def falar(self) -> str:
        raise NotImplementedError('A classe filha precisa implementar este método.')
    
    def comer(self) -> str:
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome: str) -> None:
        super().__init__(nome)
    
    def falar(self) -> str:
        print(f'{self._Animal__nome} fala au au...')


class Gato(Animal):

    def __init__(self, nome: str) -> None:
        super().__init__(nome)
    
    def falar(self) -> str:
       print(f'{self._Animal__nome} fala miau...')


class Rato(Animal):

    def __init__(self, nome: str) -> None:
        super().__init__(nome)


# TESTANDO

felix = Gato('Felix')
felix.comer()
felix.falar()

print('-' * 70)

duque = Cachorro('Duque')
duque.comer()
duque.falar()

print('-' * 70)

mickey = Rato('Rato')
mickey.comer()
mickey.falar()