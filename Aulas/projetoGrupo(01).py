print("CALCULADORA DE INDICE DE MASSA CORPORAL")
peso=float(input("Digite a sua peso em (kg):"))
altura=float (input("Digite a sua altura em (m):"))

imc = peso /(altura *altura)

if imc < 18.5:
    print(f"O seu imc é de {imc:.2f}, está Abaixo do peso ")

elif (imc >= 18.5) and (imc <= 24.9):
    print(f"O seu imc é de {imc:.2f}, está com o Peso Normal")

elif (imc >= 25.0) and (imc <= 29.9):
    print(f"O seu imc é de {imc:.2f}, está com Sobrepeso")

elif (imc >= 30.0) and (imc <=34.9):
    print(f"O seu imc é de {imc:.2f}, está com Obsidade grau 1 ")

elif (imc >= 35.0) and (imc <= 39.9):
    print(f" O seu imc é de {imc:.2f}, está com Obsidade Grau 2")

elif imc >= 40:
    print(f" O seu imc é de {imc:.2f}, está com Obsidade Grau 3")


