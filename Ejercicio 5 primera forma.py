#Crear un programa en Python que al recibir una lista elimine los elementos que se encuentran repetidos.
#EJ: [1,a,2,d,3,e,e,1,2,5]  [1,a,2,d,e,5]

def crearLista(numero, lista):
  i = 1
  while(i <= numero):
    valor = input(f"ingrese un valor [{i}]: ")
    lista.append(valor)

    i += 1

  return lista

def EliminarRepetidos(lista):
  i = 0
  while(i < len(lista)):
    objetivo = lista[i]
    j = i + 1
    while(j < len(lista)):
      
      if(lista[j] == objetivo):
        lista.pop(j)
      
      j += 1

    i += 1
  return lista

# Ingreso de datos.
numero = int(input("ingrese el total de elemntos: "))
lista = []

lista = crearLista(numero, lista)
lista = EliminarRepetidos(lista)
print(", ".join(lista))
