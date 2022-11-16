'''
POO - Objetos

Objetos -> São instâncias da classe, ou seja, após o mapeamento do objeto do mundo real para sua representação computacional, podemos criar quantos objetos forem necessários. Pensamos nos objetos/istâncias de uma classe como variáveis do tipo definido na classe.
'''

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False
    
    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True
    
    def checa_lampada(self):
        return self.__ligada


# Instâncias/Objetos
lamp1 = Lampada('amarelo', 110, 60)
lamp1.ligar_desligar()
lamp1.ligar_desligar()
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')