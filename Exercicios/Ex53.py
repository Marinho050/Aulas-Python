# Ex53
from random import randint
from time import sleep
from operator import itemgetter

jogo = {"Ricardo": randint(1, 6),
        "Alfredo": randint(1, 6),
        "Carla": randint(1, 6),
        "Francisco": randint(1, 6)
}

ranking = dict()

print("Valores sorteados:")
for k, v in jogo.items():
    sleep(1)
    print(f"{k} tirou {v} no dado.")

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
sleep(1)
print("=-" * 15)
print(f"{'Ranking:':^30}")
print("=-" * 15)
sleep(1)
for i, v in enumerate(ranking):
    sleep(1)
    print(f"{i+1}.ª lugar ---> {v[0]} com {v[1]}.")