"""
Programa que soltea un número y pide al usuario un número con la intencion de adivinarlo
el usuario tiene 10 intentos y si se agotan esos 100 intentos muestra el numero que
se había solteado.

- Autor: Francisco Manuel Moyano Coleto
- Fecha : 03/11/2021

--------------------------------------------------------------------------
Algoritmo
--------------------------------------------------------------------------
1. Pedimos el número al usuario.
2. solteamos el número.
3 inicializamos la variable intentos a 0
4. comprobamos el numero de intentos
5. si el numero de intentos es menos del limite comprobamos
si el número introducido es igual al número sorteado
6. si es igual mostramos que se ha acertado y el número de intentos utilizados
7. si no es igual se comprueba si es mayor o menos y se informa al usuario.
8. si se llega al limite de intentos se muestra cual era el número y se termina el programa

"""

print("----------------------------------------------------")
print("|Programa que sortea un número y se intenta acertar|")
print("----------------------------------------------------")

from random import randrange

# Inicializamos las variables

num_sorteo = randrange(0, 100)
intentos = 1

while intentos <= 10:
    num_usuario = int(input("Introduce un número, tendrás 10 intentos: "))
    if num_usuario == num_sorteo:
        print("ENHORABUENA, has acertado el número y tu número de intentos es..", intentos)
        break
    elif num_usuario > num_sorteo:
        print("El número introducido es mayor al número sorteado, tu número de intentos es ", intentos)
    elif num_usuario < num_sorteo:
        print("El número introducido es menor que el número sorteado, tu número de intentos es ", intentos)
    intentos += 1

if intentos > 10:
    print("Has agotado los intentos, el número sorteado es ", num_sorteo)
