#Ex17
#pedir um  numero ao utilizador
num= int(input("Digite um numero inteiro: "))
#Ler opçao de escolha
print("[ 1 ] - Binario:")
print("[ 2 ]- Octal: ")
print("[ 3 ]- Hexadecimal")
opcao=int(input("Digite a sua opcao:"))
if opcao == 1 :
 print(input(f"O numero{num} Binario é :{bin(num)[2:]}"))
elif opcao == 2 :
    print(input(f"O numero{num} Binario é :{oct(num)[2:]}"))
elif opcao == 3 :
    print(input(f"O numero{num} Binario é :{hex(num)[2:]}"))