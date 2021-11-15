print("______________________________________________")
print("|vamos a calcular la distancia entre 2 puntos|")
print("----------------------------------------------")
# importamos el modulo math
import math

# Pedimos los datos al usuario
x1 = int(input("Introduce las coordenadas del punto 1:\n"))
y1 = int(input())
x2 = int(input("Introduce las coordenadas del punto 2:\n"))
y2 = int(input())

# Realizamos los calculos
distancia = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

# Mostramos por pantalla el resultado
print("La distancia es ", distancia)
