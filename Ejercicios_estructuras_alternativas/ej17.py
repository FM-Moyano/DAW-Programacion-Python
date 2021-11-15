"""
Programa que nos dice el lado opuesto de un dado.

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 24/10/2021

--------------------------------------------------
Algoritmo
--------------------------------------------------
1. Pedimos el numero por pantalla.
2. comprobamos que está entre 1 y 6 (incluidos)
3. Si está entre los números comprobaremos que numero es y mmostramos el opuesto.
4. si no es mostramos que el número es incorrecto
"""

print("Programa que muestra la cara opuest ade un dado")
print("-----------------------------------------------")

# Pedimos los datos
num = int(input("Introduce el número del dado (1-6): "))

# Comprobamos
if num < 1 or num > 6:
    print("El número introducido es incorrecto")
else:
    if num == 1:
        print("En la cara opuesta está el 6")
    elif num == 2:
        print("En la cara opuesta está el 5")
    elif num == 3:
        print("En la cara opuesta está el 4")
    elif num == 4:
        print("En la cara opuesta está el 3")
    elif num == 5:
        print("En la cara opuesta está el 2")
    else:
        print("En la cara opuesta está el 1")
