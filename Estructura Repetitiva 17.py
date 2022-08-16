print("-------------------------------------------------------")
print("Repetitivo 17")
print("-------------------------------------------------------")

i = 1
c = 0
numEntradas = 10

print("Ingrese", numEntradas, "N�meros:")

while i <= numEntradas:
n = int( input("Ingrese n�mero: "))

if n%2 == 0 :
c = c + 1
i = i + 1

print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("En", numEntradas, "n�meros enteros hay", c, "n�meros pares")