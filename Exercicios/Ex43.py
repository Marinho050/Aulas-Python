# Ex43

lista = []
maior = menor = 0

print("Digite 5 números para guardar numa lista.")
for c in range(1, 6):
    num = int(input(f"Digite o {c} numero: "))
    lista.append(num)  # Add the entered number to the list

for a in lista:
    if a > maior:
        maior = a
    if a < menor or menor == 0:
        menor = a

print(f"O maior número gerado foi o: {maior}")
print(f"O menor número gerado foi o: {menor}")
