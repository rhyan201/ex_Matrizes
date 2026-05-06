import numpy as np

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz = np.array(matriz)

print("Matriz antes da limpeza:")
print(matriz)

matriz[:] = 0

print("Matriz após a limpeza: ")
print(matriz)
