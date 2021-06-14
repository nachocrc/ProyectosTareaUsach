#Crear un programa en Python que al recibir una lista elimine los elementos que se encuentran repetidos.
#EJ: [1,a,2,d,3,e,e,1,2,5]  [1,a,2,d,e,5]

def EliminarRepetidos(lista):
  i = 0
  while(i < len(lista)):
    
    objetivo = lista[i] # "1"
    j = i + 1
    while(j < len(lista)):
      if(lista[j] == objetivo):
        lista.pop(j)
      
      j += 1

    i += 1
  return lista

# Ingreso de datos.
lista = ["1","a","2","d","3","e","e","1","2","5"]
lista = EliminarRepetidos(lista)
print(", ".join(lista))
