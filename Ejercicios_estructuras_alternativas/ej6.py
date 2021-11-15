"""
Programa que lee una cadena por teclado y compruebe si es una letra mayúscula

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 19/10/2021

--------------------------------------------------------------
Algoritmo
--------------------------------------------------------------
1. pedimos al usuario que introduzca el valor
2. comparamos que ha introducido solo un valor
3. comprobamos que ese valor sea mayúscula
4. sacamos por pantalla si es mayuscula o no
"""

print("--------------------------")
print("Comprobación de mayúsculas")
print("--------------------------")

# pedimos los datos al usuario
letra = input("Introduce la letra: ")

# comprobamos y mostramos al usuario
if len(letra) == 1 and letra.isupper():
    print("La cadena es una letra mayúscula")
else:
    print("La cadena no es una letra mayúscula")
