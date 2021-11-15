"""
Programa que lee 3 datos que son las dimensiones de los lados
de un triangulo y segun los lados nos diga que tipo de triangulo es

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 24/10/2021

-------------------------------------------------
Algoritmo
-------------------------------------------------
1. Pedimos los tres lados.
2. comparamos los lados para saber que tipo de triangulo es.
3. mostramos el resultado
"""

# Pedimos los datos
A = float(input("Introduce la longitud del lado A: "))
B = float(input("Introduce la longitud del lado B: "))
C = float(input("Introduce la longitud del lado C: "))

# Cálculos
if A == B == C:
    print("El triangulo es 'equilatero'")
else:
    if A**2 == (B**2+C**2) or B**2 == (A**2+C**2) or C**2 == (B**2+A**2):
        print("El triángulo es 'Rectángulo'")
    if A == B or A == C or B == C:
        print("El triángulo es 'Isóceles'")
    else:
        print("El triangulo es 'Escaleno'")
