import re # regular expressions

# Função \\\\\\\\SEARCH//////// 

frase = 'Olá, meu número de telefone é (42)0000-0000'
print()
print(frase)
print(re.search('\(\d{2}\)\d{4,5}-\d{4}', frase)) # Fazendo busca de uma expressão regular
print()

placa = 'A placa do carro que eu anotei durante o acidente foi FRT-1998'
print(placa)
print(re.search('[A-Za-z]{3}-\d{4}', placa)) # Fazendo busca de uma expressão regular
print()

email = 'Entre em contato atráves do meu email: matheusobreira27@gmail.com'
print(email)
print(re.search('\w+@\w+\.com', email)) # Fazendo busca de uma expressão regular
print()