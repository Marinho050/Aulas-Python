# Ex81
class Livro:
    def __init__(self, titulo, ano, autor, disponibilidade=True):
        self._titulo = titulo
        self._ano = ano
        self._autor = autor
        self._disponibilidade = disponibilidade

    @property
    def titulo(self):
        return self._titulo

    @property
    def ano(self):
        return self._ano

    @property
    def autor(self):
        return self._autor

    @property
    def disponibilidade(self):
        return self._disponibilidade

    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo

    @ano.setter
    def ano(self, novo_ano):
        self._ano = novo_ano

    @autor.setter
    def autor(self, novo_autor):
        self._autor = novo_autor

    @disponibilidade.setter
    def disponibilidade(self, nova_disponibilidade):
        self._disponibilidade = nova_disponibilidade

# Exemplo de uso
livro_exemplo = Livro("Python for Beginners", 2020, "John Doe")
print(f"Título: {livro_exemplo.titulo}")
print(f"Ano: {livro_exemplo.ano}")
print(f"Autor: {livro_exemplo.autor}")
print(f"Disponibilidade: {livro_exemplo.disponibilidade}")

# Alterando o título e verificando novamente
livro_exemplo.titulo = "Python for Everyone"
print(f"Novo Título: {livro_exemplo.titulo}")
