"""
programa que lee dos edades e indica si el primero es mayor que el segundo o no

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 14/10/2021
-------------------------------------------------------------
Algoritmo
-------------------------------------------------------------
1. Pedir los dos númeoros
2. Comparar el primer numero con el segundo
3. si es mayor sacar por pantalla un mensaje diciendo que es mayor y si no un mensaje diciendo que es menor

"""

print("Calculamos quien de los dos es mayor")

# Pedimos las edades al usuario
edad1 = int(input("Introduzca la edad de la primera persona : "))
edad2 = int(input("Introduzca la edad de la segunda persona : "))

# Comprobamos y mostramos
if edad1 > edad2:
    print("El primero es mayor que el segundo")

else:
    if edad1 == edad2:
        print("los dos tienen la misma edad")
    else:
        print("El segundo es mayor que el primero")
