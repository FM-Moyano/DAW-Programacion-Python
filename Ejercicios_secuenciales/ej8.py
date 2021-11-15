print("______________________________________________________________")
print("|vamos a calcular el suelto dando el sueldo base y sus ventas|")
print("--------------------------------------------------------------")

# Pedimos al usuario los datos
salarioBase = float(input("Introduce el sueldo base: "))
venta1 = float(input("Introduce el valor de la primera venta: "))
venta2 = float(input("Introduce el valor de la segunda venta: "))
venta3 = float(input("Introduce el valor de la tercera venta: "))

# Realizamos los calculos
comision = 0.1 * (venta1 + venta2 + venta3)
sueldoTotal = salarioBase + comision

# sacamos los resultados por pantalla
print("La comision por  ventas es ", comision)
print("El sueldo total es ", sueldoTotal)
