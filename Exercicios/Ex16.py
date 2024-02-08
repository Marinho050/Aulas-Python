#Ex16
num1=float(input("Digite o primeiro numero: "))
num2=float(input("Digite o segundo numero: "))
num3=float(input("Digite o terceiro numero: "))
num4=float(input("Digite o quarto numero: "))
num5=float(input("Digite o quinto numero: "))

media= (num1 + num2 + num3 + num4 + num5) / 5

if media >= 9.5 :
    print(f"Passou",media)

elif media < 8  :
    print(f"Recuperação",media)

else :
    print(f"Reprova",media)