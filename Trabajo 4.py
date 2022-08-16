print("-------------------------------------------------------")
print("EjercicioN: VERIFICAR SI EL A�O ES BISIESTO.")
print("-------------------------------------------------------")

anio = int( input("Ingrese a�o: "))

print("\nSALIDA: ")
print("-------------------------------------------------------")

if (anio % 400 == 0) or (anio % 4 == 0) and (anio % 100 != 0):
print("El a�o es BISIESTO")

else:
print("El a�o NO es BISIESTO")