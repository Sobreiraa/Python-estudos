from re import I
import numpy as np

class VetorOrdenado:
    
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.vetor = np.empty(self.capacidade, dtype=int)
    
    # O(n)
    def imprime(self) -> None: 
        if self.ultima_posicao == -1: 
            print('O vetor está vazio.')
        else:
            print('P  /  N')
            for i in range(self.ultima_posicao + 1): 
                print(i, ' - ', self.vetor[i]) 

    # O(n)
    def insere(self, valor):
        if isinstance(valor, int): 
            if self.ultima_posicao == self.capacidade - 1: 
                print('Capacidade máxima atingida.')
                return
            
            posicao = 0 
            for i in range(self.ultima_posicao + 1):
                posicao = i
                if self.vetor[i] > valor:
                    break
                if i == self.ultima_posicao:
                    posicao = i + 1

            x = self.ultima_posicao 
            while x >= posicao:
                self.vetor[x + 1] = self.vetor[x]
                x -= 1
            
            self.vetor[posicao] = valor
            self.ultima_posicao += 1
        else:
            print('É necessário um número do tipo int.')
        
    # O(n)
    def pesquisa_linear(self, valor) -> int:
        if isinstance(valor, int):
            for i in range(self.ultima_posicao +1):
                if self.vetor[i] > valor:
                    return -1
                if self.vetor[i] == valor:
                    return i
                if i == self.ultima_posicao:
                    posicao = i + 1
        else:
            print('É necessário um número do tipo int.')
    

    def pesquisa_binaria(self, valor) -> int:
        if isinstance(valor, int):
            limite_inferior = 0
            limite_superior = self.ultima_posicao

            while True:
                posicao_atual = int((limite_inferior + limite_superior) / 2)
                if self.vetor[posicao_atual] == valor:
                    return posicao_atual
                elif limite_inferior > limite_superior:
                    return -1
                else:
                    if self.vetor[posicao_atual] < valor:
                        limite_inferior = posicao_atual + 1
                    else:
                        limite_superior = posicao_atual -1 

    # O(n)
    def exclui(self, valor) -> int: 
        if isinstance(valor, int): 
            posicao = self.pesquisa_linear(valor)
            if posicao == -1:
                return -1
            else:
                for i in range(posicao, self.ultima_posicao):
                    self.vetor[i] = self.vetor[i + 1]

                self.ultima_posicao -= 1

# Testes da busca linear

vetor = VetorOrdenado(10)

vetor.imprime()

vetor.insere(18)
vetor.insere(7)
vetor.insere(4)
vetor.insere(9)
vetor.insere(0)
vetor.insere(1)
vetor.insere(8)
vetor.insere(5)
vetor.insere(12)
vetor.insere(-1)

print(vetor.pesquisa_linear(5))
print(vetor.pesquisa_linear(9))
print(vetor.pesquisa_linear(6))
print(vetor.pesquisa_linear(18))

vetor.exclui(-1)
vetor.exclui(12)
vetor.exclui(18)


vetor.imprime()

print('-' * 50)
print('-' * 50)

# Testes da busca binária

vetor_binario = VetorOrdenado(10)

vetor_binario.insere(25)
vetor_binario.insere(3)
vetor_binario.insere(19)
vetor_binario.insere(28)
vetor_binario.insere(21)
vetor_binario.insere(22)
vetor_binario.insere(23)
vetor_binario.insere(31)
vetor_binario.insere(6)
vetor_binario.insere(10)

vetor_binario.imprime()

print(vetor_binario.pesquisa_binaria(3))
print(vetor_binario.pesquisa_binaria(22))
print(vetor_binario.pesquisa_binaria(31))
print(vetor_binario.pesquisa_binaria(1))