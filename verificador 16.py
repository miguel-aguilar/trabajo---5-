#calculadora diesiseis
#esta calculadora realizara calculos del calor latente

#declaracion de variables
area,tiempo,calor_latente=0.0,0.0,0.0

#calculadora
area=45
tiempo=3
calor_latente=(area/tiempo**2)

#mostrar datos
print("area= ", area)
print("tiempo= ", tiempo)
print("calor latente= ", calor_latente)

#verificador
verificador=bool(calor_latente<543)
print("el calor latente es menor que 543= ", (verificador))
