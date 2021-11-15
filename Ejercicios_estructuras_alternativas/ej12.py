"""l
Programa que nos dice si un año es bisiento o no

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 24/10/2021
"""
print("---------------------------------------------")
print("Programa que nos indica si un año es bisiesto")
print("---------------------------------------------")

# Pedir datos
num = int(input("Introduce el año: "))

# Cálculos
if num % 4 == 0 and num % 100 != 0:
    print("El año ", num, "es bisiesto")
else:
    print("El año ", num, "no es bisiesto")
