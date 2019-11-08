#INPUT
cliente=input("ingrese el nombre del cliente:")
bolsas_de_caramelos=int(input("ingrese el numero de bolsas:"))
pu=float(input("ingrese precio de cada bolsa:"))

#PROCESSING
total = (bolsas_de_caramelos * pu)
descuento = (bolsas_de_caramelos*0.3)
precio_a_pagar = (total-descuento)

#VERIFICADOR
compra_excesiva=(precio_a_pagar>250)

#OUTPUT
print("#############################")
print("# BOLETA DE VENTA")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Item             : ", bolsas_de_caramelos, "bolsas de caramelos")
print("# P.U.             : ", pu)
print("# Total            : ", total)
print("# Descuento        : ", descuento)
print("# Precio a pagar   : ", precio_a_pagar)
print("#############################")
print("compra excesiva?:", compra_excesiva)
