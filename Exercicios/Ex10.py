#Ex10
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
print("Milhar {}".format(m))