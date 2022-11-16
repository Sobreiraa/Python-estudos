# Escreva um código que apresente a classe Quadrado, com atributos lado, área e perímetro. Crie também os métodos calcular_area, calcular_perimetro e imprimir. Os métodos calcular_area e calcular_perimetrodevem efetuar seus respectivos cálculos e colocar os valores nos atributos area e perimetro. O método imprimir deve mostrar na tela os valores de todos os atributos.

class Quadrado:

    def __init__(self, lado: int or float) -> None:
        self.__lado = lado
        self.__area = 0
        self.__perimetro = 0

    def calcular_area(self) -> int or float:
        if isinstance(self.__lado, int or float):
            self.__area = self.__lado * self.__lado
            return self.__area
        else:
            print('O lado do quadrado deve ser um número inteiro ou flutuante.')
    
    def calcular_perimetro(self) -> int or float:
        if isinstance(self.__lado, int or float):
            self.__perimetro = 4 * self.__lado
            return self.__perimetro
        else:
            print('O lado do quadrado deve ser um número inteiro ou flutuante.')
    
    def imprimir(self) -> str:
        if isinstance(self.__lado, int or float):
            print(f'Lado: {self.__lado}')
            print(f'Área: {self.__area}')
            print(f'Perímetro: {self.__perimetro}')
        else:
            print('Erro ao instanciar os valores do objeto.')


q1 = Quadrado(8)
print(q1.calcular_area())
print(q1.calcular_perimetro())

q1.imprimir()