'''Crie expressões regulares para extrair as seguintes informações do texto (use a função findall)
- CEPs
- URLs'''

import re

texto_ceps = 'Me chamo matheus tenho 21 anos, o cep da minha casa é 75114-550 e o da minha antiga casa é 75550-910.' 
print()
print(texto_ceps)
print('Buscando números:', re.findall('\d', texto_ceps))
print('Buscando ceps:', re.findall('\d{5}-\d{3}', texto_ceps))
print()

texto_url = 'Estou estudando Expressões Regulares e um link bom para revisar os estudos é https://www.iaexpert.academy, https://www.youtube.com/ e https://www.google.com'

# MINHA SOLUÇÃO
print()
print(texto_url)
print('Buscando url:', re.findall('\w+\:\//\w{3}\.\w+\.\w+', texto_url)) 
print()

# SOLUÇÃO DO PROFESSOR
print()
print(texto_url)
print('Buscando url:', re.findall('https?://[A-Za-z0-9./]+', texto_url)) 
print()