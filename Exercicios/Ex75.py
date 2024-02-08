# Ex75
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


titulo = input("Digite o titulo do livro: ")
autor = input("Digite o nome do autor: ")

livro = Livro(titulo, autor)

print(f"O titulo do seu livro é {livro.titulo} e o autor {livro.autor}.")
