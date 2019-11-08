#INPUTN4
cliente=input("cliente:")
cajero=input("cajero:")
cantidad_de_cemento=int(input("Cantidad de cementos pacasmayo:"))
pu_del_cemento=float(input("Ingrese precio unitario del cemento pacasmayo:"))

# PROCESSING
total = (pu_del_cemento*pu_del_cemento)

# OUTPUT
print("#######################")
print("# FERRERTERIA - PERNO LOCO")
print("#######################")
print("# Cliente:  ", cliente, " -  # cajero:", cajero)
print("# Item   :  ",cantidad_de_cemento," cementos pacasmayo")
print("# P.U.   :  S/.", pu_del_cemento)
print("# Total  :  S/.", total)
print("#######################")
