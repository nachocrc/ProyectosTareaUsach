#. Crear un programa en Python que a partir de una lista (puede ser creada por el usuario) de “n” elementos, se entregue el elemento que más se repite e indique cuantas veces se repitió. NO UTILIZAR METODO MAX NI MIN, NI METODO .COUNT()

def crearLista(numero, lista):
  i = 1
  while(i <= numero):
    valor = input(f"ingrese un valor [{i}]: ")
    lista.append(valor)

    i += 1


  return lista

def contarElementos(lista, elemento, indice):
  repeticiones = 1

  i = 0
  while(i < len(lista)):
    
    if(lista[i] == elemento and i != indice):
      repeticiones += 1
    i +=1

  return repeticiones

def contadorElementos(lista):
  i = 0
  
  while(i < len(lista)):
    if(i == 0):
      mayor = contarElementos(lista, lista[i], i)
      elementoMayor = lista[i]
    
    temporal = contarElementos(lista, lista[i], i)
    temporalMayor = lista[i]

    if(temporal > mayor):
      mayor = temporal
      elementoMayor = temporalMayor

    i +=1
  
  print(f"el elemento se repitio {mayor}, {elementoMayor}")
  

elemento = int(input("Ingrese la cantidad de elementos: "))
listaElementos = []
listaElementos = crearLista(elemento, listaElementos)
contadorElementos(listaElementos)
