"""
Programa que calcula el valor del viaje de autobús segun el número de alumnos

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 24/10/2021

--------------------------------------------------
Algoritmo
__________________________________________________
1. Preguntamos el número de alumnos que asisten al viaje.
2. Comprobamos si son 100 o más y el númer de alumnos lo multiplicamos por 65
2. Comprobamos si el número de alumnos está entre 50 y 99 y se multiplica por 70
3. Comprobamos si el número de alumnos está entre 30 a 49 y se multiplica por 95
4. si hay menos de 30 alumnos el viaje costará en total 400
"""

print("---------------------------------------------------------------------")
print("Programa que calcula el precio de un viaje según el número de alumnos")
print("---------------------------------------------------------------------")

# Pedimos el valor
num = int(input("Introduce el número de alumnos que asiten al viaje: "))

# Comparaciones

if num >= 100:
    print("El valor del viaje es ", num * 65, ", 65€ por alumno")
elif 50 <= num <= 99:
    print("El valor del viaje es ", num * 70, ", 70€ por alumno")
elif 30 <= num <= 49:
    print("El valor del viaje es", num * 95, ", 95€ por cada alumno")
elif num == 0:
    print("No habrá viaje porque no va asistir ningún alumno")
else:
    print("El valor del viaje es 400€")
