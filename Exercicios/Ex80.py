class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        else:
            return 0

    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 7.0:
            return "Aprovado"
        else:
            return "Reprovado"

# Exemplo de uso da classe Aluno
nome_aluno = "João"
notas_aluno = [8.5, 7.0, 6.5, 9.0]
aluno_joao = Aluno(nome_aluno, notas_aluno)

media_joao = aluno_joao.calcular_media()
situacao_joao = aluno_joao.verificar_situacao()

print(f"Aluno: {aluno_joao.nome}")
print(f"Notas: {aluno_joao.notas}")
print(f"Média: {media_joao}")
print(f"Situação: {situacao_joao}")
