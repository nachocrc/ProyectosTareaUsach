#ingrese 3 numeros para ordenarlo de menor a mayor

numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))
numero3 = float(input("ingrese el tercer numero: "))
numero4 = float(input("ingrese el cuarto numero: "))

valores=[numero1, numero2, numero3, numero4]

valores.sort()

print(f"sus valores de menor a mayor son {valores}")
