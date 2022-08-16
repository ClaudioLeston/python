Sprint("-------------------------------------------------------")
print("Repetitivo 13")
print("-------------------------------------------------------")

print("Ingrese un n�mero:")
n = int( input())

con = 0

for i in range(2, n):
if n % i == 0 :

con = con + 1

print("\nSALIDA: ")
print("-------------------------------------------------------")

if con == 0:
print (n, " Es un n�mero primo")
else:

print (n, " No es un n�mero primo")