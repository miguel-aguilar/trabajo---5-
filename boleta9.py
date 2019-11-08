#INPUTN9
velocidad=int(input("ingrese la velocidad:"))
tiempo=int(input("ingrese el tiempo:"))
aceleracion=int(input("ingrese la aceleracion:"))

# PROCESSING
altura=(velocidad*tiempo+(aceleracion*tiempo*tiempo)/2)

# OUTPUT
print("velocidad= ",velocidad)
print("tiempo= ", tiempo)
print("aceleracion= ",aceleracion)
print("ALTURA= ", altura)
