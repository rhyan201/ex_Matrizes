import numpy as np

ingredientes = []
pedidos = []
resultado = []

for i in range(3):
    a = []
    for j in range(3):
        elemento = int(input(f"Digite a quantidade de produtos na posição ({i}, {j})"))
        a.append(elemento)
    ingredientes.append(a)

ingredientes_np = np.array(ingredientes)
print(ingredientes_np)

for k in range(3):
    b = []
    for l in range(3):
        elemento2 = int(input(f"Digite a quantidade de produtos vendidos na posição ({k}, {l})"))
        b.append(elemento2)
    pedidos.append(b)

pedidos_np = np.array(pedidos)
print(pedidos_np)

resultado_np = np.dot(ingredientes_np, pedidos_np)
print("Resultado:")
print(resultado_np)