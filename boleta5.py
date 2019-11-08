#INPUTN5
masa_del_ladrillo=int(input("ingrese la masa del ladrillo:"))
calor_especifico=int(input("ingrese el calor especifico:"))
temperatura=int(input("ingrese la temperatura:"))

# PROCESSING
capacidad_calorifica=(masa_del_ladrillo*calor_especifico*temperatura)

# OUTPUT
print("masa1= ", masa_del_ladrillo)
print("calor especifico= ", calor_especifico)
print("temperatura= ", temperatura)
print("CAPACIDAD CALORIFICA= ", capacidad_calorifica)
