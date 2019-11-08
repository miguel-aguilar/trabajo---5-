#INPUT
cliente=input("ingrese el nombre del cliente:")
litros=int(input("ingrese el numero de litros de leche:"))
precio_del_litro=float(input("ingrese precio del litro:"))

#PROCESSING
total = (litros * precio_del_litro)
descuento = (litros*0.2)
precio_a_pagar = (total-descuento)

#VERIFICADOR
compra_excesiva=(precio_a_pagar>100)

#OUTPUT
print("#############################")
print("# BOLETA DE VENTA")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Item             : ",litros, "litros de leche")
print("# P.U.             : ", precio_del_litro)
print("# Total            : ", total)
print("# Descuento        : ", descuento)
print("# Precio a pagar   : ", precio_a_pagar)
print("#############################")
print("compra excesiva?:", compra_excesiva)
