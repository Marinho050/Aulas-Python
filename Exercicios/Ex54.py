# Ex54
from datetime import datetime
from time import sleep
ano_atual = datetime.now().year

simulacao = dict()

simulacao["Nome"] = input("Digite o nome do Cliente: ")
simulacao["Ano de Nascimento"] = int(input("Ano de nascimento: "))
simulacao["Idade"] = ano_atual - simulacao["Ano de Nascimento"]
del simulacao["Ano de Nascimento"]
simulacao["Rendimentos mensais"] = float(input("Rendimentos mensais: "))
simulacao["Despesas mensais"] = float(input("Despesas mensais: "))
simulacao["Remanescente"] = simulacao["Rendimentos mensais"] - simulacao["Despesas mensais"]
simulacao["Montante do crédito"] = int(input("Montante do Crédito: "))
simulacao["Prazo"] = int(input("Prazo em anos: "))
simulacao["Valor mensal"] = simulacao["Montante do crédito"] / (simulacao["Prazo"] * 12)

sleep(1)
print("=-"*10)
print("A analisar", end="")
for c in range(0, 3):
    sleep(1)
    print(".", end="")
print()
print("=-"*10)

for k, v in simulacao.items():
    sleep(1)
    if k == "Idade" or k == "Prazo":
        print(f"{k}: {v} anos")
    elif k in ["Rendimentos mensais", "Despesas mensais", "Remanescente", "Montante do crédito", "Valor mensal"]:
        print(f"{k}: {v:.2f}€")
    else:
        print(f"{k}: {v}")

for c in range(0, 10):
    print(".", end="")
    sleep(0.3)
print()
simulacao["Resposta"] = "Aprovado" if simulacao["Valor mensal"] < simulacao["Remanescente"] else "Reprovado"
sleep(1)
print(f"Crédito {simulacao['Resposta']}")
