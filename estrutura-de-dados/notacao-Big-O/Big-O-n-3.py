# %%

''' Funções Big-O

1 Constant
log(n) Logarithmic
n Linear
nlog(n) Log Linear
n^2 Quadratic
n^3 Cubic
2^n Exponential'''

from math import log
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 10, 100)
print(n)

print('-' * 75)
print('CONSTANT')
print(np.ones(n.shape))
print()

print('-' * 75)
print('LOGARITHMIC')
print(np.log(n))
print()


print('-' * 75)
print('LINEAR')
print(n)
print()

print('-' * 75)
print('LOG LINEAR')
print(n * np.log(n))
print()

print('-' * 75)
print('QUADRATIC')
print(n ** 2)
print()

print('-' * 75)
print('CUBIC')
print(n ** 3)
print()

print('-' * 75)
print('Exponential')
print(2**n)
print()

labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]

plt.figure(figsize=(10, 8))
plt.ylim(0, 100)
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')
# %%
