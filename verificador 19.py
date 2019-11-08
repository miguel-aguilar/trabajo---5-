#calculadora diesinueve
#esta calculadora realizara calculos de la elipse

#declaracion de variables
semieje_mayor,semieje_menor,pi,area_de_la_elipse=0.0,0.0,3.14,0.0

#calculadora
semieje_mayor=23
semieje_menor=14
pi=3.14
area_de_la_elipse=(semieje_menor*semieje_mayor*pi)

#mostrar datos
print("semieje mayor= ", semieje_mayor)
print("semieje menor= ", semieje_menor)
print("pi= ", pi)
print("area de la elipse= ", area_de_la_elipse)

#verificador
verificador=bool(area_de_la_elipse<300)
print("el area de la elipse es menor que 300= ", (verificador))
