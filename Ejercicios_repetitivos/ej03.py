"""
Programa que pide caracteres hasta que se introduce un espacio y comprueba si el caracter
es vocal o no

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 04/11/2021

=============================================================================
Algoritmo
==========================================================================
1. pedimos un caracter.
2. comprobamos la longitud de la cadena, para saber si es un caracter
3. comprobamos que no es un espacio.
4. si es un espacio salimos del programa
5. si no es un espacio comprobamos si es vocal o no
"""

print("========================================================")
print("|Programa que pide un carracter y dice si es vocal o no|")
print("========================================================")

vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
letra = input("Introduce un caracter: ")

if len(letra) == 1:  # comprobacionde que es un caracter
    while letra != " ":
        if letra in vocales:
            print("VOCAL")
            letra = input("Introduce un caracter: ")
        else:
            print("NO VOCAL")
            letra = input("Introduce un caracter: ")
    if letra == " ":
        print("HAs introducido un espacio, ADIOS!!!")
