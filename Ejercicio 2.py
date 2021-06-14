#Escriba un programa que pida un número y a continuación escriba la lista de todos los divisores del número (incluidos el uno y él mismo).

def CalcularDivisores(numero, lista):
  i = 1
  while(i <= numero):
    total = numero % i

    if(total == 0):
      b = str(i)
      lista.append(b)
    
    i += 1
  return lista

# ingreso de datos
numero = int(input("ingrese un numero: "))
ListaDivisores = []

ListaDivisores = CalcularDivisores(numero, ListaDivisores)
print(", ".join(ListaDivisores))
