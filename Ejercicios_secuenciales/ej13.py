print("______________________________________________________________")
print("|vamos a calcular la raiz cuadrada y raiz cúbica de un número|")
print("--------------------------------------------------------------")

# Pedimos los datos
num = float(input("Introduce un número: "))



# importamos el módulo math

import math

# Realizamos los calculos
raizcuadrada = math.sqrt(num)
raizcubica = num ** (1/3)

# mostrar el resultado por pantalla
print("La raiz cuadrada de ", num, " es ", raizcuadrada)
print("La raiz cubica de ", num, " es ", raizcubica)

