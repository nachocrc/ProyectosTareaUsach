#ingrese 2 numeros para ejeutar una operacion

print("Si desea una suma digite 1\nSi desea una resta digite 2\nSi desea una multiplicacion digite 3\nSi desea una división digite 4\nSi desea una exponenciación digite 5")
operacion= int(input("ingrese su operacion: "))
if operacion==1:
    print("en esta operacion se sumarán los numeros")
    num1=float(input("digite su primer numero: "))
    num2=float(input("digite su segundo numero: "))
    suma = num1 + num2
    print(f"su adición es {suma}")
elif operacion==2:
    print("en esta operacion se restarán los numeros en el orden de numero 1 - numero 2")
    num1=float(input("digite su primer numero: "))
    num2=float(input("digite su segundo numero: "))
    resta = num1 - num2
    print(f"su sustracción es {resta}")
elif operacion==3:
    print("en esta operacion se multiplicarán los numeros")
    num1=float(input("digite su primer numero: "))
    num2=float(input("digite su segundo numero: "))
    multiplicación = num1 * num2
    print(f"su multiplicación es {multiplicación}")
elif operacion==4:
    print("en esta operacion se dividirán los numeros")
    num1=float(input("digite su primer numero: "))
    num2=float(input("digite su segundo numero: "))
    división = num1 / num2
    print(f"su división es {división}")
else:
    operacion==5
    print("en esta operacion se hará una exponenciacion de la manera\n(numero 1)^(numero 2)")
    num1=float(input("digite su primer numero: "))
    num2=float(input("digite su segundo numero: "))
    exponente = num1 ** num2
    print(f"su exponenciación es {exponente}")
