'''#EX01 - ola mundo
print("Olá mundo")

#EX02- Mensagem de boas vindas
print("-.-.--.-.-.-.-.-.-")
print("-.-""Boas vindas""-.-")
print("-.-.--.-.-.-.-.-.-")

#EX03 - Exibir soma
num1=int (input("Digite um numero :"))
num2= int (input("Digite outro numero :"))
resultado = num1+ num2
print(num1,"+",num2,"=",resultado)

#EX04 - Mostrar sucessor e antecessor

num3=int (input("Escreva um numero :"))
antecessor= num3-1
sucessor=num3+1
print("O antecessor do numero é  :" ,antecessor)
print("O sucessor so numero é : ",sucessor)
'''


'''#Ex05
#Ler numero do utilizador
num1= int (input("Digite um número: "))
num2= int (input("Digite outro número: "))

soma= num1 + num2
subtracao = num1- num2
multiplicacao = num1 * num2
divisao =num1 / num2
resto= num1 %num2

print(num1,"+",num2,"=",soma)
print (num1,"-",num2,"=", subtracao)
print (num1,"*",num2,"=",multiplicacao)
print (num1,"/",num2,"=",divisao)
print (num1,"%",num2,"=",resto)'''

'''#Ex06
#ler os numeros do utilizador
num1 =float (input("Digite Primeiro numero: "))
num2 =float (input("Digite Primeiro numero: "))
num3 =float (input("Digite Primeiro numero: "))
num4 =float (input("Digite Primeiro numero: "))
num5 =float (input("Digite Primeiro numero: "))

#calcular a media
media = (num1+num2+num3+num4+num5)/5

#exibir a media
print("A sua media final é de:",media,"Valores")'''

'''#Ex07
#pedir o ano de nascimento e o ano atual
data_de_nascimento=int (input("Digite a sua data de nascimento: "))
ano_atual=int(input("Digite o ano atual: "))


#calcular a idade
idade= ano_atual-data_de_nascimento

#exibir a idade
print("A sua idade é: ",idade)'''

'''#Ex08

quantidade_dias=int(input("Digite o numero de dias que o carro foi alugado: "))
km=float(input("Digite o numero de km percorridos :"))


preco_km= 0.456
preco_dias=60

total= km * preco_km + quantidade_dias *preco_dias 
print("Estimado cliente, tem a pagar a quantia de  ",total,"€")'''


'''#Ex09
#Pedir o nome do utilixzador

nome= (input("Digite seu nome completo: ")).strip()
print("Estou a avaliar o seu nome... ")

print("O seu nome em maiúsculas é {}",format(nome.upper()))
print("O seu nome em minusculas é:",format(nome.lower()))

print("O seu nome tem {} caracteres",format(len(nome) - nome.count(" ")))

pNome=nome.split()

print("O seu nome é {} e tem {} caracteres".format(pNome[0],len(pNome[0])))'''



'''#Ex10
#pedir numero ao utilizador

num= int(input("Digite um numero inteiro de 0 a 9999: "))

#tratar os dados

u=num//1 % 10
d=num//10 % 10
c=num//100 %10
m=num//1000 % 10


#imprimir no ecra
print("Undidade {}".format(u))
print("Dezena {}".format(d))
print("Centena {}".format(c))
print("Milhar {}".format(m))'''



'''#Ex11

frase= (input("Escreva um a frase: ")).upper().strip()
print("A letra A aparece {} vezes.".format(frase.count("A")))
print("O primeiro A aparece na posição {}.".format(frase.find("A")+1))
print("O primeiro A aparece na posição {}.".format(frase.rfind("A")+1))'''

'''#Ex12
print("Vamos iniciar o seu registo")

nome=(input("Ecreva o seu primeiro e ultimo: ")).strip()
indice_espaco= nome.find(" ")

primeira_letra=nome[0].lower()
ultimo_nome=[indice_espaco+ 1].lower()
email=f"{primeira_letra}.{ultimo_nome}.edu@empresa.pt"  

print(f"Nome:{nome}")
print(f"Email:{email}")'''

'''#Ex13
palavra= "Python"
palavra_invertida= palavra [5] +palavra [4]+palavra [3]+palavra [2]+palavra [1] +palavra [0]
print(palavra_invertida)
print(palavra[::-1])'''

'''#Ex14

velocidade =int(input("========RADAR DE VELOCIDADE======== "))

multa = 100 + 7 * (velocidade - 80)
if velocidade > 80 :
    print("A sua multa é de",multa,"€")

else:
    print("Nao Multado")'''

'''#Ex15
numero=(int(input("Digite um numero: ")))
resto = numero % 2
if resto ==0 :
    print("Numero par")

else:
    print("Numero impar")'''


'''#Ex16
num1=float(input("Digite o primeiro numero: "))
num2=float(input("Digite o segundo numero: "))
num3=float(input("Digite o terceiro numero: "))
num4=float(input("Digite o quarto numero: "))
num5=float(input("Digite o quinto numero: "))

media= (num1 + num2 + num3 + num4 + num5) / 5

if media >= 9.5 :
    print(f"Passou",media)

elif media < 8  :
    print(f"Recuperação",media)

else :
    print(f"Reprova",media)'''

'''#Ex17
#pedir um  numero ao utilizador
num= int(input("Digite um numero inteiro: "))
#Ler opçao de escolha
print("[ 1 ] - Binario:")
print("[ 2 ]- Octal: ")
print("[ 3 ]- Hexadecimal")
opcao=int(input("Digite a sua opcao:"))
if opcao == 1 :
 print(input(f"O numero{num} Binario é :{bin(num)[2:]}"))
elif opcao == 2 :
    print(input(f"O numero{num} Binario é :{oct(num)[2:]}"))
elif opcao == 3 :
    print(input(f"O numero{num} Binario é :{hex(num)[2:]}"))
'''

'''#Ex18
#Pedir numero ao utilizador
num1= int(input("Digite o primeiro numero: "))
num2=int(input("Digite o segundo numero: "))

if num1 > num2 :
    print(f"O numero {num1} é maior que {num2}")

elif num1 <num2 :
    print(f"O numero {num1} é menor que {num2}")

else :
    print(f"Os numeros sao {num1}e {num2} sao iguais")'''

'''#Ex19
#biblioteca de um numero random
import random
numero= random.randrange(start=0 ,stop= 7)
print("Vou pensar num numero de 0 a 7 e tentas adivinhar.")

num=int(input("Em que numero eu pensei?"))
if numero == num :
    print("GANHOUUUU !!!!!!!!!")
    print(f"Eu escolhi o  {numero} ")
    print(f"Voce escolheu o {num}")

else :
    print("UPS !!!!!, Perdeu !!!!")
    print(f"Eu escolhi o  {numero} ")
    print(f"Voce escolheu o {num}")'''

'''#Ex20
import random
import time
#Ler opçao de escolha
print("[ 1 ] - Pedra:")
print("[ 2 ]- Papel: ")
print("[ 3 ]- Tesoura")
numero= random.randrange(start=1 ,stop= 3)
jogada=int(input("Digite a sua opcao:"))
if jogada -numero == 0 :
 print(input(f"Empate"))
elif jogada - numero == -2 :
    print(input(f"Vitoria"))
else :
    print(input(f"Derrota"))'''


'''#for
tentativas= 0
mensagem = "Bem Vindo"
password= "password"

for c in range (0,3):
    entrada = input("Insira a password:")
    if entrada == password:
        print(mensagem)

    else :
        tentativas=tentativas + 1
        print("Tente novamente...\n")

        if tentativas==3:
            print("Utilizador Bloqueado")'''

'''# Ex21
import time
for c in range(0, 10):
    time.sleep(1)
    print(10 - c)

time.sleep(1)
print("Bom Ano Novo !!!!!!!!!")
'''

'''# Ex22
i=0
f=100
for c in range(i, f):
    if c == 0:
        continue
    elif c % 2 ==0:
        print(c)'''

'''# Ex23

num = int(input("Digite um numero para saber a sua tabuada: "))
for c in range(0, 10):
    print(num,"x", c+1, "=", num * (c+1))
'''

'''#Ex24

num=int(input("Digite um numero para verificar se é numero primo: "))
tot=0
for c in range (1, num+1 ):
    if num % c ==0:
        tot= tot+1
if tot > 2:
    print(f"{num} não é um numero primo pois foi divisivel {tot} vezes")
else:
    print(f"{num} é um numero primo pois apenas foi divisivel por {tot} vezes")'''

'''#Ex25
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
'''

'''#Ex26
#importes
from datetime import date
ano_atual= date.today().year

#Iniciar variaveis de controlo
tot_maior=0
tot_menor=0

for pessoa in range (1,8):
    nascimento= int(input(f"Digite em que ano a {pessoa}: "))
    idade = ano_atual - nascimento

    if idade >= 18:
        tot_maior += 1
    else:
        tot_menor += 1
          
# Exibir no ecra os dados
print(f"Ao todo tivemos {tot_maior} pessoas maiores de idade. ")
print(f"Ao todo tivemos {tot_menor} pessoas menores de idade. ")'''

'''#Ex27

#iniciar variaveis de controlo

maior = 0
menor = 0
for pessoa in range (0, 10):
    idade= int(input(f"{pessoa + 1}º pessoa - Digite a sua idade: "))

    if idade == 0 :
      maior = idade
      menor = idade
    else:
        if idade > maior :
            maior = idade
        elif idade < menor:
            menor =idade

print(f"A maior idade encontrada foi: {maior} anos.")
print(f"A menor idade encontrada foi: {menor} anos.")
'''



'''#Ex28

#Primeira pergunta
print("O primeiro rei de Portugal foi Tiotónio Pais.")
print("[V] / [F]")
resp=input("----->>>").strip().upper()

#loop para ter resposta adquada
while resp not in 'VF':
  print("Por favor digite 'V' para verdadeiro e 'F' para falso")
  resp=input("-------->>>")

  if resp  == 'F':
    print("A sua resposta esta certa")
  elif resp == 'V':
    print("A sua resposta esta errada")'''


# EX029
from random import randint
cpu = randint(0, 10)

print("-" * 37)
print("WELCOME TO OUR 'GUESS DE NUMBER' GAME")
print("-" * 37)

coisas = input("Carrega ENTER para iniciar...")

certo = False
palpites = 0

print("\n\nAcabei de pensar num número! Será que consegues adivinhar? :D\n")

while not certo:
    jogador = int(input(f"{palpites + 1}ª - Qual é o teu palpite? ---> "))
    palpites += 1
    if jogador == cpu:
        certo = True
    else:
        if jogador < cpu:
            print("Mais acima...")
        elif jogador > cpu:
            print("Mais abaixo...")

print("BOA!!!!")
print(f"ACERTAS-TE COM APENAS {palpites} TENTATIVAS!!!")