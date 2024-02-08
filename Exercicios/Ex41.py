# Ex41

'''Crie um programa que leia 4 valores e guarde-os num tuple. No final exiba:

Quantas vezes aparecer o número 7.
Em que posição foi digitado o número 5.
Quais são os números pares.

O programa deve informar quando não encontrar resposta.'''

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))
d = int(input("Digite um último número: "))

tupla = (a, b, c, d)

#número 7
cont_7 = 0
for num in tupla:
    if num == 7:
        cont_7+=1

if cont_7 == 0:
    print("O número 7 não aparece nenhuma vez.")
else:
    print(f"O número 7 apareceu {cont_7} vezes.")

#número 5
if 5 in tupla:
    print(f"O número 5 está na posição {tupla.index(5)+1}.")
else:
    print("O 5 não aparece nenhuma vez.")

# numeros pares
controlo_pares = 0
for num in tupla:
    if num % 2 == 0:
        if num == tupla[0]:
            print("Os números pares são: ", end=" -> ")
        print(num, end=" -> ")
    else:
        controlo_pares += 1

    if controlo_pares == 4:
        print("Não há números pares disponíveis.")