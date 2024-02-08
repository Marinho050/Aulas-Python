# Ex60
from time import sleep



def contador (inicio, fim, passo):
    if passo < 0 :
        passo *= 1
    if passo == 0 :
        passo=1
        print(f"Contagem de {inicio} ate {fim} de {passo} em {passo}")
        sleep(1)

    cont = inicio

    if inicio < fim :
        while cont <= fim:
            print(f"{cont}", end=" ")
            cont += passo
            sleep(0.3)
        print("FIM!")

    else:
        while cont >= fim :
            print(f"{cont}",end=" ")
            cont-=passo
            sleep(0.3)
        print("FIM!")


contador (1,20,2)
contador(10, 0,1)
print()
print("Chegou a hora de personalizar a contagam!")
i=int(input("Inicio: "))
f=int(input("Fim: "))
p=int(input("Passo: "))
contador(i,f,p)
