# Ex55
jogador = dict()
jogador["nome"] = input("Digite o nome do jogador: ")
jogador["qntjogos"] = int(input("Quantidade de jogos: "))
jogador["qntgolos"] = int(input("Quantidade de golos: "))
jogador["mediagolos"] = jogador["qntgolos"] / jogador["qntjogos"]

print(f"O jogador {jogador['nome']} fez {jogador['qntjogos']} jogos e marcou {jogador['qntgolos']} golos.")
print(f"Isto dá uma média de {jogador['mediagolos']:.3} golos marcados por jogo.")