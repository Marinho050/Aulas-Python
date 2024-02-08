# Ex62

from time import sleep

def pauta(nome, lista_notas):
    print("~" * 30)
    print(f"{f'PAUTA DO ALUNO {nome.upper()}':^30}")
    print("~" * 30)
    sleep(1)
    soma_notas = 0
    for notas in lista_notas:
        soma_notas += notas

    media = soma_notas / len(lista_notas)
    situacao = "Aprovado" if media >= 9.5 else "Reprovado"
    sleep(0.5)
    print(f"\nMédia: {media:.2f}")
    sleep(0.5)
    print(f"Situação: {situacao}")


nome = input("Digite o nome do aluno: ")
notas = list()
contador = 0
while True:
    nota = float(input(f"Digite a {contador + 1}ª nota: "))
    notas.append(nota)
    contador += 1
    opcao = input("Deseja continuar? [S/N]\n---> ").lower().strip()
    if opcao == "n":
        break
pauta(nome, notas)