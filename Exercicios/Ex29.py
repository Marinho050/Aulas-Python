# EX029
from random import randint
cpu = randint(0, 10)

print("-" * 37)
print("WELCOME TO OUR 'GUESS DE NUMBER' GAME")
print("-" * 37)

coisas = input("Carrega ENTER para iniciar...")

certo = False
palpites = 0

print("\n\nAcabei de pensar num número! Será que consegues adivinhar? :D\n")

while not certo:
    jogador = int(input(f"{palpites + 1}ª - Qual é o teu palpite? ---> "))
    palpites += 1
    if jogador == cpu:
        certo = True
    else:
        if jogador < cpu:
            print("Mais acima...")
        elif jogador > cpu:
            print("Mais abaixo...")

print("BOA!!!!")
print(f"ACERTAS-TE COM APENAS {palpites} TENTATIVAS!!!")
