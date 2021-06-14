# Crear un programa en Python que a partir de una lista (puede ser creada por el usuario) de “n” elementos, se entregue el elemento que más se repite e indique cuantas veces se repitió.

def crearLista(numero, lista):
  i = 1
  while(i <= numero):
    valor = input(f"ingrese un valor [{i}]: ")
    lista.append(valor)

    i += 1

  print(", ".join(lista))
  return lista

def contadorElementos(lista):
  i = 0

  while(i < len(lista)):
    if(i == 0):
      mayor = lista.count(lista[i])
      elementoMayor = lista[i]
    
    temporal = lista.count(lista[i])
    temporalMayor = lista[i]

    if(temporal > mayor):
      mayor = temporal
      elementoMayor = temporalMayor

    i +=1
  
  print(f"el elemento {elementoMayor}, se repite {mayor} veces")
  

elemento = int(input("Ingrese la cantidad de elementos: "))
listaElementos = []
listaElementos = crearLista(elemento, listaElementos)
contadorElementos(listaElementos)
