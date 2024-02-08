from math import factorial


def header(msg):
    print(f"-----{msg}-----")


def calculadora(a, b, c="+"):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "x":
        return a * b
    elif c == "/":
        return a / b


def tabuada(num):
    while True:
        if num <= 0:
            break

        print(f"Tabuada de {num}:")
        for i in range(num):
            print(f"{num} x {i} = {num * i}")


def ParOuImpar(a):
    resto = a % 2
    if resto == 0:
        print(f"O numero {a} é um numero par.")
    else:
        print(f"O numero {a} é um numero impar.")


def Factorial(a):
    f = factorial(a)
    print(f"O fatorial de {a} é {f}\n")


def MainMenu():
    opcao = 0
    while opcao != 6:
        print("[1]-Calculadora")
        print("[2]-Tabuada")
        print("[3]-Par ou Impar")
        print("[4]-Números Primos")
        print("[5]-Factorial")
        print("[6]-Sair")
        opcao = input("---> ")

        if opcao == "1":
            print("Calculadora")
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, x, /): ")
            resultado = calculadora(a, b, operacao)
            print(f"Resultado: {resultado}")
        elif opcao == "2":
            print("Tabuada")
            num = int(input("Digite o número para a tabuada: "))
            tabuada(num)
        elif opcao == "3":
            print("Par ou impar")
            num = int(input("Digite o número: "))
            ParOuImpar(num)
        elif opcao == "4":
            print("Opção 4 selecionada: Procurar")
        elif opcao == "5":
            print("Factorial")
            num = int(input("Digite o número: "))
            Factorial(num)
        elif opcao == "6":
            print("A sair do programa...")
        else:
            print("Opção inválida. Tente de novo.")


header("BEM VINDO")
MainMenu()

