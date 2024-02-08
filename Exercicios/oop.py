'''class Conta:

    def __init__(self, nib, titular, saldo, limite):
        print("A contruir objeto...")
        self.nib = nib
        self.titular = titular
        self.__saldo = saldo  # tributo privadoo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo: {self.__saldo}€")

    def depositar(self, valor):
        self.__saldo += valor

    def levantar(self, valor):
        self.__saldo -= valor

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, valor):
        self.__limite = valor
'''



class Conta:

    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.__saldo = saldo  # tributo privadoo
        self.__limite = limite


    @property
    def saldo(self):
        return f'O saldo da conta é : {self.__saldo}€'


    @saldo.setter
    def saldo(self, valor):
        if valor > 1000:
            print("Valor não autorizado")
        self.__saldo = valor
        print("Saldo modificado com sucesso!")


conta = Conta("Ricardo",)