"""
Programa que ompruebe si una cadena contiene una subcadena.
Las dos cadenas se introducen por teclado.

-Autor: Francisco Manuel Moyano Coleto

=================================================================================
Algoritmo
=================================================================================
1. Pedimos la cadena
2. pedimos la subcadena
3. comprobamos que la subcadena está en la cadena
"""

print("==========================================================")
print("Programa que comprueba si una subcadena está en una cadena")
print("==========================================================")

cadena = input("Introduce la cadena: ")
sub_cadena = input("Introduce la subcadena: ")

es_subcadena = False
for comprobacion in range(len(cadena) - len(sub_cadena)):
    if sub_cadena == cadena[comprobacion:comprobacion + len(sub_cadena)]:
        es_subcadena = True
        break


if es_subcadena:
    print("La subcaena está en la cadena")
else:
    print("La subcadena no está en la cadena")
