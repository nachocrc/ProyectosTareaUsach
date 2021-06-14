nombre1=str(input("digite el nombre de la primera persona: "))
edad1=int(input(f"digite el año de nacimiento de forma 'AAAA' de {nombre1}: "))

nombre2=str(input("digite el nombre de la segunda persona: "))
edad2=int(input(f"digite el año de nacimiento de forma 'AAAA' de {nombre2}: "))

if edad1 < edad2 :
    diferencia=edad2-edad1
    print(f"{nombre1} es mayor que {nombre2} por {diferencia} años")
elif edad2 < edad1 :
    diferencia=edad1-edad2
    print(f"{nombre2} es mayor que {nombre1} por {diferencia} años")
else:
    edad1==edad2
    mes1=int(input(f"digite el mes de nacimiento en forma 'MM' de {nombre1}: "))
    mes2=int(input(f"digite el mes de nacimiento en forma 'MM' de {nombre2}: "))
    if mes1 < mes2 :
        meses = mes2-mes1
        print(f"{nombre1} es mayor que {nombre2} por {meses} meses")
    elif mes2 < mes1 :
        meses = mes1-mes2
        print(f"{nombre2} es mayor que {nombre1} por {meses} meses")
    else:
        mes1==mes2
        dia1=int(input(f"digite el dia de nacimiento en forma 'DD' de {nombre1}: "))
        dia2=int(input(f"digite el dia de nacimiento en forma 'DD' de {nombre2}: "))
        if dia1 < dia2 :
            dias = dia2-dia1
            print(f"{nombre1} es mayor que {nombre2} por {dias} dias")
        elif dia2 < dia1 :
            dias = dia1-dia2
            print(f"{nombre2} es mayor que {nombre1} por {dias} dias")

            
#no seguí con horas ni minutos porque me da una real pereza
        
