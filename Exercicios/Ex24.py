#Ex24

num=int(input("Digite um numero para verificar se é numero primo: "))
tot=0
for c in range (1, num+1 ):
    if num % c ==0:
        tot= tot+1
if tot > 2:
    print(f"{num} não é um numero primo pois foi divisivel {tot} vezes")
else:
    print(f"{num} é um numero primo pois apenas foi divisivel por {tot} vezes")