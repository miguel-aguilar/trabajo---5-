#INPUT
cliente=input("ingrese el nombre del cliente:")
latas_de_conserva=int(input("ingrese el numero de latas de conserva de durazno:"))
precio_de_cada_lata=float(input("ingrese precio de cada lata:"))
botellas_de_yogurt=int(input("ingrese el numero de botellas de yogurt:"))
precio_de_cada_botella=float(input("ingrese precio de cada botella:"))

#PROCESSING
total_1 = (latas_de_conserva * precio_de_cada_lata )
total_2 = (botellas_de_yogurt * precio_de_cada_botella)
monto_total = (total_1 + total_2)
descuento_1 = (latas_de_conserva*0.5)
descuento_2 = (botellas_de_yogurt*0.4)
descuento_total = (descuento_1 + descuento_2)
precio_a_pagar = (monto_total-descuento_total)

#VERIFICADOR
compra_excesiva=(precio_a_pagar>300)

#OUTPUT
print("#############################")
print("# BOLETA DE VENTA")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Item             : ", latas_de_conserva, " latas de conserva de durazno ")
print("# P.U.             : ", precio_de_cada_lata)
print("# Item             : ", botellas_de_yogurt, " botellas de yogurt ")
print("# P.U.             : ", precio_de_cada_botella)
print("# Total            : ", monto_total)
print("# Descuento        : ", descuento_total)
print("# Precio a pagar   : ", precio_a_pagar)
print("#############################")
print("compra excesiva?:", compra_excesiva)
