#Ex44

numeros = []

while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")

    if entrada.lower() == 'sair':
        break

    numero = int(entrada)

    if numero not in numeros:
        numeros.append(numero)
    else:
        print("Número já está na lista. Tente novamente.")

# Ordenar a lista em ordem decrescente
numeros.sort(reverse=True)

# Mostrar os valores em ordem decrescente
print("\nValores em ordem DECRESCENTE:")
for num in numeros:
    print(num)