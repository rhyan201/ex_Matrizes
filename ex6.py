import numpy as np

matriz = [
    [1,42,3,41],
    [34,12,4,3],
    [2,32,45,6],
    [3,5,7,8]
]
matriz = np.array(matriz)

print("Matriz original:")
print(matriz)

matriz[:] = [1]

print("Matriz após alteração: ")
print(matriz)