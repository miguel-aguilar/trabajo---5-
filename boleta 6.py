#INPUT
cliente=input("ingrese el nombre del cliente:")
cantidad_de_tv=int(input("ingrese el numero de tv:"))
pu=float(input("ingrese precio de cada tv:"))

#PROCESSING
total = (cantidad_de_tv * pu)
descuento = (cantidad_de_tv*100.0)
precio_a_pagar = (total-descuento)

#VERIFICADOR
compra_excesiva=(precio_a_pagar>25000)

#OUTPUT
print("#############################")
print("# BOLETA DE VENTA")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Item             : ", cantidad_de_tv, " tv ")
print("# P.U.             : ", pu)
print("# Total            : ", total)
print("# Descuento        : ", descuento)
print("# Precio a pagar   : ", precio_a_pagar)
print("#############################")
print("compra excesiva?:", compra_excesiva)
