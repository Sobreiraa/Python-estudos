'''
POO - Métodos Mágicos

Métodos Mágicos são todos os métodos que utilizam dunder.

Dunder init -> __init__()
    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

Dunder repr -> __repr__() / Representação do objeto
    def __repr__(self) -> str:
        return f'{self.titulo} escrito por {self.autor}'

Dunder str -> __str__() / Representa para os usuários como uma string 
     def __str__(self) -> str:
        return self.titulo

Dunder len -> __len__() / Retorna a quantidade de algum valor inteiro do objeto
    def __len__(self) -> int:
        return self.paginas

Dunder: Double Underscore
'''

class Livro:

    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __repr__(self) -> str:
        return f'{self.titulo} escrito por {self.autor}'
    
    def __str__(self) -> str:
        return self.titulo
    
    def __len__(self) -> int:
        return self.paginas
    

livro1 = Livro('A menina que roubava livros', 'Pedro', 400)
livro2 = Livro('O apanhador no campo de centeio', 'Lucas G.', 350)

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

del livro2