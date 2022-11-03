# CONSTANT - O(1)
lista = [1, 2, 3, 4, 5]

def constant(n):
    print(n[0])

print('Constant: ')
constant(lista)
print()


# LINEAR - O(n)
def linear(n):
    for i in n:
        print(i)

print('Linear:')
linear(lista)
print()


#QUADRATIC O(n^2) - Polynomial
def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)
        print('---')

print('Quadratic')
quadratic(lista)
print()

# COMBINATION
# O(1) + O(5) + O(n) + O(n) + O(3)
# O(9) + O(2n) -> O(n)
def combination(n): 
    print(n[0]) # O(1)

    for i in range(5): # O(5)
        print('Test', i)
    
    for i in n: # O(n)
        print(i)
    
    for i in n: # O(n)
        print(i)
    
    # O(3)
    print('Python') # O(1)
    print('Python') # O(1)
    print('Python') # O(1)