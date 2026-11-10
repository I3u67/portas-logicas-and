print("AND | Determine o valor das portas com: 0 ou 1")
positivo = int(1)
negativo = int(0)

print("Há 2 portas, cada uma com 2 entradas, que vão até uma porta final que reage a saída das duas portas")
Aporta1 = int(input("1° Valor da Porta A: "))
if Aporta1 in ['1', '0']:
  if Aporta1 == "1":
    Aporta1 = positivo
  elif Aporta1 == "0":
    Aporta1 = negativo
else:
  print("Valor inválido")

Aporta2 = int(input("2° Valor da Porta A: "))
if Aporta2 in ['1', '0']:
  if Aporta2 == "1":
    Aporta2 = positivo
  elif Aporta2 == "0":
    Aporta2 = negativo
else:
  print("Valor inválido")

print(f"A |1° ENTRADA: {Aporta1}" )
print(f"A |2° ENTRADA: {Aporta2}")
if Aporta1 == positivo and Aporta2 == positivo:
  Asaida = positivo
else:
  Asaida = negativo
print(f"A |SAÍDA: {Asaida}")

print("Agora defina os valores da Porta B")

Bporta1 = int(input("1° Valor da Porta B: "))
if Bporta1 in ['1', '0']:
  if Bporta1 == "1":
    Bporta1 = positivo
  elif Bporta1 == "0":
    Bporta1 = negativo
else:
  print("Valor inválido")

Bporta2 = int(input("2° Valor da Porta B: "))
if Bporta2 in ['1', '0']:
  if Bporta2 == "1":
    Bporta2 = positivo
  elif Bporta2 == "0":
    Bporta2 = negativo
  else:
    print("Valor Inválido")

print(" ")
print(f"B |1° ENTRADA: {Bporta1}" )
print(f"B |2° ENTRADA: {Bporta2}")
if Bporta1 == positivo and Bporta2 == positivo:
  Bsaida = positivo
else:
  Bsaida = negativo
print(f"A |SAÍDA: {Bsaida}")

print(" ")
print("Agora as saídas A e B irão até as 2 entradas da saída C, que reagirá com 1 ou 0 (Ligado ou Desligago)")
if Asaida == positivo and Bsaida == positivo:
  Csaida = positivo
  print(f"SAÍDA FINAL: {Csaida}")
  print("Aparelho ligado!")
else:
  Csaida = negativo
  print(f"SAÍDA FINAL: {Csaida}")
  print("Aparelho desligado!")
