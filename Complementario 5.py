print("-------------------------------------------------------")
print("Complemento5")
print("-------------------------------------------------------")

print("Ingrese las velocidades de ambos veh�culos: ")
v1 = float( input("V1: "))
v2 = float( input("V2: "))

print("Ingrese la distancia que los separa: ")
d = float( input("Distancia: "))

print("\nSALIDA: ")
print("-------------------------------------------------------")

if v1 > 0 and v2 > 0 :
t = d/(v1+v2)
print(t, "segundos")

else:
print("ERROR")