# Ex48

lista = [[], []]

for c in range(0, 10):
    num = int(input(f"Digite o {c+1} números: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f"Os numeros  inseridos foram: {lista}")
print(f"Os numeros pares inseridos foram: {lista[0]}")
print(f"Os numeros impares inseridos foram: {lista[1]}")


