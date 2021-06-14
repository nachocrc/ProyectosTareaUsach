menu= 'SI'
while menu=='SI':
  palabra = str(input("inserte una palabra: "))

  if 'ñ' not in palabra:
    palabra1 = palabra.upper()
    palabra_en_lista = list(palabra1)

    i = 0

    while i < len(palabra_en_lista) :
      if (palabra_en_lista[i]=='A'):
        palabra_en_lista[i] = '.-'
      else:
        if palabra_en_lista[i] == 'B':
          palabra_en_lista[i] = '-...'
        else:
          if palabra_en_lista[i] == 'C':
            palabra_en_lista[i]= '-.-.'
          else:
            if palabra_en_lista[i] == 'D':
              palabra_en_lista[i] = '-..'
            else:
              if palabra_en_lista[i] == 'E':
                palabra_en_lista[i] = '.'
              else:
                if palabra_en_lista[i] == 'F':
                  palabra_en_lista[i] = '..-.'                 
                else:
                  if palabra_en_lista[i] == 'G':
                    palabra_en_lista[i] = '--.'
                  else:
                    if palabra_en_lista[i] == 'H':
                      palabra_en_lista[i] = '....'
                    else:
                      if palabra_en_lista[i] == 'I':
                        palabra_en_lista[i] = '..'
                      else:
                        if palabra_en_lista[i] == 'J':
                          palabra_en_lista[i] = '.---'
                        else:
                          if palabra_en_lista[i] == 'K':         
                            palabra_en_lista[i] = '-.-'
                          else:
                            if palabra_en_lista[i] == 'L':
                              palabra_en_lista[i] = '.-..'
                            else:
                              if palabra_en_lista[i] == 'M':
                                palabra_en_lista[i] = '--'
                              else:
                                if palabra_en_lista[i] == 'N':
                                  palabra_en_lista[i] = '-.'
                                else:
                                  if palabra_en_lista[i] == 'O':
                                    palabra_en_lista[i] = '---'
                                  else:
                                    if palabra_en_lista[i] == 'P':
                                      palabra_en_lista[i] = '.--.'
                                    else:
                                      if palabra_en_lista[i] == 'Q':
                                        palabra_en_lista[i] = '--.-'
                                      else:
                                        if palabra_en_lista[i] == 'R':
                                          palabra_en_lista[i] = '.-.'
                                        else:
                                          if palabra_en_lista[i] == 'S':
                                            palabra_en_lista[i] = '...'
                                          else:
                                            if palabra_en_lista[i] == 'T':
                                              palabra_en_lista[i] = '-'
                                            else:
                                              if palabra_en_lista[i] == 'U':
                                                palabra_en_lista[i] = '..-'
                                              else:
                                                if palabra_en_lista[i] == 'V':
                                                  palabra_en_lista[i] = '...-'
                                                else:
                                                  if palabra_en_lista[i] == 'W':
                                                    palabra_en_lista[i] = '.--'
                                                  else:
                                                    if palabra_en_lista[i] == 'X':
                                                      palabra_en_lista[i] = '-..-'
                                                    else:
                                                      if palabra_en_lista[i] == 'Y':
                                                        palabra_en_lista[i] = '-.--'
                                                      else:
                                                        if palabra_en_lista[i] == 'Z':
                                                          palabra_en_lista[i] = '--..'
      i +=1

      n = ' '
      alfanumerico = n.join(palabra_en_lista)

    print(f"la palabra {palabra} en codigo morse se escribe como:\n{alfanumerico}")
  
    menu=input("Desea evaluar otra palabra [Si/No]: ")
    menu=menu.upper()

  else:
    while 'ñ' in palabra:
      print("insertaste una palabra con ñ, escriba una sin 'ñ'")
      palabra = str(input("inserte una palabra nuevamente: "))