print("-------------------------------------------------------")
print("Trabajo 6")
print("-------------------------------------------------------")

NUM = int( input("Ingrese n�mero:" ))

par_Impar = {
1 : 'Impar',
3 : 'Impar',
5 : 'Impar',
7 : 'Impar',
9 : 'Impar',
2 : 'Par',
4 : 'Par',
6 : 'Par',
8 : 'Par',
10 : 'Par'
}

print("\nSALIDA: ")
print("-------------------------------------------------------")
print(par_Impar.get(NUM, "Numero fuera de Rango"))