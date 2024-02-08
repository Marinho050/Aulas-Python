# Ex49

lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for indice in range(0, 3):
    for valor in range(0, 3):
        lista[indice][valor] = int(input(f"Digite o valor para [{indice}][{valor}]: "))

for indice in range(0, 3):
    for valor in range(0, 3):
        print(f"[{lista[indice][valor]}]", end=" ")
    print()

