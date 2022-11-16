'''O que são dataclasses? O módulo Dataclasses fornece um decorador e funções para criar automaticamente métodos, como __init__, __repr__ (etc) em classes definidas pelo usuário.
Basicamente, dataclasses são syntas sugar para criar classes normais.
Leia a documentação: https://docs.python.org/3/library/dataclasses.html'''

from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple # Transformando a classe em dicionário e tupla

@dataclass(eq=False, repr=True, order=False, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self): # Usando o pst init para forçar um tipo de dado criado no init.
        if not isinstance(self.nome, str):
            raise TypeError(f'Tipo inválido {type(self.nome).__name__} != str em {self}.')

    '''def __post_init__(self): # Usando o post init para criar um atributo após o init ser inicializado.
        self.nome_completo = f'{self.nome} {self.sobrenome}'.title()'''

    '''@property
    def nome_completo(self) -> str:
        return f'{self.nome} {self.sobrenome}'.title()'''

p1 = Pessoa('matheus', 'sobreira')
p2 = Pessoa('Maria', 'Joaquina')

print(p1 == p2)

print(p1)
print(p1.nome)
print(p1.sobrenome)

print('-' * 50)

print(asdict(p1)) # Transformando em dicionário
print(astuple(p2)) # Transformando em tupla