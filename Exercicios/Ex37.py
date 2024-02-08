# Ex 037

mais_25 = 0
homens_menos_17 = 0
mulheres = 0
menores_idade = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo: [M/F] ").lower().strip()
    opcao = input("Quer continuar? [S/N]: ").lower().strip()
    if opcao == "n":
        break
    if idade > 25:
        mais_25 += 1
    if sexo == "m" and idade < 17:
        homens_menos_17 += 1
    if sexo == "f":
        mulheres += 1
    if idade < 18:
        menores_idade += 1

print(f"Há {mais_25} pessoas com mais de 25 anos.")
print(f"Há {homens_menos_17} homens com menos de 17 anos.")
print(f"Há {mulheres} mulheres registadas.")
print(f"Há {menores_idade} menores de idade.")