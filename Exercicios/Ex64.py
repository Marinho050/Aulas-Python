# Ex64
def conversor(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"Em celsius: {celsius}º")
    print(f"Em fahrenheit: {fahrenheit}º")

print(f"~"*50)
print(f"{'CONVERSOR DE CELSIUS PARA FAHRENHEIT':^50}")
print(f"~"*50)
graus = float(input("Digite a temperatura em Celsius: "))
conversor(graus)