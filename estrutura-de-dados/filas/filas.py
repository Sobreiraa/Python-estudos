import numpy as np

class FilaCircular:

    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numeros_elementos = 0
        self.vetor = np.empty(self.capacidade, dtype = int)
    

    def __fila_vazia(self) -> bool:
        return self.numeros_elementos == 0
    

    def __fila_cheia(self) -> bool:
        return self.numeros_elementos == self.capacidade


    def enfileirar(self, valor) -> None:
        if isinstance(valor, int):
            if self.__fila_cheia():
                print('A fila está cheia.')
                return
            
            if self.final == self.capacidade - 1:
                self.final = -1
            self.final += 1
            self.vetor[self.final] = valor
            self.numeros_elementos += 1
        
    
    def desenfileirar(self) -> int:
        if self.__fila_vazia():
            print('A fila já está vazia.')
            return
        
        temp = self.vetor[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.numeros_elementos -= 1
        return temp


    def primeiro(self) -> None:
        if self.__fila_vazia():
            print('-1')
        else:
            print(f'{self.vetor[self.inicio]}')


# Testes

fila = FilaCircular(5)

fila.primeiro()

# 9 3 4 8 2
fila.enfileirar(2)
fila.enfileirar(8)
fila.enfileirar(4)
fila.enfileirar(3)
fila.enfileirar(9)
fila.enfileirar(5)

fila.primeiro()

fila.desenfileirar()
fila.desenfileirar()

fila.primeiro()

fila.enfileirar(6)
fila.enfileirar(7)

fila.primeiro()