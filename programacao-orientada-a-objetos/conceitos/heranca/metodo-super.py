'''
POO - O método super()

O método super() se refere a super classe.

'''

class Animal:

    def __init__(self, nome: str, especie: str) -> None:
        self.__nome = nome
        self.__especie = especie
    
    def faz_som(self, som) -> str:
        print(f'O {self.__nome} faz {som}.')


class Gato(Animal):

    def __init__(self, nome: str, especie: str, raca: str) -> None:
        # Animal.__init__(self, nome, especie) - Não recomendado
        super().__init__(nome, especie) # Recomendado
        self.__raca = raca


# TESTANDO

gato = Gato('Duque', 'Felino', 'Angorá')
gato.faz_som('miau')