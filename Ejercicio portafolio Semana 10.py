#Se cargan las funciones

# corregiremos si es un numero distinto de un natural
def RevisarNumero(numero):
  dato=numero
  while ('.' in dato) or ('-' in dato): 
    if '.' in dato:
      print("ingresaste un decimal")
      dato=str(input("vuelva a ingresar su numero correctamente: "))
    elif '-' in dato:
      print("ingresaste un entero negativo")
      dato=str(input("vuelva a ingresar su numero correctamente: "))

  dato=int(dato)
  return dato

# se crea la función de los primos hasta n
def FunciónPrimos(lista):
  Lista=[]
  Constante=2
  while Constante<=(número):
    dos=2
    tres=3
    cinco=5
    siete=7
    nueve=9

    if Constante%dos==0:
      if Constante==2:
        variable=str(Constante)
        Lista.append(variable)
        Constante=Constante+1
      elif Constante!=2:
        Constante+=1

    elif (Constante%tres)==0:
      if Constante==3:
        variable = str(Constante)
        Lista.append(variable)
        Constante+=1
      elif Constante!=3:
        Constante=Constante+1   

    elif (Constante%cinco)==0:
      if Constante==5:
        variable = str(Constante)
        Lista.append(variable)
        Constante+=1
      elif Constante!=5:
        Constante+=1

    elif (Constante%siete)==0:
      if Constante==7:
        variable = str(Constante)
        Lista.append(variable)
        Constante+=1
      elif Constante!=7:
        Constante+=1

    elif (Constante%9)==0:
      if Constante==9:
        variable = str(Constante)
        Lista.append(variable)
        Constante=Constante+1
      elif Constante!=9:
        Constante=Constante+1

    else:
        variable = str(Constante)
        Lista.append(variable)
        Constante+=1

  return Lista

# se crea la funcion primeros n primos
def PrimerosPrimos(lista):
  constante = 1
  Constante=2

  #Se crea una lista solo para len
  lista=[]
  while constante<=número:
    lista.append(constante)
    constante+=1
  #Se cran los primeros n primos

  Lista=[]

  while len(Lista)<=(len(lista)-1):
    dos=2
    tres=3
    cinco=5
    siete=7
    nueve=9

    if Constante%dos==0:
      if Constante==2:
        variable=str(Constante)
        Lista.append(variable)
        Constante=Constante+1
      elif Constante!=2:
        Constante+=1

    elif (Constante%tres)==0:
      if Constante==3:
        variable = str(Constante)
        Lista.append(variable)
        Constante+=1
      elif Constante!=3:
        Constante=Constante+1   

    elif (Constante%cinco)==0:
      if Constante==5:
        variable = str(Constante)
        Lista.append(variable)
        Constante+=1
      elif Constante!=5:
        Constante+=1

    elif (Constante%siete)==0:
      if Constante==7:
        variable = str(Constante)
        Lista.append(variable)
        Constante+=1
      elif Constante!=7:
        Constante+=1

    elif (Constante%9)==0:
      if Constante==9:
        variable = str(Constante)
        Lista.append(variable)
        Constante=Constante+1
      elif Constante!=9:
        Constante=Constante+1

    else:
        variable = str(Constante)
        Lista.append(variable)
        Constante+=1

  return Lista

# se crea la funcion para descomponer el numero en primos
def multiplos(lista):
  lista1=[]
  const=número
  i=0
  while const>1:
    if (const%(int(Primeros_n_primos[i])))==0:
      lista1.append(str(Primeros_n_primos[i]))
      const=const/(int(Primeros_n_primos[i]))
    elif (const%(int(Primeros_n_primos[i])))!=0:
      i+=1
  return lista1

# Se ingresa el dato
numero = str(input("ingrese un número entero positivo: "))
número = RevisarNumero(numero)

# Se trabaja la constante para las listas
Separador = ", "
separar= "*"

#Se trabaja los primos hasta n para dejarlos presentables con una Constante
primos = FunciónPrimos(número)
Número_Primo_Trabajado = Separador.join(primos)

#Se trabaja los primeros n primos para dejarlos presentables con una Constante
Primeros_n_primos = PrimerosPrimos(número)
PrimerosPrimosN = Separador.join(Primeros_n_primos)

#Se trabaja los multiplos
descomponer = multiplos(número)
multiplo = separar.join(descomponer)

#Se imprime la función
print(f"\npara el valor n = {número}:")
print(f"\nlos numeros primos hasta {número}, son: {Número_Primo_Trabajado}")
print(f"\nlos primeros {número} numeros primos son: {PrimerosPrimosN}")
print(f"\nEl número {número} en factores primos puede descomponerse como: {multiplo}")