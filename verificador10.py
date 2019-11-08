#calculadora nro10
#esta calculadora calcula el empuje del agua

#declaracion de variables
densidad,volumen_de_una_pelota,gravedad,empuje_del_agua=0.0,0.0,0.0,0.0

#calculadora
densidad=30
volumen_de_una_pelota=8
gravedad=10
empuje_del_agua=(densidad*gravedad*volumen_de_una_pelota)
verificador=(empuje_del_agua==2400)

#mostrar datos
print("densidad= ", densidad)
print("volumen de la pelota= ", volumen_de_una_pelota)
print("gravedad= ", gravedad)
print("empuje del agua= ", empuje_del_agua)
print("empuje del agua:", verificador)
