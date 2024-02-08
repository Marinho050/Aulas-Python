# Ex82

class Produto:
    def __init__(self, nome, quantidade_stock):
        self._nome = nome
        self._quantidade_stock = quantidade_stock

    @property
    def quantidade_stock(self):
        return self._quantidade_stock

    @quantidade_stock.setter
    def quantidade_stock(self, nova_quantidade):
        if nova_quantidade >= 0:
            self._quantidade_stock = nova_quantidade
        else:
            print("Erro: A quantidade em stock não pode ser negativa.")

    def mostrar_stock(self):
        print(f"O produto {self._nome} tem {self._quantidade_stock} unidades em stock.")

    def adicionar_stock(self, quantidade_adicional):
        if quantidade_adicional >= 0:
            self._quantidade_stock += quantidade_adicional
            print(f"Foram adicionadas {quantidade_adicional} unidades ao stock do produto {self._nome}.")
        else:
            print("Erro: A quantidade a adicionar não pode ser negativa.")

# Exemplo de uso da classe
produto1 = Produto(nome="ProdutoA", quantidade_stock=10)
produto1.mostrar_stock()

produto1.adicionar_stock(5)
produto1.mostrar_stock()

produto1.quantidade_stock = 15
produto1.mostrar_stock()

produto1.adicionar_stock(-3)  
produto1.mostrar_stock()
