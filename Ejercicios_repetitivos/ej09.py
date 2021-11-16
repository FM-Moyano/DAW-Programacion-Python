"""
Programa que muestra N primeros números primos, N se pide al usuario

-Autor: Francisco Manuel Moyanno Coleto

-------------------------------------------------------
Algoritmo
----------------------------------------------------
1. Pedimos el valor de N, que es la cantidad de primos
2. creamos la variable contador igual a 2, para ir acumulando
el total de números primos que llevamos
3. Creamos la variable numero igual a 3, porque vamos
a empezar a comprobar desde ese número
4. Creamos la variable orden igual a 2, porque el primer número primo
lo vamos a poner manual.
5. Imprimimos 1 : 2, que es el primer y nunico número primo que no es impar
6. Cremamos un contador
7. Creamos un bucle que se esté ejecutando mientras contador
sea <= que cantidad_primos
8. Si el número es impar, lo mostramos, aumentamos en 1 el contador y orden
9. Aumentamos en 1 el número
"""

print("==================================================")
print("Programa que muestra los primeros N números primos")
print("==================================================")

cantidad_primos = int(input("Introduce el número de números primos que va a mostrar: "))
contador = 2  # variable que acumula los número primos que llevamos, empezamos en 2
numero = 3  # Esta variable es con la que vamos a empezar a comprobar
orden = 2  # Empezamos con el 2, porque el 1 va a ser el número 2 que lo ponemos manualmente

print("1 : 2")

while contador <= cantidad_primos:
    if numero % 2 == 1:  # comporbamos que es impar
        print(orden, ":", numero)
        contador += 1
        orden += 1
    numero += 1
