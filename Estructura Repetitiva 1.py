print("-------------------------------------------------------")
print("Repetivo 1")
print("-------------------------------------------------------")

C = -1
I = 0
M = 0

while (C<0) or (I<=0) or (I>=100) or (M <=0):

print("Introduce el capital, el inter�s y el tiempo apropiados")
C = int( input("Capital: "))
I = int( input("Inter�s: "))
M = int( input("Tiempo en A�os: "))

for i in range(M):

C = C*( 1 + I/100)

print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("Tienes", C , "soles")