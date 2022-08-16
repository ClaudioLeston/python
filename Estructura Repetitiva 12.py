print("-------------------------------------------------------")
print("Repetitivo 12")
print("-------------------------------------------------------")

aux = 0
aux2 = 0

print("Ingrese un n�mero: ")

n = int( input())
i = 10

while i <= n:

aux = n%10
n = n // 10
aux2 = aux2*10 + aux
aux2 = aux2*10 + n

print("\nSALIDA: ")
print("-------------------------------------------------------")
print("El n�mero invertido ser�:", aux2)