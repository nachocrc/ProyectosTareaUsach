print("tomaremos los primos dentro del parametro [numero1,numero2]")
num1=int(input("digite su primer numero: "))
num2=int(input("digite su segundo numero: "))
div=2
Lista = []
while num1<=(num2-1):
    num1+=1
    div=2
    while num1>=div :
      if num1%div==0:
          if num1==2:
              Lista.append(num1)
          elif num1!=2:
              break
          break
      elif num1%div!=0 :
          div+=1
      if num1==div:
          Lista.append(num1)
print(f"los primos dentro del parametro son {Lista}")
            
                
    
    
    
