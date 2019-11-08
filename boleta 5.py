#INPUT
cliente=input("ingrese el nombre del cliente:")
cajas_de_cerveza=int(input("ingrese el numero de cajas:"))
pu=float(input("ingrese precio de cada caja:"))

#PROCESSING
total = (cajas_de_cerveza * pu)
descuento = (cajas_de_cerveza*0.5)
precio_a_pagar = (total-descuento)

#VERIFICADOR
compra_excesiva=(precio_a_pagar>2000)

#OUTPUT
print("#############################")
print("# BOLETA DE VENTA")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Item             : ", cajas_de_cerveza, "cajas de cerveza")
print("# P.U.             : ", pu)
print("# Total            : ", total)
print("# Descuento        : ", descuento)
print("# Precio a pagar   : ", precio_a_pagar)
print("#############################")
print("compra excesiva?:", compra_excesiva)
