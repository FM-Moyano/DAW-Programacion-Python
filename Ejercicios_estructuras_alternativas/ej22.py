"""
Programa que pida cinco números enteros y diga cuál es el mayor.
----------------------------------------------------------------------------------------------------------------

Autor: Francisco Manuel Moyano Coleto
Fecha: 24/10/2021

----------------------------------------------------------------------------------------------------------------
Algoritmo:
1. Pedir 5 número
2. comprobamos que número es mayor.
3. inprimimos el resultado
"""
print("-------------------------------------")
print("Este programa muestra el número mayor")
print("-------------------------------------")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
num4 = int(input("Introduce el cuarto número: "))
num5 = int(input("Introduce el quinto número: "))

# comprobamos el mayor

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print("EL ", num1, "es el mayor")
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("EL ", num2, "es el mayor")
elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    print("EL ", num3, "es el mayor")
elif num4 > num1 and num4 > num3 and num4 > num2 and num4 > num5:
    print("EL ", num4, "es el mayor")
elif num5 > num1 and num5 > num3 and num5 > num4 and num5 > num2:
    print("EL ", num5, "es el mayor")
else:
    print("Los dos números mayores son iguales")




