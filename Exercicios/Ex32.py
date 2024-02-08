# Ex032
print("-" * 22)
print("Sequência de Fibonacci")
print("-" * 22)

n = int(input("Quantos elementos que mostrar?\n---> "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Por favor, insira um número positivo.")
elif n == 1:
    print("Sequência de Fibonacci até", n, ":")
    print(a)
else:
    print("Sequência de Fibonacci:")
    while count < n:
        print(a, end=' ~ ')
        nth = a + b
        # atualizando os valores
        a = b
        b = nth
        count += 1
print("FIM")
