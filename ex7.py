import numpy as np

matriz = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
matriz = np.array(matriz)

print("Matriz original:")
print(matriz)


matriz[0][1] = 67
matriz[2][4] = 67
print("Matriz após alteração:")
print(matriz)