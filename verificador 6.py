#calculadora seis
#esta calculadora realizara calculos de energia gravitatoria

#declaracion de variables
masa,gravedad,altura,energia_gravitatoria=0.0,9.8,0.0,0.0

#calculadora
masa=50
gravedad=9.8
altura=15
energia_gravitatoria=(masa*gravedad*altura)

#mostrar datos
print("masa= ", masa)
print("gravedad= ", gravedad)
print("altura= ", altura)
print("energia gravitatoria= ", energia_gravitatoria)

#verificador
verificador=bool(energia_gravitatoria>150)
print("la energia gravitatoria excede a 150= ", (verificador))
