menu="SI"

while menu=='SI':
  texto = str(input("inserte una frase o cadena de texto: "))
  texto = texto.split()

  palabra_insertada = str(input("digite la palabra que cambiara:\n"))
  palabra_a_cambiar = str(input("digite la palabra por la cual cambiara la primera:\n"))

  a = texto.index(palabra_insertada)
  texto[a] = palabra_a_cambiar

  n = ' '
  texto_nuevo = n.join(texto)
  print(texto_nuevo)

  menu=input("Desea evaluar otra palabra [Si/No]: ")
  menu=menu.upper()