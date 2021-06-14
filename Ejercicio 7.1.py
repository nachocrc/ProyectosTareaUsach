texto = input("inserte una palabra: ")
i = 0
while i<len(texto):
  nuevo = texto[:(i)] + texto[i].swapcase() + texto[(i+1):]
  print(nuevo)
  i += 1