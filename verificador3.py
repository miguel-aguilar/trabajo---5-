#calculadora nro3
#esta calculadora calcula capacidad calorifica

#declaracion de variables
capacidad_calorifica,masa2,calor_especifico,temperatura=0.0,0.0,0.0,0.0

#calculadora
masa2=15
calor_especifico=3
temperatura=10
capacidad_calorifica=(masa2*calor_especifico*temperatura)
verificador=(capacidad_calorifica<2830)

#mostrar datos
print("masa2= ", masa2)
print("calor especifico= ", calor_especifico)
print("temperatura= ", temperatura)
print("capacidad caorifica= ", capacidad_calorifica)
print("capacidad calorifica:", verificador)
