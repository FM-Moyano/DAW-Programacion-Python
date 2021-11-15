# para realizar este calculo vamos a importar la librería math
import math

print("______________________________________________________________")
print("|vamos a calcular el la hipotenusa de un triángulo rectangulo|")
print("--------------------------------------------------------------")

# le pedimos los datos al usuario
lado1 = float(input("Intruduce el primer cateto: "))
lado2 = float(input("Introduce el segundo cateto: "))

# realizamos los calculos
hipotenusa = math.sqrt(lado1 ** 2 + lado2 ** 2)

# sacamos por pantalla el resultado
print("EL resultado de la hipotenusa es ", hipotenusa)
