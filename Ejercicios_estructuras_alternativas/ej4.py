"""
Programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 14/10/2021

--------------------------------------------------------------
Algoritmo
--------------------------------------------------------------
1. Pedimos los 2 números y loa amacenamos en variables
2. comprobamos si el segundo es 0
3. si es 0 mostramos mensaje y si no mosramos la división
"""

print("Mostramos la división de dos números")

# Introducción de datos
num1 = float(input("Introduce el primer número :"))
num2 = float(input("Introduce el segundo número :"))

# Salida
if num2 != 0:
    print(num1, "/", num2, "=", num1/num2)
else:
    print("Has introducido un valor erroneo")
