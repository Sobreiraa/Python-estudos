'''
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto, ou seja, as ações que este objeto pode realizar no seu sistema.

Em python, dividimos os métodos em 2 grupos:
    - Métodos de Instância: Precisa de acesso de uma instância do objeto.
    - Métodos de Classe: Não tem nenhum acesso a qualquer instância do objeto
'''

# Métodos de Instância:
class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False 
    
    # Exemplo do método de Instância
    def ligar(self):
        '''Liga a lâmpada'''
        print(f'Ligando...')
        self.__ligada = True
    
lampada1 = Lampada('amarelo', 150, 'alta')
lampada1.ligar()

# Métodos de Classe:
class Usuario:

    contador = 0 

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        Usuario.contador = self.__id
        print(f'Usuário {self.__gera_usuario()} gerado com sucesso.')
    

    # Exemplo do método de Classe
    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema.')
    
    # Exemplo do método Estático 
    @staticmethod
    def definicao():
        return 'UXR344'
    
    # Método privado (Só é acessado na class)
    def __gera_usuario(self):
        return self.__email.split('@')[0]
    


user = Usuario('Matheus', 'Sobreira', 'matheusobreira@gmail.com', '456789')

Usuario.conta_usuarios() #Forma correta
user.conta_usuarios() #Forma incorreta

print(Usuario.definicao())


