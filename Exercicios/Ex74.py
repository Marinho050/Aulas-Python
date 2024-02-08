# Ex74

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


livro1 = Livro("Ola", "Jose Saramago")
livro2 = Livro("Adeus", "Toné")
livro3 = Livro("O amigo", "Quim")

print(f"O titulo do livro é {livro1.titulo} e o seu autor é {livro1.autor}.")
print(f"O titulo do livro é {livro2.titulo} e o seu autor é {livro2.autor}.")
print(f"O titulo do livro é {livro3.titulo} e o seu autor é {livro3.autor}.")

