# Ex76

class Produto:
    def __init__(self, nome, quantidade_em_stock):
        self.nome = nome
        self.quantidade_em_stock = quantidade_em_stock

    def mostrar_stock(self):
        print(f"O produto {self.nome} tem {self.quantidade_em_stock} unidades em stock.")

    def aumentar_stock(self, quantidade):
        self.quantidade_em_stock += quantidade
        print(f"Adicionadas {quantidade} unidades ao stock. Novo total: {self.quantidade_em_stock}")


produto1 = Produto("Camiseta", 50)
produto1.mostrar_stock()

produto1.aumentar_stock(30)
produto1.mostrar_stock()
