from pessoa import Pessoa

#Criando pessoas (criando um objeto atráves de uma classe)
p1 = Pessoa('Matheus', 21)
p2 = Pessoa('João', 32)

p1.falar('POO')
p2.comer('sorvete')
p1.comer('churrasco')

print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())