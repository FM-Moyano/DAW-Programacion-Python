print("______________________________________________")
print("|vamos intercambiar el valor de dos variables|")
print("----------------------------------------------")

# Pedimos los datos al usuario
a = input("Introduce el valor de 'A': ")
b = input("Introduce el valor de 'B': ")

# Realizamos las opereaciones
a, b = b, a

# Mostramos por pantalla los resultados
print("Valor de A ", a)
print("Valor de B ", b)

