# Escreva um código que apresente a classe Circulo, com atributos raio, área e perímetro. Crie também os métodos calcular_area, calcular_perimetro e imprimir. Os métodos calcular_area e calcular_perimetrodevem efetuar seus respectivos cálculos e colocar os valores nos atributos area e perimetro. O método imprimir deve mostrar na tela os valores de todos os atributos.


class Circulo:

    pi = 3.14

    def __init__(self, raio: int or float) -> None:
        self.__raio = raio
        self.__area = 0
        self.__perimetro = 0 

    def calcular_area(self) -> None:
        if isinstance(self.__raio, int or float):
            self.__area = Circulo.pi * self.__raio * self.__raio
            return self.__area
        else:
            print('O lado do círculo deve ser um número inteiro ou flutuante.')
    
    def calcular_perametro(self) -> None:
        if isinstance(self.__raio, int or float):
            self.__perimetro = (2 * Circulo.pi * self.__raio)
            return self.__perimetro
        else:
            print('O lado do círculo deve ser um número inteiro ou flutuante.')
    
    def imprimir(self) -> str:
        if isinstance(self.__raio, int or float):
            print(f'Raio: {self.__raio}')
            print(f'Área: {self.__area:.2f}')
            print(f'Perímetro: {self.__perimetro:.2f}')
        else:
            print('Erro ao instanciar os valores do objeto.')


c1 = Circulo(6)
c1.calcular_area()
c1.calcular_perametro()
c1.imprimir()