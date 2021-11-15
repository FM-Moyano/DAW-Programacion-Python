"""
programa que recibe un número e indica si es par o impar

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 14/10/2021

__________________________________________________
Algoritmo
__________________________________________________
1. Pedimos al usuario el número.
2. comprobamos si es par o no
3. sacamos el resto de la division del numero por dos
4. si el resultado es 1 es inpar y si es 0 es par
5. mostreamos al usuario si es par o no
"""

print("Calcular si un número es par o inpar")

# Pedimos al usuario el número
num = int(input("Introduce un número: "))

# Realizamos los calculos
resto = num % 2

# Mostramos los resultados según la condición

if resto == 0 :
    print("El número ", num, " es par")
else:
    print("El número ", num, " es inpar")
