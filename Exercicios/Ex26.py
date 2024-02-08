# Ex26
# importes
from datetime import date

ano_atual = date.today().year

# Iniciar variaveis de controlo
tot_maior = 0
tot_menor = 0

for pessoa in range(1, 8):
    nascimento = int(input(f"Digite em que ano a {pessoa}: "))
    idade = ano_atual - nascimento

    if idade >= 18:
        tot_maior += 1
    else:
        tot_menor += 1

# Exibir no ecra os dados
print(f"Ao todo tivemos {tot_maior} pessoas maiores de idade. ")
print(f"Ao todo tivemos {tot_menor} pessoas menores de idade. ")