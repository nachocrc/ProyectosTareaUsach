#empresa de turismo
#ya la capacidad de los vehiculos de turismo puede cambiar le preguntamos al usuario cuanta gasolina llenará
gasolina_total_vehiculo_todo_terreno = 65
gasolina_total_vehiculo_de_turismo = float(input("¿cuantos litros de gasolina le agregará al tanque de los vehiculos de turismo?\n: "))
flota_turismo = int(input("¿cuantos vehiculos de turismo llevará?\n: "))
flota_todo_terreno = int(input("¿cuantos vehiculos todo terreno llevará?\n: "))
#luego de esto generamos el algoritmo, tras tener los datos
gasolina_gastada_turismo = flota_turismo*gasolina_total_vehiculo_de_turismo
gasolina_gastada_todo_terreno = flota_todo_terreno*gasolina_total_vehiculo_todo_terreno
gasolina_total = gasolina_gastada_todo_terreno+gasolina_gastada_turismo
print(f"para la flota todo terreno usaremos {gasolina_gastada_todo_terreno} litros")
print(f"para la flota de vehiculos de turismo usaremos {gasolina_gastada_turismo} litros")
print(f"por tanto gastaremos un total de {gasolina_total} litros")
