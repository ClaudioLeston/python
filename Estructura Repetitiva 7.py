print("-------------------------------------------------------")
print("Repetitivo 7")
print("-------------------------------------------------------")

c = 0

print("Ingrese 10 n�meros: ")

for i in range(1, 10 + 1):

num = int( input("Ingrese N�mero: "))
if num % 2 == 0 :

c = c + 1

print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Hay", c, "n�meros pares")