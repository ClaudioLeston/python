print("-------------------------------------------------------")
print("Repetitivo 15")
print("-------------------------------------------------------")

print ("Ingrese la cantidad de n�meros a comparar:")
lim = int( input())

print ("Ingrese los n�meros: ")
n = int( input("Ingrese n�mero: "))

men = n
may = n

for i in range(1, lim):

n = int( input("Ingrese n�mero: "))
if n < men :
men = n

else:
if n > may :
may = n

print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("El n�mero menor es :" ,men)
print ("El n�mero mayor es :", may)