texto = input("escriba un texto:\n ")
texto_nuevo = texto.split()
palabra_escogida = str(input("ingrese palabra para ver cuantas veces se repite: "))
nuevo = texto.count(palabra_escogida)
print(f"la {palabra_escogida} aparece {nuevo} en el texto")