# Ex038
numeros_extenso = ("zero", "um", "dois", "três", "quatro", "cinco",
                   "seis", "sete", "oito", "nove", "dez", "onze",
                   "doze", "treze", "catorze", "quinze", "dezasseis",
                   "dezassete", "dezoito", "dezanove", "vinte")

while True:
    num = int(input("Digite um número de 0 a 20: "))
    if num >= 0 and num <= 20:
        break
    else:
        print("Por favor digite um número entre 0 e 20.")

print(f"Inseriu o número {numeros_extenso[num]}.")