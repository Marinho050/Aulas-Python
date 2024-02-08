# Ex52
aluno= dict()

aluno["Nome"]=input("Digite o nome do aluno: ")
aluno["Media"]=int(input("Digite a media do aluno: "))

if aluno["Media"] >= 9.5 :
    print("Aprovado")
else:
    print("Reprovado")

print(aluno.items())