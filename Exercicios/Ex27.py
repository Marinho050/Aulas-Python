#Ex27

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