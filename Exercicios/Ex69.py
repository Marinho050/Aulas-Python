# Ex69

def calcula_imc(altura, peso):
    imc = peso / (altura * altura)
    if imc < 18.5:
        return f"Com IMC de {imc:.2f} você está abaixo do peso."
    elif imc <= 18.5 and imc <= 24.9:
        return f"Com IMC de {imc:.2f} você está com o peso normal."
    elif imc <= 25 and imc <= 29.9:
        return f"Com IMC de {imc:.2f} você está com o sobrepeso."
    elif imc <= 30 and imc <= 34.9:
        return f"Com IMC de {imc:.2f} você está com o Obesidade grau 1."
    elif imc <= 35 and imc <= 39.9:
        return f"Com IMC de {imc:.2f} você está com o Obesidade grau 2."
    else:
        return f"Com IMC de {imc:.2f} você está com o Obesidade grau 3 (obesidade mórbida)."



#print(calcula_imc(1.70, 68))
num = 1.75
print(type(num))
if type(num) == float:
    numero = str(num)
    posicao = numero.find(".")
    numero[posicao].replace(".", " ")
    print(numero)
    print(posicao)