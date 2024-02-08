#Ex09
#Pedir o nome do utilixzador

nome= (input("Digite seu nome completo: ")).strip()
print("Estou a avaliar o seu nome... ")

print("O seu nome em maiúsculas é {}",format(nome.upper()))
print("O seu nome em minusculas é:",format(nome.lower()))

print("O seu nome tem {} caracteres",format(len(nome) - nome.count(" ")))

pNome=nome.split()

print("O seu nome é {} e tem {} caracteres".format(pNome[0],len(pNome[0])))