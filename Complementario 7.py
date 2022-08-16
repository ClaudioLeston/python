print("-------------------------------------------------------")
print("Complemento7")
print("-------------------------------------------------------")

print("Ingrese valores de la ecuaci�n cuadr�tica:")
a = int( input("a: "))
b = int( input("b: "))
c = int( input("c: "))

d = b**2 - 4*a*c

print("\nSALIDA: ")
print("-------------------------------------------------------")

if d > 0 :
x1 = ( (-b) + d**0.5 )/ 2*a
x2 = ( (-b) - d**0.5 )/ 2*a

print("Ra�ces reales:", x1, x2)

else:
print("Ra�ces Irracionales")