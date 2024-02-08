#Ex40

'''Crie um programa que gere 5 números aleatórios dentro de um tuple.
Depois mostra a listagem de números gerados, o menor e o maior da lista.'''

from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f"Os números selecionados foram: {tupla}")
maior = menor = tupla[0]

for num in tupla:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"O maior número gerado foi o: {maior}")
print(f"O menor número gerado foi o: {menor}")