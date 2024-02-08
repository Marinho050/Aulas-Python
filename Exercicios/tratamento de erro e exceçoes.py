def divisao(a, b):
    div = a / b
    return div


try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(divisao(num1, num2))

except ZeroDivisionError:
    print(f"ERRO ! A DIVISÃO POR ZERO NÃO É POSSÍVEL.")

except ValueError:
    print("O utilizador não digitou os números")

except EOFError:
    print("Erro do Fabio")

except KeyboardInterrupt:
    print("O programa foi fechado inesperadamente.")
else:
    print("A divisão é possível.")

finally:
    print("Terminou.")
