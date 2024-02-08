#Ex 035
while True:
    numero = int(input("Digite um número para ver a sua tabuada (0 ou negativo para sair): "))
    if numero <= 0:
        break

    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

print("Programa encerrado.")

