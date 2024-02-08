#Ex19
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
    print(f"Voce escolheu o {num}")