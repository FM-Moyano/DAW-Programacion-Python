print("________________________________________________________________")
print("|vamos a obtener el número invertido de un numero de dos cifras|")
print("----------------------------------------------------------------")

# Pedimos los datos al usuario
num = int(input("Introduzca un número: "))

# Realizamos operaciones
posicion1 = num // 10
posicion2 = num % 10
invertido = posicion2 * 10 + posicion1

# Mostramos el resultado por pantalla
print("El número invertido es : ", invertido)


