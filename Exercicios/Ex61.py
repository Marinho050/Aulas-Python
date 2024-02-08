# Ex61
def soma ():
    maior = menor = 0
    opcao = ""

    while opcao.lower() != "n":
        print("Digite vários números")
        num = int(input("-------->"))

        if num > maior:
            maior = num
        elif num < menor or menor == 0:
            menor = num

        opcao = input("Deseja continuar? [S/N] -> ")



soma()