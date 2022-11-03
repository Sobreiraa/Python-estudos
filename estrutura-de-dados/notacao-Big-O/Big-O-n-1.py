# Criando duas funções diferentes que faça a mesma somatória

# Função 1

# 11 passos
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    
    return soma

print('Função 1')
print(soma1(10))


# Função 2

# 3 passos
# O(3)
def soma2(n):
    return (n * (n + 1)) / 2

print('Função 2')
print(soma2(10))
