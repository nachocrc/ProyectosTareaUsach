#calcular geometria
import math 
figura = str(input("va a calcular el area y perimetro de la siguiente figura geometrica, escoja una\ncirculo, cuadrado, triangulo rectangulo y rectangulo\ny anote su nombre para escojerla: "))
while figura!="circulo" or figura!="cuadrado" or figura!="triangulo rectangulo" or figura!="triangulo":
    if figura=="circulo":
        pi=3.1415
        radio=float(input("digite su radio: "))
        P=2*pi*radio
        A=pi*(radio**2)
        print(f"su area es {A} cm2 y su perimetro es {P} cm")
    elif figura=="cuadrado":
        b=float(input("digite su base: "))
        a=float(input("digite su altura: "))
        P=2*b + 2*a
        A=b*a
        print(f"su area es {A} cm2 y su perimetro es {P} cm")
    elif figura=="circulo":
        b=float(input("digite su base: "))
        b=float(input("digite su altura: "))
        c=float(input("digite su hipotenusa: "))
        P=a+b+c
        A=(b*a)/2
        print(f"su area es {A} cm2 y su perimetro es {P} cm")
    elif figura=="triangulo":
        a=float(input("digite su lado 1: "))
        b=float(input("digite su lado 2: "))
        c=float(input("digite su base: "))
        #calculamos el semi perimetro de la figura como SP y calculamos el aréa por la formula de herón
        P=a+b+c
        SP=(a+b+c)/2
        A= math.sqrt((SP)*(SP-a)*(SP-b)*(SP-c))
        print(f"su area es {A} cm2 y su perimetro es {P} cm")
    print("error, escoja bien su figura")
    figura = str(input("va a calcular el area y perimetro de la siguiente figura geometrica, escoja una\ncirculo, cuadrado, triangulo rectangulo y rectangulo\ny anote su nombre para escojerla: "))
    
