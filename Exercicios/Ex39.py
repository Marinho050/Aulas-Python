# Ex039
equipas = ("Real Madrid", "Girona", "Atlético de Madrid", "Barcelona",
                 "Athletic Bilbao", "Real Sociedad", "Betis", "Getafe",
                 "Valencia", "Las Palmas", "Rayo Vallecano", "Osasuna",
                 "Villarreal", "Mallorca", "Alavés", "Sevilla", "Cádiz",
                 "Celta", "Granada", "Almería")

print("Os primeiros 5 classificados são: ")
for c in range(5):
    print(f"{c + 1}º - {equipas[c]}")
print("")

print("Os últimos 4 classificados são: ")
for c in range(1, 5):
    print(f"{20 - c + 1}º - {equipas[-c]}")
print("")

print("Lista de equipas por ordem alfabética: ")
lista_alfabetica = sorted(equipas)
contador = 0
for e in lista_alfabetica:
    print(f"{e} ->", end=" ")
    contador += 1
    if contador == 5:
        print("")
        contador = 0

print("")
print(f"A equipa Las Palmas está na {equipas.index('Las Palmas')+1}ª posição")