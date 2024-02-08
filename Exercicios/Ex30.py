#Ex30
#Ler valores
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

opcao = 0

while opcao != 5:
    print("\nO que pretende fazer com os valores?\n")
    print("[ 1 ] SOMAR")
    print("[ 2 ] MULTIPLICAR")
    print("[ 3 ] MAIOR")
    print("[ 4 ] NOVOS NÚMEROS")
    print("[ 5 ] SAIR")
    opcao = int(input("---> "))

    if opcao == 1:
        soma = a + b + c
        print(f'{a} + {b} + {c} = {soma}')
    elif opcao == 2:
        relacao = a * b * c
        print(f'{a} x {b} x {c} = {relacao}')
    elif opcao == 3:
        print(f"O maior número é: {max(a, b, c)}")
    elif opcao == 4:
        print("Insira novos números:")
        a = int(input("Digite o primeiro valor: "))
        b = int(input("Digite o segundo valor: "))
        c = int(input("Digite o terceiro valor: "))
    elif opcao == 5:
        print("A sair do programa...")
        break
    else:
        print("Opção inválida. Tente de novo.")
