# Ex83
class ContaBancaria:
    def __init__(self, titular, saldo_inicial, limite):
        self._titular = titular
        self._saldo = saldo_inicial
        self._limite = limite

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @property
    def saldo_disponivel(self):
        return self._saldo + self._limite

    @titular.setter
    def titular(self, novo_titular):
        self._titular = novo_titular

    @limite.setter
    def limite(self, novo_limite):
        self._limite = novo_limite

    def depositar(self, valor):
        self._saldo += valor
        print(f'Depósito de €{valor} realizado. Novo saldo: €{self._saldo}')

    def sacar(self, valor):
        if valor <= self.saldo_disponivel:
            self._saldo -= valor
            print(f'Levantamento de €{valor} realizado. Novo saldo: €{self._saldo}')
        else:
            print('Operação interronpida. Saldo insuficiente.')

# Exemplo de uso
conta = ContaBancaria("João", 1000, 500)
conta.depositar(200)
conta.sacar(1500)
