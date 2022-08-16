print("-------------------------------------------------------")
print("Repetitivo 2")
print("-------------------------------------------------------")

print("Introduce un n�mero, y para acabar uno negativo:")
numero = int( input("N�m: "))

while numero > 0 :

Suma = 0
for i in range(1,numero+1):

if numero % i == 0 :
Suma = Suma + i

print("\nSALIDA: ")
print("----------------------------------------------------")

print("La suma de los divisores del n�mero es:", Suma, "\n" )

print("Introduce un n�mero, y para acabar uno negativo:")
numero = int( input("N�m: "))