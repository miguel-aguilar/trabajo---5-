# INPUTN3
alumno=input("Ingrese el nombre del alumno:")
nota1=float(input("Ingrese nota1-asisteencia:"))
nota2=float(input("Ingrese nota2-peso1:"))
nota3=float(input("Ingrese nota3-peso2:"))
nota4=float(input("Ingrese nota4-peso3:"))

# PROCESSING
prom = (nota1+nota2+nota3+nota4)/4

# OUTPUT
print("PROMEDIO DE NOTAS DE PROGRAMACION A FIN DE CICLO")
print("El alumno", alumno, " tiene de promedio:", prom)
