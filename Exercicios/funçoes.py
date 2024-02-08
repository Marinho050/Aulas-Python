'''# import

# definir funções
def insere_linha():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")



# Programa principal
print("Código com prints")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Ola mundo!")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

print()
print("Codigo com funções")
insere_linha()
print("ola mundo")
insere_linha()
'''


'''# import

# definir funções
def cabecalho(msg):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(msg)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



cabecalho("Olá mundo!")
cabecalho("Olá turma!")
cabecalho("Coisas")'''



# import

# definir funções
def cabecalho(msg):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(msg)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def soma(a,b):
    s = a + b
    print(f"A soma entre {a} e {b} é igual a {s} ")


def conta_numeros(*num):
    print(f"Inseriu {len(num)} numeros")
    for numeros in num:
        print(f"{numeros}", end="")
        print()


# programa principal
cabecalho("Mundo das Funções!")
print("Função soma")
soma(2,5)
soma(4,4)
soma(13,15)
print()
print("Função Desempacotar")
conta_numeros(1,2,3,4,5,6)
conta_numeros(1,3,5)
conta_numeros(1,2,3,4,5,6,7,8,9)