# Ex67
def valida_numero():
    while True:
        num = input("Insira um número: ")
        if num.isnumeric():
            print("Isso é um número inteiro.")
            break
        else:
            print("Isso não é um número inteiro. Tente novamente.")


valida_numero()
