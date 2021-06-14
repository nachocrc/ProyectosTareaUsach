palabra = str(input("inserte una palabra: "))
palabra1 = palabra.upper()
palabra_en_lista = list(palabra1)

i = 0

while i < len(palabra_en_lista):
  if (palabra_en_lista[i]=='A'):
    palabra_en_lista[i] = '1'
  else:
    if palabra_en_lista[i] == 'B':
      palabra_en_lista[i] = '2'
    else:
      if palabra_en_lista[i] == 'C':
        palabra_en_lista[i]= '3'
      else:
        if palabra_en_lista[i] == 'D':
          palabra_en_lista[i] = '4'
        else:
          if palabra_en_lista[i] == 'E':
            palabra_en_lista[i] = '5'
          else:
            if palabra_en_lista[i] == 'F':
              palabra_en_lista[i] = '6'
            else:
              if palabra_en_lista[i] == 'G':
                palabra_en_lista[i] = '7'
              else:
                if palabra_en_lista[i] == 'H':
                  palabra_en_lista[i] = '8'
                else:
                  if palabra_en_lista[i] == 'I':
                    palabra_en_lista[i] = '9'
                  else:
                    if palabra_en_lista[i] == 'J':
                      palabra_en_lista[i] = '10'
                    else:
                      if palabra_en_lista[i] == 'K':         
                        palabra_en_lista[i] = '11'
                      else:
                        if palabra_en_lista[i] == 'L':
                          palabra_en_lista[i] = '12'
                        else:
                          if palabra_en_lista[i] == 'M':
                            palabra_en_lista[i] = '13'
                          else:
                            if palabra_en_lista[i] == 'N':
                              palabra_en_lista[i] = '14'
                            else:
                              if palabra_en_lista[i] == 'Ñ':
                                palabra_en_lista[i] = '15'
                              else:
                                if palabra_en_lista[i] == 'O':
                                  palabra_en_lista[i] = '16'
                                else:
                                  if palabra_en_lista[i] == 'P':
                                    palabra_en_lista[i] = '17'
                                  else:
                                    if palabra_en_lista[i] == 'Q':
                                      palabra_en_lista[i] = '18'
                                    else:
                                      if palabra_en_lista[i] == 'R':
                                        palabra_en_lista[i] = '19'
                                      else:
                                        if palabra_en_lista[i] == 'S':
                                          palabra_en_lista[i] = '20'
                                        else:
                                          if palabra_en_lista[i] == 'T':
                                            palabra_en_lista[i] = '21'
                                          else:
                                            if palabra_en_lista[i] == 'U':
                                              palabra_en_lista[i] = '22'
                                            else:
                                              if palabra_en_lista[i] == 'V':
                                                palabra_en_lista[i] = '23'
                                              else:
                                                if palabra_en_lista[i] == 'W':
                                                  palabra_en_lista[i] = '24'
                                                else:
                                                  if palabra_en_lista[i] == 'X':
                                                    palabra_en_lista[i] = '25'
                                                  else:
                                                    if palabra_en_lista[i] == 'Y':
                                                      palabra_en_lista[i] = '26'
                                                    else:
                                                      if palabra_en_lista[i] == 'Z':
                                                        palabra_en_lista[i] = '27'
  i +=1

n = ','
alfanumerico = n.join(palabra_en_lista)

print(f"la palabra {palabra} tiene su equivalente alfa-numerico como {alfanumerico}")