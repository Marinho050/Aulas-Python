# Ex65

from datetime import datetime


def boas_vindas():
    print("~" * 50)
    print(f"{'Validador de carta de Condução':^50}")
    print("~" * 50)
    print()


def validador_carta(ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    if idade > 18:
        return f"Com {idade} anos, o cidadão pode tirar a carta de condução"
    elif idade < 16:
        return f"Com {idade} anos, o cidadão não pode tirar a carta de condução"
    else:
        return f"Com {idade} anos, o cidadão necessita de autorização para tirar a carta de condução"


boas_vindas()
ano_nascimento = int(input("Digite o ano de nascimento do cidadão: "))
print(validador_carta(ano_nascimento))