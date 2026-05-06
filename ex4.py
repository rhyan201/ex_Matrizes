import numpy as np

salarios = []


for i in range(3):
    a = []
    for j in range(3):
        elemento = int(input(f"Digite a quantidade de produtos na posição ({i}, {j})"))
        a.append(elemento)
    salarios.append(a)

salarios_np = np.array(salarios)

resultado_np = salarios_np*1.1
print("Resultado:")
print(resultado_np)