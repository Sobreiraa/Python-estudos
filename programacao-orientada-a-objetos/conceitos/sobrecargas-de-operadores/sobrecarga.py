'''
Em python, o comprtamento dos operadores é definido por métodos especiais. Vamos alterar o comportamento de operadores com classes definidas pelo usuário.
'''

class Retangulo:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'<class Retangulo({self.x}, {self.y})>'

    def __add__(self, other) -> int:
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)
    
    def get_area(self) -> int:
        return self.x * self.y
    
    def __lt__(self, other) -> bool:
        a1 = self.area()
        a2 = other.x

        if a1 < a1:
            return True
        else:
            return False
    
    def __gt__(self, other) -> bool:
        a1 = self.area()
        a2 = other.area()

        if a1 > a1:
            return True
        else:
            return False





r1 = Retangulo(10, 20)
r2 = Retangulo(5, 30)
r3 = r1 + r2
print(r1 + r2)
print(r1 == r1)
print(r1 < r2)
print(type(r3))