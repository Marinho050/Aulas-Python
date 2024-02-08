#inserir numeros numa lista
lista = list()

for c in range(0, 5):
    novo_num = int(input(f"Digite o {c+1}º número: "))

    if c == 0 or novo_num > lista[-1]:
        lista.append(novo_num)
        print(f"O número {novo_num} foi adicionado na última posição.")
    else:
        indice = 0

        while indice < len(lista):
            if novo_num <= lista[indice]:
                lista.insert(indice, novo_num)
                print(f"Novo número adicionado na posição {indice + 1}.")
                break

            indice+=1

print("-=" * 30)
print(f"Os valores digitados por ordem são {lista}")
