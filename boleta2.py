#INPUT N2
cliente=input("cliente:")
mesero=input("mesero:")
cantidad_de_platos_de_arroz_chaufa=int(input("Cantidad de platos de arroz chaufa:"))
pu_del_arroz_chaufa=float(input("Ingrese precio unitario del plato de arroz chaufa:"))
cantidad_de_botellas_de_inka_cola=int(input("Cantidad de botellas de inka cola:"))
pu_de_la_botella_de_inka_cola=float(input("Ingrese precio unitario de la botella de inka cola:"))

# PROCESSING
total = (pu_del_arroz_con_pato * cantidad_de_platos_de_arroz_con_pollo+cantidad_de_botellas_de_inka_cola*pu_de_la_botella_de_inka_cola)

# OUTPUT
print("#######################")
print("# CHIFA -EL DRAGON ROJO #")
print("#######################")
print("# Cliente:  ", cliente, " -  # Mesero:", mesero)
print("# Item 1  :  ",cantidad_de_platos_de_arroz_chaufa,"platos de arroz haufa")
print("# Item 2  :  ",cantidad_de_botellas_de_inka_cola,"botellas de inka cola")
print("# P.U. del arroz chaufa  :  S/.", pu_del_arroz_chaufa)
print("# P.U. de la inka cola   :  S/.", pu_de_la_botella_de_inka_cola)
print("# Total  :  S/.", total)
print("#######################")
