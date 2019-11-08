#calculadora diesisiete
#esta calculadora realizara calculos del momento torque

#declaracion de variables
masa,area,tempo,momento_torque=0.0,0.0,0.0,0.0

#calculadora
masa=32
area=144
tiempo=4
momento_torque=(masa*area/tiempo**2)

#mostrar datos
print("masa= ", masa)
print("area= ", area)
print("tiempo= ", tiempo)
print("momento torque= ", momento_torque)

#verificador
verificador=bool(momento_torque>354)
print("el momento o torque excede a 354= ", (verificador))
