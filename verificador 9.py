#calculadora nueve
#esta calculadora realizara calculos del area del rectangulo

#declaracion de variables
lado1,lado2,area_del_rectangulo=0.0,0.0,0.0

#calculadora
lado1=30
lado2=48.9
area_del_rectangulo=(lado1*lado2)

#mostrar datos
print("lado 1= ", lado1)
print("lado 2= ", lado2)
print("area del rectangulo= ", area_del_rectangulo)

#verificador
verificador=bool(area_del_rectangulo<320)
print("el area del rectangulo es menor que 320= ", (verificador))
