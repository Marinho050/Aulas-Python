#Ex28

#Primeira pergunta
print("O primeiro rei de Portugal foi Tiotónio Pais.")
print("[V] / [F]")
resp=input("----->>>").strip().upper()

#loop para ter resposta adquada
while resp not in 'VF':
  print("Por favor digite 'V' para verdadeiro e 'F' para falso")
  resp=input("-------->>>")

  if resp  == 'F':
    print("A sua resposta esta certa")
  elif resp == 'V':
    print("A sua resposta esta errada")