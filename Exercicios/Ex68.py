# Ex68

from time import sleep


def boas_vindas():
    print("~" * 30)
    print(f"{'SISTEMA DE AVALIAÇÃO DA TURMA':^30}")
    print("~" * 30)


def sit_turma(lista):
    maior = soma = situacao = cont = 0
    for nota in lista:
        if cont == 0:
            maior = nota
        else:
            if nota > maior:
                maior = nota
        soma += nota
        cont += 1
    media = soma / len(lista)
    if media > 12:
        situacao = "Boa"
    elif media < 9.5:
        situacao = "Fraca"
    else:
        situacao = "Razoável"
    return {"maior nota": maior, "Média": media, "Situação": situacao}


notas = [10, 12, 7, 9, 8, 10]
avaliacao = sit_turma(notas)
boas_vindas()
sleep(1)
for c, k in avaliacao.items():
    if c == "Média":
        print(f"A {c} é {k:.2f}")
        sleep(0.5)
    else:
        print(f"A {c} é {k}")
        sleep(0.5)