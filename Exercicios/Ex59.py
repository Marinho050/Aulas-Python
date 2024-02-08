# Ex59
def centralizar_texto(texto, largura_linha):
    espacos_total = largura_linha - len(texto)
    espacos_esquerda = espacos_total // 2
    texto_centralizado = ' ' * espacos_esquerda + texto
    print('~' * largura_linha)  # Linha superior de tils
    print(texto_centralizado)
    print('~' * largura_linha)  # Linha inferior de tils

texto = input("Digite o seu texto: ")

# Calcula a largura da linha com base no comprimento do texto

largura_linha = len(texto) + 4  # Adicionando 4 para espaços em ambos os lados

centralizar_texto(texto, largura_linha)
