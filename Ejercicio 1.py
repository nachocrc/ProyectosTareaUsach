# 1. Escriba un programa que permita crear una lista de palabras.
#para ello, el programa tiene que solicitar un numero y a partir de ese numero,
#solicitar esa cantidad de palabras para crear la lista

def AgregarPalabas(numero, lista):

  i = 1
  while(i <= numero):
    palabra = input(f"Ingrese la palabra {i}: ")
    lista.append(palabra)
    i = i + 1
  
  return lista

# ingrese de datos
numeroPalabra = input("ingrese el numero de palabras: ")
numeroPalabra = int(numeroPalabra)

ListaPalabras = []

ListaPalabras = AgregarPalabas(numeroPalabra, ListaPalabras)
print(", ".join(ListaPalabras))
