import re

# Função \\\\\\\\MATCH//////// 

frase = 'A placa do carro que eu anotei durante o acidente foi PRT-1998'
print()
print(frase)
print(re.match('[A-Za-z]{3}-\d{4}', frase)) # Procurando a expressão regular no ínicio.
print()

frase2 = 'PRT-1998 é a placa do carro que anotei durante o acidente.'
print(frase2)
print(re.match('[A-Za-z]{3}-\d{4}', frase2)) # Procurando a expressão regular no ínicio.
