""""
Programa que lee un carácter y nos dice si es un punto de acentuación,
una letra, un dígito, o es otro tipo de carácter o si se ha introducido
más de uno decir que no es un carácter.

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 21/10/2021
___________________________________________________
Algoritmo
___________________________________________________
1. pedimos los datos
2. comprobamos se ha introducido un caracter.
3. si hay más de uno salimos y decimos ' no es un carácter' si no comporbamos que tipo es
4. mostramos que carácter es
"""

print("--------------------------------------------------")
print("|Comprobación de que carácter nos han introducido|")
print("--------------------------------------------------")

# Pedimos los datos
caracter = input("Introduce el carácter: ")

# comprobamos
if len(caracter) == 1:
    if caracter in ":;¿?'\\\",-/—()[]¡!.":
        print("Es un signo de puntuación")
    elif caracter.isalpha():
        print("Es una letra")
    elif caracter.isdigit():
        print("Es un dígito")
    else:
        print("Es otro tipo de carácter")
else:
    print("No es un carácter")
