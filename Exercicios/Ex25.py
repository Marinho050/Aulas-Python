#Ex25
frase = input("Introduza uma frase: ").strip().upper()
palavras = frase.split()
juntas = "" .join(palavras)
inverso= juntas[::-1]
if juntas == inverso:
    print("A palavra é um palíndromo.")
else :
    print("A palavra não é um polídromo")
print(juntas)
print(inverso)