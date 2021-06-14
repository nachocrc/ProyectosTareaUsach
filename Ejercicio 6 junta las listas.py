#Crear un programa en Python que, a partir de dos listas, entregue al usuario una lista con los elementos contenidos en ambas listas

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

def juntarListas(lista1, lista2):
  lista3 = lista1 + lista2
  return lista3

listaA = ["manzana", "roberto"]
listaB = ["sol", "mañana", "manzana"]

listaC = juntarListas(listaA, listaB)
listaC = EliminarRepetidos(listaC)
print(listaC)
