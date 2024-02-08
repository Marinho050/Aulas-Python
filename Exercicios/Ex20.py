#Ex20
import random
import time
#Ler opçao de escolha
print("[ 1 ] - Pedra:")
print("[ 2 ]- Papel: ")
print("[ 3 ]- Tesoura")
numero= random.randrange(start=1 ,stop= 3)
jogada=int(input("Digite a sua opcao:"))
if jogada -numero == 0 :
 print(input(f"Empate"))
elif jogada - numero == -2 :
    print(input(f"Vitoria"))
else :
    print(input(f"Derrota"))