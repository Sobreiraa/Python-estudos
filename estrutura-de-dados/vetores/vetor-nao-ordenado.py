import numpy as np

class VetorNaoOrdenado:

    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade # Capacidade máxima do vetor.
        self.ultima_posicao = -1 # Ponteiro.
        self.vetor = np.empty(self.capacidade, dtype=int)   # Vetor numpy.
    

    # O(n)
    def imprime(self) -> None: # Método para imprimir o vetor.
        if self.ultima_posicao == -1: # Conferindo se o vetor está vazio.
            print('O vetor está vazio.')
        else:
            print('P  /  N')
            for i in range(self.ultima_posicao + 1): 
                print(i, ' - ', self.vetor[i]) # Imprimindo vetor.

    # O(1) - O(2)
    def insere(self, valor) -> None:
        if isinstance(valor, int): # Conferindo se o valor é inteiro.
            if self.ultima_posicao == self.capacidade - 1: # Conferindo a capacidade máxima do vetor.
                print('Capacidade máxima atingida.')
            else:
                self.ultima_posicao += 1 # Atualizando o ponteiro.
                self.vetor[self.ultima_posicao] = valor # Inserindo um valor no vetor.
        else:
            print('É necessário um valor inteiro.')

    # O(n)
    def pesquisa(self, valor) -> int: # Método para pesquisar um valor no vetor.
        if isinstance(valor, int): # Conferindo se o valor é inteiro.
            for i in range(self.ultima_posicao + 1): # Passando pela quantidade de elementos no vetor.
                if valor == self.vetor[i]: # Conferindo se o valor pesquisado é igual aos elementos do vetor.
                    return i # Retornando a posição do número encontrado.
            return -1
        else:
            print('É necessário um valor inteiro.')
    
    # O(n)
    def exclui(self, valor) -> int: # Método para exlcuir um valor do vetor.
        if isinstance(valor, int): # Conferindo se o valor é inteiro.
            posicao = self.pesquisa(valor) # Fazendo uma pesquisa com o método pesquisa.
            if posicao == -1: 
                return -1
            else:
                for i in range(posicao, self.ultima_posicao):
                    self.vetor[i] = self.vetor[i + 1]

                self.ultima_posicao -= 1


# Testes


vetor = VetorNaoOrdenado(5)

vetor.imprime()

vetor.insere(9)
vetor.insere(2)
vetor.insere(1)
vetor.insere(8)
vetor.insere(3)

vetor.imprime()

print(vetor.pesquisa(3))
print(vetor.pesquisa(10))

vetor.exclui(9)
vetor.exclui(2)
vetor.exclui(3)

vetor.imprime()

vetor.insere(1)
vetor.insere(0)
vetor.insere(6)

vetor.imprime()

vetor.exclui(1)

vetor.imprime()