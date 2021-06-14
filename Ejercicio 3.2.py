menu="SI"
while menu=="SI":
    texto= input("Ingrese palabra a evaluar: ")
    texto=texto.lower()
    texto = texto.replace(" ", "")
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

    if exito==largo:
        print("\nLa palabra ingresada es Palíndroma!")
    else:
        print("\nLa palabra ingresada  NO es Palíndroma!")

    menu=input("Desea evaluar otra palabra [Si/No]: ")
    menu=menu.upper()