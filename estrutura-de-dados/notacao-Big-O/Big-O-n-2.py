# Criar duas listas com um tamanho de 1000 elementos

# Função 3
# O(1000) -> O(n)
def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

print('Lista 1')
print(lista1())
print('Tamanho da lista:', len(lista1()))


# Funlçao 4

def lista2():
    return range(1000)

l = lista2()
 
print('Lista 2')

for i in l:
    print(i)

print('Tamanho da lista:', len(l))