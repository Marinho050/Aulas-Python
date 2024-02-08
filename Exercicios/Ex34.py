# Ex034
resp = "S"
soma = quant = media = maior = menor = 0

while resp in "Ss":
    nota = float(input("Digite uma nota: "))
    soma += nota
    quant += 1
    if quant == 1:
        maior = menor = nota
    else:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota

    resp = input("Quer continuar? [S/N]: ").upper().strip()[0]
media = soma / quant
print(f"Digitou {quant} números e a média foi {media} valores.")
print(f"O maior valor foi {maior} e o menor foi {menor}")