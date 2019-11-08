#calculadora once
#esta calculadora realizara calculos de capacidad calorifica

#declaracion de variables
calor,variacion_de_la_temperatura,capacidad_calorifica=0.0,0.0,0.0

#calculadora
calor=800
variacion_de_la_temperatura=135
capacidad_calorifica=(calor/variacion_de_la_temperatura)

#mostrar datos
print("calor= ", calor)
print("variacion de la temperatura= ", variacion_de_la_temperatura)
print("capacidad calorifica= ", capacidad_calorifica)

#verificador
verificador=bool(capacidad_calorifica!=700)
print("la capacidad calorifica es diferente a 700= ", (verificador))
