'''aluno = {"Nome":"Gonçalo","Media":9}
print(f"O aluno {aluno['Nome']} tem a media de {aluno['Media']} valores.")

if aluno["Media"] >=9.5:
    aluno["Situaçao"]= "Aprovado"
else :
    aluno["Situaçao"]="Reprovado"

    print(aluno.items())'''




'''aluno=dict()

aluno["Nome"]=input("Digite o nome do aluno: ")
aluno["Ex001"]=input("Digite a nota do aluno: ")
aluno["Ex002"]=input("Digite a nota do aluno: ")
aluno["Ex003"]=input("Digite a nota do aluno: ")

print(aluno.items())

aluno["Media"]= aluno["Ex001"] + aluno["Ex002"]+ aluno["Ex003"] /3

print(aluno.items())

del aluno["Media"]


print(aluno.items())'''


cidade = {"Nome":"Porto","Codigo":"OPO","Baixa":"Ribeira","Rio":"Douro"}
cidade2 = {"Nome":"Lisboa","Codigo":"Lx","Baixa":"Chiado","Rio":"Tejo"}
pais = list()

pais.append(cidade)
pais.append(cidade2)


for c in range (0, len(pais)):
    print(f"Cidade: {pais[c]['Nome']} -> Registada")
