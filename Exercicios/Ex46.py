# Ex46
lista = list()
pares = list()
impares = list()

opcao = ""

while opcao != "n":
    novo_num = int(input("Digite um número: "))
    lista.append(novo_num)
    if novo_num % 2 == 0:
        pares.append(novo_num)
    else:
        impares.append(novo_num)
    opcao = input("Deseja continuar? [S/N] -> ")

print("~*" * 20)
print(f"Os números inseridos foram: {lista}")
print(f"Os números pares inseridos foram: {pares}")
print(f"Os números ímpares inseridos foram: {impares}")
print("~*" * 20)


