from ast import If

import numpy as np

matriz = np.random.random((5, 5))

for i in range(5):
    for j in range(5):
        if i != j:
            matriz[i, j] = 0

print(matriz)