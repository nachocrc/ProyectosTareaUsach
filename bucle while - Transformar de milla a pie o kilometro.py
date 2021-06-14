#transformar de milla a pie y milla a km
trf = str(input("si pasará de milla a pie, escriba pie. si desea pasar de millas a kilometro, escriba kilometro\n: "))
while trf!="pie" or trf!="kilometro":
    if trf=="pie":
        milla_a_pie = 5280
        milla=float(input("cuantas millas a va transformar: "))
        milla_pie = milla*milla_a_pie
        print(f"las {milla} mi's son {milla_pie} foot's")
    elif trf=="kilometro":
        milla_a_kilometro = 1609
        milla=float(input("cuantas millas a va transformar: "))
        milla_km = milla*milla_a_kilometro
        print(f"las {milla} mi's son {milla_km} km's")
    print("dato erroneo, digite nuevamente su dato")
    trf = str(input("si pasará de milla a pie escriba pie, si desea pasar de millas a kilometro escriba km\n: "))
