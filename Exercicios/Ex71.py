# Ex71
def divisao(a, b):
    div = a/b
    return div

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(divisao(num1, num2))

except ZeroDivisionError:
    print("ERRO! A divisão não é possivel com ZERO.")

except ValueError:
    print("ERRO! Não é possivel inserir caracteres.")

finally:
    print("Terminou.")
