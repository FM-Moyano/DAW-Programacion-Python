"""
Programa que lee la base  y el exponente y realice la potencia

-Autor: Francisco Manuel Moyno coleto

------------------------------------------------------
Algoritmo
1. Pedimos la base y el exponente
2. comprobamos que se han introducido correctamente
3. multiplicamos ba base por el mismo hasta que se repita
tantas veces como el número del exponente.
"""

print("=================================")
print("Programa que calcula la potencia")
print("=================================")
num = 1
base = float(input("Introduce la base: "))
exponente = int(input("introduce el exponente: "))

while exponente < 0:
    print()
    print("Has introducido un número negativo")
    exponente = int(input("introduce el exponente: "))

for i in range(exponente):
    num *= base

if exponente == 0:
    print()
    print("El resultado de la potencia es 1")
else:
    print()
    print("El resultado de la potencias es ", num)

