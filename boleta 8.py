#INPUT
cliente=input("ingrese el nombre del cliente:")
cantidad_de_computadoras=int(input("ingrese el numero de computadoras:"))
pu=float(input("ingrese precio de cada computadora:"))

#PROCESSING
total = (cantidad_de_computadoras * pu)
descuento = (cantidad_de_computadoras*50.0)
precio_a_pagar = (total-descuento)

#VERIFICADOR
compra_excesiva=(precio_a_pagar>10000)

#OUTPUT
print("#############################")
print("# BOLETA DE VENTA")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Item             : ", cantidad_de_computadoras, " computadoras ")
print("# P.U.             : ", pu)
print("# Total            : ", total)
print("# Descuento        : ", descuento)
print("# Precio a pagar   : ", precio_a_pagar)
print("#############################")
print("compra excesiva?:", compra_excesiva)
