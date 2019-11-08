#INPUT
cliente=input("ingrese el nombre del cliente:")
kg=int(input("ingrese el numero de kg de manzanas:"))
pu=float(input("ingrese precio unitario:"))

#PROCESSING
total = (pu * kg)

#VERIFICADOR
compra_excesiva=(total>200)

#OUTPUT
print("#############################")
print("# BOLETA DE VENTA")
print("#############################")
print("#")
print("# Cliente: ", cliente)
print("# Item   : ",kg, "kg manzana")
print("# P.U.   : ", pu)
print("# Total  : ", total)
print("#############################")
print("compra excesiva?:", compra_excesiva)

