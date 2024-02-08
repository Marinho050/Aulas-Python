# Ex51

from random import randint
from time import sleep

print("*=" * 20)
print(f"{'EUROMILHÕES':^40}")
print("*=" * 20)
print()

palpites = int(input("Quantos palpites deseja que eu crie?\n---> "))
print("A gerar chaves", end="")
sleep(1)
print(".", end="")
sleep(1)
print(".", end="")
sleep(1)
print(".", end="")
sleep(1)
print()

for a in range(0, palpites):
    chave = [[], []]
    for i in range(0, 5):
        while True:
            num = randint(1, 50)
            if num not in chave[0]:
                chave[0].append(num)
                break

    for i in range(0, 2):
        while True:
            num = randint(1, 12)
            if num not in chave[1]:
                chave[1].append(num)
                break

    while True:
        # mostrar números
        print(f"Chave {a + 1:0>2}:", end=" | ")
        for numero in chave[0]:
            print(f"{numero:0>2}", end=" | ")
            sleep(0.2)
        print("", end=" | ")
        for estrela in chave[1]:
            print(f"*{estrela:0>2}", end=" | ")
            sleep(0.2)
        print("")
        break
sleep(0.4)
print("Chaves geradas com sucesso! Boa sorte e volte sempre!")


