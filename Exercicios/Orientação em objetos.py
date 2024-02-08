'''class Jogo:
    def __init__(self, titulo, consola, preco):
        self.titulo = titulo
        self.consola = consola
        self.preco = preco

jogo = Jogo("Palworld", "PC", 29.90)

print(jogo.titulo)
print(jogo.consola)
print(jogo.preco)
'''


class Conta:
    def __init__(self, identidade, titular, saldo, limite):
        self.identidade = identidade
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def levantar(self, valor):
        if valor > self.limite:
            print("O seu limite é de 400.00€ diários.")
        else:
            if self.saldo > valor:
                self.saldo -= valor

    def depoisitar(self, valor):
        self.saldo -= valor

    def estrato(self):
        print(f"A conta {self.identidade} tem {self.saldo}€ disponiveis.")


