#Crear un programa en Python que, a partir de dos listas, entregue al usuario una lista con los elementos contenidos en ambas listas.
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

def interseccion(lista):
  i = 0
  listaTemporal = []
  
  while(i < len(lista)):
    
    objetivo = lista[i]
    valor = lista.count(objetivo)
    
    if(valor == 1):
      lista.pop(i)
    elif(valor > 1):
      valor2 = listaTemporal.count(objetivo)
     
      if(valor2 == 0):
        listaTemporal.append(objetivo)

    i += 1
    
  return listaTemporal


listaA = ["manolo", "roberto", "javier", "javier", "jordan"]
listaB = ["roberto", "jordan", "jose"]

listaC = EliminarRepetidos(listaA) + EliminarRepetidos(listaB) 
# ["manolo", "roberto", "javier", "javier", "roberto", "jordan", "jose", "javier"]

listaC = interseccion(listaC)
print(listaC)
