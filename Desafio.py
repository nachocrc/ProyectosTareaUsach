# [Pregunta PEP] Construya un programa en Python que, dadas dos listas A y B, revise si la B es una lista “pseudovalente” de A. Diremos que una lista es pseudovalente de otra, si contiene todos los elementos de la otra al cuadrado, sin importar el orden. 
#Por ejemplo:  En este caso, las listas A y B son pseudovalentes, pues para cada elemento de a, existe una versión “pseudovalente” en B 
# A = [11, 5, 2, 4, 9, 5, 11] #7
# B = [25, 16, 4, 81, 121, 25, 121] # 7
# En este caso, las listas A y B no son pseudovalentes, pues existe un elemento en A que no tiene su par “pseudovalente” en B
# A = [11, 5, 2, 4, 9, 5, 11] # 7
# B = [16, 4, 81, 121, 25, 121] # 6
#  En este caso, las listas A y B no son pseudovalentes, pues existe un elemento en B que no tiene su par “pseudovalente” en A
# A = [11, 5, 2, 4, 9, 5, 11] # 7
# B = [25, 81, 16, 4, 81, 121, 25, 121] # 8
# La función deberá retornar un booleano, indicando si la condición para que las listas sean “pseudovalentes” se cumple o no.
# RESTRICCIÓN: No se pueden utilizar métodos o funciones para obtener máximos, mínimos, u ordenar listas.
 
# A[1,2,3] -> [1,4,9]
# B[1,4,9]
# i = 0
#pseudovalente  = [A[i]*2,A[i + 1]2,A[i + 2]*2] and len(A) == len(B)

def CalcularSeudovalente(lista):
  listaSeudovalente = []

  i = 0
  while(i < len(lista)):
    listaSeudovalente.append(lista[i]**2)
    i += 1

  print(listaSeudovalente)
  return listaSeudovalente

def compararElemntos(lista, listaSeudovalente):
  contadorIndice = 0
  i = 0
  while(i < len(listaSeudovalente)):
    contador = lista.count(listaSeudovalente[i])
    if(contador >= 1):
      contadorIndice +=1
      
    
    

    i+=1
  if(contadorIndice == len(listaSeudovalente) and len(lista) == len(listaSeudovalente)):
    comprobacion = True
  else:
    comprobacion = False

  return comprobacion

def compararSeudovalente(lista1, lista2):
  
  if(lista1 == lista2 and len(lista1) == len(lista2)):
    verificacion = True
  
  else: 
    verificacion = compararElemntos(lista1, lista2)

  return verificacion

listaA = [11, 5, 2, 4, 9, 5, 11]
listaB = [25, 16, 4, 81, 121, 25, 121]

resultado = compararSeudovalente(listaB, CalcularSeudovalente(listaA))

if(resultado == True):
  print("Las listas son seudovalentes")
elif(resultado != True):
  print("Las listas no son seudovalentes")
