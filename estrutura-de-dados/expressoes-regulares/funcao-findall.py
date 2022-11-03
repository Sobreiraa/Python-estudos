import re

# Função \\\\\\\\FINDALL//////// 


frase = 'Meu número de telefone atual é (62)99237-9966. O número (56)99533-8763'
print()
print(frase)
print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase))
print()


emails = '''Nome: Teste 1
Email: teste1@teste.com
Nome: Teste 2
Email: teste2@teste.com
Nome: Teste 3
Email: teste3@teste.com.br
'''
print()
print(emails)
print(re.findall('\w+@\w+\.\w*', emails))
print()