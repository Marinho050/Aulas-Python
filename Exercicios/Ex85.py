# Ex85
import random


class JogoPedraPapelTesoura:
    def __init__(self):
        self._opcoes = ["Pedra", "Papel", "Tesoura"]
        self._escolha_jogador = None
        self._escolha_computador = None

    @property
    def opcoes(self):
        return self._opcoes

    @property
    def escolha_jogador(self):
        return self._escolha_jogador

    @escolha_jogador.setter
    def escolha_jogador(self, escolha):
        if escolha.capitalize() in self.opcoes:
            self._escolha_jogador = escolha.capitalize()
        else:
            raise ValueError("Escolha inválida. Por favor, escolha Pedra, Papel ou Tesoura.")

    @property
    def escolha_computador(self):
        return self._escolha_computador

    def jogar(self):
        self._escolha_computador = random.choice(self.opcoes)
        print(f"Você escolheu: {self.escolha_jogador}")
        print(f"Computador escolheu: {self.escolha_computador}")

        if self.escolha_jogador == self.escolha_computador:
            return "Empate!"
        elif (
                (self.escolha_jogador == "Pedra" and self.escolha_computador == "Tesoura") or
                (self.escolha_jogador == "Papel" and self.escolha_computador == "Pedra") or
                (self.escolha_jogador == "Tesoura" and self.escolha_computador == "Papel")
        ):
            return "Você ganhou!"
        else:
            return "Você perdeu!"


if __name__ == "__main__":
    jogo = JogoPedraPapelTesoura()

    while True:
        escolha_jogador = input("Escolha Pedra, Papel ou Tesoura (ou 'sair' para encerrar): ")

        if escolha_jogador.lower() == "sair":
            print("Obrigado por jogar. Até mais!")
            break

        try:
            jogo.escolha_jogador = escolha_jogador
            resultado = jogo.jogar()
            print(resultado)
        except ValueError as e:
            print(e)
