"""
Programa que pide un cadena y nos muestra cuantas pabalbras hemos escrito

- Autor: Francisco Manuel Moyano Coleto

-------------------------------------------------------
Algoritmo
------------------------------------------------------
1. Pedimos la cadena
2. creamos una variable palabras que la igualaremos a 1 para contar la primera palabra
3. comprobamos que no se ha introducido un espacio en blanco o nada
4. recorremos la cadena y por cada espacio sumanos 1 a la cadena palabras
"""

print("Programa que muestra las palabras que contiene una cadena")

cadena = input("Introduce una cadena: ")
palabras = 1

if cadena == "" or cadena == " ":
    print("No has introducido ninguna palabra")
else:
    for i in cadena:
        if i == " ":
            palabras += 1
print("Esta cadena tiene ", palabras, "palabras")
