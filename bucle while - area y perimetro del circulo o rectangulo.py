dato = str(input("escriba si desea calcular el perimetro y area, si es un circulo escriba circulo y si es rectangulo escriba rectangulo: "))
while dato!="circulo" or dato!="rectangulo":
    if dato=="circulo":
        pi = 3.1415
        radio = float(input("digite su radio en cm: "))
        area_circulo = pi*(radio**2)
        perimetro_circulo = 2*pi*radio
        print(f"su area es {area_circulo} cm2")
        print(f"su perimetro es {perimetro_circulo} cm")
    elif dato=="rectangulo":
        largo = float(input("digite su base en cm: "))
        ancho = float(input("digite su altura en cm: "))
        area_rectangulo = largo*ancho
        perimetro_rectangulo = 2*largo + 2*ancho
        print(f"su area es {area_rectangulo} cm2")
        print(f"su perimetro es {perimetro_rectangulo} cm")
    print("su dato es erroneo, ingrese su dato nuevamente")
    dato = str(input("escriba si desea calcular el perimetro y area, si es un circulo escriba circulo y si es rectangulo escriba rectangulo: "))
