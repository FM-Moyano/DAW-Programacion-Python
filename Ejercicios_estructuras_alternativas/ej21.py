"""
Programa que pida tres números enteros y diga cuál es el mayor.
----------------------------------------------------------------------------------------------------------------

Autor: Francisco Manuel Moyano Coleto
Fecha: 24/10/2021

----------------------------------------------------------------------------------------------------------------
Algoritmo:
1. Pedimos los 3 números.
2. Si num1 es mayor que num2 y num1 es mayor que num3,
num1 es el mayor
3. Si num2 es mayor que num1 y num2 es mayor que num3,
num2 es el mayor
4. Si num3 es mayor que num1 y num3 es mayor que num2,
num3 es el mayor
"""

print("-------------------------------------------")
print("Este programa que muestra el número mayor")
print("-------------------------------------------")

num1 = int(input("Introduce el primer número : "))
num2 = int(input("Introduce el segundo número : "))
num3 = int(input("Introduce el tercer número : "))

if num1 == num2 or num1 == num3 or num2 == num3:
    print("Has introducido algunos números iguales")
elif num1 > num2 and num1 > num3:
    print(f"El número mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El número mayor es: {num2}")
elif num3 > num1 and num3 > num2:
    print(f"El número mayor es: {num3}")
