#Ex11

frase= (input("Escreva um a frase: ")).upper().strip()
print("A letra A aparece {} vezes.".format(frase.count("A")))
print("O primeiro A aparece na posição {}.".format(frase.find("A")+1))
print("O primeiro A aparece na posição {}.".format(frase.rfind("A")+1))