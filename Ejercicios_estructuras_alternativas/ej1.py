"""
programa que lee dos números e indica si el primero es mayor que el segundo o no

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 14/10/2021
-------------------------------------------------------------
Algoritmo
-------------------------------------------------------------
1. Pedir los dos númeoros
2. Comparar el primer numero con el segundo
3. si es mayor sacar por pantalla un mensaje diciendo que es mayor y si no un mensaje diciendo que es menor

"""

print("Comprobación de dos números")

# Pedir al usuario los datos
num1 = float(input("Introduzca el primer número :"))
num2 = float(input("Introduzca el segundo número :"))

# vamos a mostrar por pantalla según la condición

if num1 > num2:
    print("El ", num1, " es mayor que ", num2)

else:
    if num1 == num2:
        print("El ", num1, "y ", num2, " es el mismo")
    else:
        print("El ",num1, " es menor que ", num2)
