'''
POO - Herança Múltipla

Herança múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas clases, fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

A herança múltipla pode ser feita de duas maneiras:
    - Por Multiderivação Direta:
    - Por Multiderivação Indireta:

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EXEMPLO 1 - Multiderivação Direta ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1, Base2, Base3):
    pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EXEMPLO 1 - Multiderivação Indireta ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass

Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará todos os atributos e métodos das supers classes.
'''

class Animal:

    def __init__(self, nome: str) -> None:
        self.__nome = nome
    
    def cumprimentar(self) -> str:
        return f'Eu sou {self.__nome}.'


class Aquatico(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self) -> str:
        return f'{self._Animal__nome} está nadando.'   
    
    def cumprimentar(self) -> str:
        return f'Eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def andar(self) -> str:
        return f'{self._Animal__nome} está andando.'
    
    def cumprimentar(self) -> str:
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguim(Terrestre, Aquatico): # Ordem importa muito, dando prioridade ao primeiro herdado (Method Resolution Order)

    def __init__(self, nome):
        super().__init__(nome)


# TESTANDO

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

print('-' * 70)

leao = Terrestre('Alex')
print(leao.andar())
print(leao.cumprimentar())

print('-' * 70)

pinguim = Pinguim('Tux')
print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimentar())

print('-' * 70)

help(Pinguim)