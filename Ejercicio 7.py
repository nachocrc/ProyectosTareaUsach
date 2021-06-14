#Escriba un programa en Python que a partir de dos números enteros distintos calcule su división y, si la división es exacta, entregue una lista de los números primos entre ellos. 
print("dividiremos los numeros como numero 1/numero 2")
num1=int(input("digite su primer numero: "))
num2=int(input("digite su segundo numero: "))
Lista = []
c=num1%num2
if c==0:
  while num2<=(num1):
    div=2
    while num2>=div :
      if num2%div==0:
          if num2==2:
              Lista.append(num2)
              num2+=1
          elif num2!=2:
              break
          break
      elif num2%div!=0 :
          div+=1
      if num2==div:
          Lista.append(num2)
    num2+=1
  print("tomaremos los primos dentro del parametro [numero2,numero1]")
  print(f"los primos dentro del parametro son {Lista}")
elif c!=0:
  print("su division no es exacta")
