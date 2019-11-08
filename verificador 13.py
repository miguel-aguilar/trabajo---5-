#calculadora trece
#esta calculadora realizara calculos del caudal

#declaracion de variables
volumen,tiempo,caudal=0.0,0.0,0.0

#calculadora
volumen=120
tiempo=3
caudal=(volumen/tiempo)

#mostrar datos
print("volumen= ", volumen)
print("tiempo= ", tiempo)
print("caudal= ", caudal)

#verificador
verificador=bool(caudal>950)
print("el caudal excede a 950= ", (verificador))
