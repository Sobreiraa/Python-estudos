# 04 - Escreva um código que apresente a classe Retangulo, com atributos comprimento, largura, área e perímetro. Crie também os métodos calcular_area, calcular_perimetro e imprimir. Os métodos calcular_area e calcular_perimetrodevem efetuar seus respectivos cálculos e colocar os valores nos atributos area e perimetro. O método imprimir deve mostrar na tela os valores de todos os atributos.

class Retangulo:

    def __init__(self, comprimento: int or float, largura: int or float) -> None:
        self.__comprimento = comprimento
        self.__largura = largura
        self.__area = 0
        self.__perimetro = 0
    
    def calcula_area(self) -> None:
        if isinstance(self.__comprimento, int or float):
            if isinstance(self.__largura, int or float):
                self.__area = self.__comprimento * self.__largura
        else:
            print('O lado do retângulo deve ser um número inteiro ou flutuante.')
    
    def calcula_perimetro(self) -> None:
        if isinstance(self.__comprimento, int or float):
            if isinstance(self.__largura, int or float):
                self.__perimetro = (2 * self.__comprimento) + (2 * self.__largura)
        else:
            print('O lado do retângulo deve ser um número inteiro ou flutuante.')

    def imprimir(self) -> str:
        if isinstance(self.__comprimento, int or float):
            if isinstance(self.__largura, int or float):
                print(f'Comprimento: {self.__comprimento}')
                print(f'Largura: {self.__largura}')
                print(f'Área: {self.__area}')
                print(f'Perímetro: {self.__perimetro}')
        else:
            print('Erro ao instanciar os valores do objeto.')

r1 = Retangulo('5', '12')
r1.calcula_area()
r1.calcula_perimetro()
r1.imprimir()