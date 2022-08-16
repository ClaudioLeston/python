print("-------------------------------------------------------")
print("Vector1")
print("-------------------------------------------------------")

i = 1
F = [] 

print("Ingrese N�mero de elementos a Ingresar: ")
numElementos = int( input())

while i <= numElementos:

elemento = int( input("Ingrese Elemento: "))
F.append(elemento) #Agregamos el elemento a la lista
i = i + 1

print("\nSALIDA: ")
print("-------------------------------------------------------")
print(F)