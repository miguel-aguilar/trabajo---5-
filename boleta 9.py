#INPUT
cliente=input("ingrese el nombre del cliente:")
cantidad_de_kg=int(input("ingrese el numero de kg de pollo:"))
pu=float(input("ingrese precio de cada kg:"))

#PROCESSING
total = (cantidad_de_kg * pu)
descuento = (cantidad_de_kg*0.1)
precio_a_pagar = (total-descuento)

#VERIFICADOR
compra_excesiva=(precio_a_pagar>100)

#OUTPUT
print("#############################")
print("# BOLETA DE VENTA")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Item             : ", cantidad_de_kg, "kg de pollo ")
print("# P.U.             : ", pu)
print("# Total            : ", total)
print("# Descuento        : ", descuento)
print("# Precio a pagar   : ", precio_a_pagar)
print("#############################")
print("compra excesiva?:", compra_excesiva)
