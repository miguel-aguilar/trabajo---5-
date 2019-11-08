#INPUT
cliente=input("ingrese el nombre del cliente:")
cantidad_de_cuadernos=int(input("ingrese el numero de cuadernos:"))
pu=float(input("ingrese precio de cada cuaderno:"))

#PROCESSING
total = (cantidad_de_cuadernos * pu)
descuento = (cantidad_de_cuadernos*0.1)
precio_a_pagar = (total-descuento)

#VERIFICADOR
compra_excesiva=(precio_a_pagar>300)

#OUTPUT
print("#############################")
print("# BOLETA DE VENTA")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Item             : ", cantidad_de_cuadernos, " cuadernos ")
print("# P.U.             : ", pu)
print("# Total            : ", total)
print("# Descuento        : ", descuento)
print("# Precio a pagar   : ", precio_a_pagar)
print("#############################")
print("compra excesiva?:", compra_excesiva)
