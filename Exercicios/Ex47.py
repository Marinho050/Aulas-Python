# Ex47
lista = list()
equacao = input("Digite a sua equação:\n---> ")
quantidade_parentises = 0

for letra in equacao:
    lista.append(letra)

for letra in lista:
    if letra == "(" or letra == ")":
        quantidade_parentises += 1

if quantidade_parentises % 2 == 0:
    print("A sua equação funciona.")
else:
    print("A sua equação está errada!")