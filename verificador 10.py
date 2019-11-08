#calculadora diez
#esta calculadora realizara calculos de fuerza resultante

#declaracion de variables
masa,aceleracion,fuerza_resultante=0.0,0.0,0.0

#calculadora
masa=34
aceleracion=12
fuerza_resultante=(masa*aceleracion)

#mostrar datos
print("masa= ", masa)
print("aceleracion= ", aceleracion)
print("fuerza resultante= ", fuerza_resultante)

#verificador
verificador=bool(fuerza_resultante>650)
print("la fuerza resultante excede a 650= ", (verificador))
