import numpy as np

estoque_inicial = []
vendidos = []
estoque_final = []

for i in range(3):
    a = []
    for j in range(3):
        elemento = int(input(f"Digite a quantidade de produtos na posição ({i}, {j})"))
        a.append(elemento)
    estoque_inicial.append(a)

estoque_inicial_np = np.array(estoque_inicial)
print(estoque_inicial_np)

for k in range(3):
    b = []
    for l in range(3):
        elemento2 = int(input(f"Digite a quantidade de produtos vendidos na posição ({k}, {l})"))
        b.append(elemento2)
    vendidos.append(b)

vendidos_np = np.array(vendidos)
print(vendidos_np)

estoque_final_np = np.array(estoque_final)
estoque_final_np = estoque_inicial_np - vendidos_np
print("Estoque final:")
print(estoque_final_np)