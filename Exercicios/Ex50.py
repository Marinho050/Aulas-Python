# Ex50

lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for indice in range(0, 3):
    for valor in range(0, 3):
        lista[indice][valor] = int(input(f"Digite um valor para [{indice}][{valor}]: "))

for indice in range(0, 3):
    for valor in range(0, 3):
        print(f"[{lista[indice][valor]}]", end=" ")
    print()

soma_pares = 0
soma_segunda_coluna = 0
maior_terceira_linha = 0

#soma pares
for indice in range(0, 3):
    for valor in range(0, 3):
        if lista[indice][valor] % 2 == 0:
            soma_pares += lista[indice][valor]
print(f"A soma de todos os valores pares é: {soma_pares}")

#soma segunda coluna
for indice in range(0, 3):
    soma_segunda_coluna += lista[indice][1]
print(f"A soma de todos os valores da segunda coluna é: {soma_segunda_coluna}")

#maior terceira linha
for indice in range(0, 3):
    if indice == 0:
        maior_terceira_linha = lista[2][indice]
    else:
        if lista[2][indice] > maior_terceira_linha:
            maior_terceira_linha = lista[2][indice]
print(f"O maior valor da terceira linha é: {maior_terceira_linha}")