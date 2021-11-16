"""
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir.

A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
Informa si hemos introducido algún número igual a los límites del intervalo.

-Autor: Francisco Manuel Moyano Coleto
-Fecha: 09/11/2021

=======================================================
Algoritmo
=======================================================
1. Pedimos el limite inferior y superior
2. comrobamos si el el limite superior es mayor, si no
lo seguimos pidiendo hasta que se cumpla.
3. pedimos números hasta que se introduzca un 0.
4. mostramos la suma de los númeross que están dentro del intervalo.
5. mostraos la cantidad de números que están en el intervalo.
6. mostramos si hemos introducido alguún número igualos a los límites.
"""
print("=======================================================================")
print("|Programa que pide números entre dos limites y nos muestra la cantidad|")
print("=======================================================================")


limite_inferior = int(input("Introduce el límite inferior: "))
limite_superior = int(input("Introduce el limite superior: "))

while limite_superior < limite_inferior:
    limite_inferior = int(input("Introduce el límite inferior: "))
    limite_superior = int(input("Introduce el limite superior: "))

num = 1
total_dentro = 0
total_fuera = 0
igual_a_limites = 0
while num != 0:
    num = int(input("Introduceun número: "))
    if limite_superior >= num >= limite_inferior:
        total_dentro = total_dentro + num
    else:
        total_fuera += 1
    if num == limite_superior or num == limite_inferior:
        igual_a_limites += 1

print("La suma de los números que están dentro del intervalo es ", total_dentro, " hay ", total_fuera, " números fuera del intervalo y tenemos ", igual_a_limites, "números iguales a los límites del intervalo ")


