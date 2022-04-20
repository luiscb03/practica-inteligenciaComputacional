import numpy as np

def matrizIdentidad():
    matriz = np.random.random((5, 5))

    for i in range(5):
        for j in range(5):
            if i != j:
                matriz[i, j] = 0

    print(matriz)

def promedioCalificaciones():
    matriz = np.random.uniform(0,5, size=(7, 7))
    promedio = matriz.mean()
    print(f'El promedio del curso es: {promedio}')
    #print(matriz)
    res = matriz[matriz > promedio]
    print(res)

promedioCalificaciones()

