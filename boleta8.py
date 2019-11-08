#INPUTN8
velocidad_inicial=int(input("ingrese la velocidad inicial:"))
aceleracion=int(input("ingrese la aceleracion:"))
tiempo=int(input("ingrese el tiempo:"))

# PROCESSING
velocidad_final=(velocidad_inicial+aceleracion*tiempo)

# OUTPUT
print("velocidad inicial= ", velocidad_inicial )
print("aceleracion= ", aceleracion)
print("tiempo= ", tiempo)
print("VELOCIDAD FINAL= ",velocidad_final )
