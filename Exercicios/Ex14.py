#Ex14

velocidade =int(input("========RADAR DE VELOCIDADE======== "))

multa = 100 + 7 * (velocidade - 80)
if velocidade > 80 :
    print("A sua multa é de",multa,"€")

else:
    print("Nao Multado")