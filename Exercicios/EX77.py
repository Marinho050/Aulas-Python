# Ex77
class ContaBancaria:
    def __init__(self, titular, saldo_inicial, limite):
        self.titular = titular
        self.saldo = saldo_inicial
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de €{valor} realizado. Novo saldo: €{self.saldo}')

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f'Levantamento de €{valor} realizado. Novo saldo: €{self.saldo}')
        else:
            print('Saldo insuficiente.')

# Exemplo de uso
conta = ContaBancaria("João", 1000, 500)
conta.depositar(200)
conta.sacar(1500)

