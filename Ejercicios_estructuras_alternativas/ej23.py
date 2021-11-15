"""
Programa que, dados cinco números enteros, determine cuál de los cuatro últimos números es más
 cercano al primero. Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10, el programa responderá que el
 número más cercano al 2 es el 1.
----------------------------------------------------------------------------------------------------------------
Autor: Francisco Manuel Moyano Coleto
Fecha: 24/10/2021
----------------------------------------------------------------------------------------------------------------
Algotitmo:
1. pedimos los 5 números
2. creamos una variable comprobación, que inicialmente
la igualamos a num2
3. creamos una variable distancia que la igualamos al la distancia
entre num1 y num2.
4. vamos comparando la distacia de los demás números con la variable distancia.
5. si es menor que distancia se cambia el valor de distacia.
"""

print("-----------------------------")
print("Cálculo de la menor distancia")
print("-----------------------------")

# Pedir los datos
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
num4 = int(input("Introduce el cuarto número: "))
num5 = int(input("Introduce el quinto número: "))


comprobacion = num2
distancia = abs(num1 - num2)

# Comprobamos tercer número
if abs(num1 - num3) < distancia:
    comprobacion = num3
    distancia = abs(num1 - num3)

# Comprobamos cuarto número
if abs(num1 - num4) < distancia:
    comprobacion = num4
    distancia = abs(num1 - num4)

# Comprobamos quinto número
if abs(num1 - num5) < distancia:
    comprobacion = num5

print(comprobacion, "Es el número con menor distancia a", num1)
