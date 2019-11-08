#calculadora cuatro
#esta calculadora realizara calculos de peso especifico

#declaracion de variables
peso,volumen,peso_especifico=0.0,0.0,0.0

#calculadora
peso=90
volumen=15
peso_especifico=(peso/volumen)

#mostrar datos
print("peso= ", peso)
print("volumen= ", volumen)
print("peso especifico= ", peso_especifico)

#verificador
verificador=bool(peso_especifico!=250)
print("el peso especifico es diferente a 250= ", (verificador))
