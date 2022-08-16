print("-------------------------------------------------------")
print("Repetitivo 10")
print("-------------------------------------------------------")

print( "Ingrese el n�mero de t�rminos: ")
n = int( input())

s = 5
ser = 0

for a in range(1, n+1):
s = s + 5
ser = ser + s

print("\nSALIDA: ")
print("-------------------------------------------------------")
print("La suma de la serie es:", ser)