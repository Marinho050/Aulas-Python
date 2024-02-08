# Ex57

import os

jogadores = list()

while True:
    jogador = dict()
    jogador["nome"] = input("Digite o nome do jogador: ")
    jogador["qntjogos"] = int(input("Quantidade de jogos: "))
    jogador["qntgolos"] = int(input("Quantidade de golos: "))
    jogador["mediagolos"] = jogador["qntgolos"] / jogador["qntjogos"]
    jogadores.append(jogador)
    opcao = input("Quer continuar? [S/N]\n--> ").strip().lower()
    if opcao == "n":
        break

print("\n")
print("=-"*20)
print(f"{'SISTEMA DE VISUALIZAÇÃO DE JOGADORES':^40}")
print("=-"*20)

while True:
    escolha_jogador = input("Qual jogador deseja ver?\n---> ").strip().lower()

    for c in range(0, len(jogadores)):
        if jogadores[c]["nome"].lower() == escolha_jogador:
            print(f"O jogador {jogadores[c]['nome']} fez {jogadores[c]['qntjogos']} jogos e marcou {jogadores[c]['qntgolos']} golos.")
            print(f"Isto dá uma média de {jogadores[c]['mediagolos']:.3} golos marcados por jogo.")
    opcao = input("Deseja ver outro jogador? [S/N]\n--> ").strip().lower()
    if opcao == "n":
        break