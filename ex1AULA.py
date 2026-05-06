import numpy as np

matrizMANHA = []
matrizNOITE = []

#MANHA
for i in range(3):
    dia1 = []
    for j in range(3):
        elemento1 = float(input(f"Digite um valor para ({i}, {j}): "))
        dia1.append(elemento1)
    matrizMANHA.append(dia1)

matrizMANHA_np = np.array(matrizMANHA)

print(matrizMANHA_np)

#tarde
for k in range(3):
    dia2 = []
    for l in range(3):
        elemento2 = float(input(f"Digite um valor para ({k}, {l}): "))
        dia2.append(elemento2)
    matrizNOITE.append(dia2)

matrizNOITE_np = np.array(matrizNOITE)

print(matrizNOITE_np)

matrizTOTAL = matrizMANHA_np + matrizNOITE_np
np.array(matrizTOTAL)

print(matrizTOTAL)