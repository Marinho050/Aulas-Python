# Ex56
lista = list()
quant = 0
soma_idades = 0
mulheres = 0
homens = 0

while True:
    temp = dict()
    temp["Nome"] = input("Digite o nome: ")
    temp["Sexo"] = input("Digite o sexo: ")
    if temp["Sexo"][0] == "f":
        mulheres += 1
    temp["Idade"] = int(input("Digite a idade: "))
    lista.append(temp)
    opcao = input("Deseja continuar? [S/N]").strip().lower()
    quant += 1
    if opcao == "n":
        break

# Quantas pessoas foram registadas;
print(f"Foram registadas {quant} pessoas.")

# Qual a média de idades do grupo;
for valor in range(0, len(lista)):
     soma_idades += lista[valor]["Idade"]
media = soma_idades/quant
print(f"A média de idades é {media} anos.")

# Quantas mulheres foram registadas;
print(f"Foram registadas {mulheres} mulheres.")

# homens acima da média
for c in range(0, len(lista)):
    if lista[c]["Sexo"] == "m" and lista[c]["Idade"] > media:
        homens += 1

print(f"Há {homens} com idade acima da média.")
