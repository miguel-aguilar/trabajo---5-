#calculadora doce
#esta calculadora realizara calculos de la inercia

#declaracion de variables
masa,area,inercia=0.0,0.0,0.0

#calculadora
masa=35
area=80
inercia=(masa*area)

#mostrar datos
print("masa= ", masa)
print("area= ", area)
print("inercia= ", inercia)

#verificador
verificador=bool(inercia<3000)
print("la inercia es menor que 3000= ", (verificador))
