print("-------------------------------------------------------")
print("Repetitivo 14")
print("-------------------------------------------------------")

print ("Ingrese la cantidad de n�meros a evaluar:")
n = int( input())

c = 0

for i in range(1, n+1):

num = int( input("Ingrese n�mero: "))
if num == 0 :
c = c+1

print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("Hay ", c, " n�meros ceros")