import numpy as np

class Pilha:
    
    def __init__(self, capacidade) -> None:
        self.__capacidade = capacidade
        self.__topo = -1
        self.__vetor = np.empty(self.__capacidade, dtype=int)
    

    def __pilha_cheia(self) -> bool:
        if self.__topo == self.__capacidade - 1:
            return True
        else:
            return False


    def __pilha_vazia(self) -> bool:
        if self.__topo == -1:
            return True
        else:
            return False
    

    def empilhar(self, valor) -> None:
        if isinstance(valor, int):
            if self.__pilha_cheia():
                print('A pilha está cheia.')
            else:
                self.__topo += 1
                self.__vetor[self.__topo] = valor
        else:
            print('É necessário um valor númerico do tipo int.')
    

    def desempilhar(self) -> None:
        if self.__pilha_vazia():
            print('A pilha está vazia.')
        else:
            self.__topo -= 1
    

    def ver_topo(self) -> None:
        if self.__topo != -1:
            print(self.__vetor[self.__topo])
        else:
            print('-1')



# Testes

pilha = Pilha(5)

pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)
pilha.empilhar(6)

pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()

pilha.ver_topo()
