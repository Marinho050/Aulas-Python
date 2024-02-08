#Ex12
print("Vamos iniciar o seu registo")

nome=(input("Ecreva o seu primeiro e ultimo: ")).strip()
indice_espaco= nome.find(" ")

primeira_letra=nome[0].lower()
ultimo_nome=[indice_espaco+ 1].lower()
email=f"{primeira_letra}.{ultimo_nome}.edu@empresa.pt"

print(f"Nome:{nome}")
print(f"Email:{email}")