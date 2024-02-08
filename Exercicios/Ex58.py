# Ex58
def boas_vindas():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Calculador de area")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


def area(b,h):
    r= b * h
    print(f"A area do terreno é {r}")


# programa principal
boas_vindas()

b= int(input("Insira o base do terreno: "))
h=int(input("Insira a altura do terreno: "))

area(b,h)
