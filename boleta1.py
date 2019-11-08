#INPUT
cliente=input("cliente:")
mesero=input("mesero:")
cantidad_de_platos_de_arroz_con_pollo=int(input("Cantidad de platos de arroz con pollo:"))
pu_del_arroz_con_pato=float(input("Ingrese precio unitario del plato de arroz con pollo:"))

# PROCESSING
total = (pu_del_arroz_con_pato * cantidad_de_platos_de_arroz_con_pollo)

# OUTPUT
print("#######################")
print("# RESTAURANTE -EL RINCON DE MIS RECUERDOS")
print("#######################")
print("# Cliente:  ", cliente, " -  # Mesero:", mesero)
print("# Item   :  ",cantidad_de_platos_de_arroz_con_pollo,"platos de arroz con pollo")
print("# P.U.   :  S/.", pu_del_arroz_con_pato)
print("# Total  :  S/.", total)
print("#######################")
















