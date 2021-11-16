"""
Programa que pide una cadena y un caracter y muestra cuantas veces
aparece el carácter en la cadena

- Autor: Francisco Manuel Moyano Coleto

----------------------------------------------------
1. Pedimos la cadena
2. Pedimos el carácter
3. creamos la variable contador
4. recorremos la cadena y si es igual aumentamos en 1 la variable contador
5. mostramos contador
"""

print("====================================================================")
print("Programa que muestra cuantas veces aparece un carácter en una cadena")
print("====================================================================")

cadena = input("Introduce una cadena: ")
caracter = input("Introduce un caracter: ")
contador = 0

for i in cadena:
    if i == caracter:
        contador += 1
print("El caracter ", caracter, "esta ", contador, "veces en la cadena")
