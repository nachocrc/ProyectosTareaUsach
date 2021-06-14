menu="SI"
while menu=="SI":
    #ENTRADA
    texto= input("\nIngrese palabra a evaluar: ")
    texto=texto.lower()

    #PROCESAMIENTO

    i=0
    largo=len(texto)
    j=largo-1
    exito=0
    while i<largo:
        if texto[i]==texto[j]:
            #exito+=1
            exito=exito+1
            i=i+1
            j=j-1
        else:
            i=i+1
            j=j-1

    #SALIDA

    if exito==largo:
        print("\nLa palabra ingresada es Palíndroma!")
    else:
        print("\nLa palabra ingresada  NO es Palíndroma!")

    menu=input("Desea evaluar otra palabra [Si/No]: ")
    menu=menu.upper()