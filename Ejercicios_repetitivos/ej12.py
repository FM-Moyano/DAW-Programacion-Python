"""
Programa que pide una cadena y dos caracteres por teclado (valida que sea un carácter),
sustituye la aparición del primer carácter en la cadena por el segundo carácter.

-Autor: Francisco Manuel Moyano Coleto

=================================================================
Algoritmo
=================================================================
1. Pedimos la candena.
2. Pedimos el carácter que vamos a sustituir.
3. comprobamos que es un caracter.
4. comprobamos que ese caracter está en la cadena.
5. si no está salimos del programa.
5. si el caracter está, pedimos el caracter por el que va a ser sustituido.
6. vamos recorriendo la cadena y si c es igual a el caracter lo sustituimos.

"""
print("----------------------------------------------------------------------------------")
print("Programa que pide una cadena, un caratr que esté en la cadena y uno que lo sustiya")
print("----------------------------------------------------------------------------------")

cadena = input("Introduce una cadena: ")
caracter1 = input("Introduce el primer caracter: ")

if len(caracter1) != 1:
    print("No has introducido un carácter")
    exit(1)
elif caracter1 in cadena:
    caracter2 = input("Introduce el segundo carácter: ")
else:
    print("El caracter a sustituir no está en la cadena")
    exit(1)


cadena_final = ""
for c in cadena:
    if c == caracter1:
        cadena_final += caracter2
    else:
        cadena_final += c

print(cadena_final)
