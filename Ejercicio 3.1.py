#ingrese 3 numeros para ordenarlo de mayor a menor

numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))
numero3 = float(input("ingrese el tercer numero: "))

valores=[numero1, numero2, numero3]

valores.sort(reverse=True)

print(f"sus valores de menor a mayor son {valores}")
