#Ex08

quantidade_dias=int(input("Digite o numero de dias que o carro foi alugado: "))
km=float(input("Digite o numero de km percorridos :"))


preco_km= 0.456
preco_dias=60

total= km * preco_km + quantidade_dias *preco_dias
print("Estimado cliente, tem a pagar a quantia de  ",total,"€")