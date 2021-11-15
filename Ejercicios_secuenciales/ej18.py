print("___________________________________________________________________")
print("|vamos calcular las iniciales del nombre y apellido de una persona|")
print("-------------------------------------------------------------------")

# Pedimos datos al usuario
nombre = input("Introduzca su primer nombre :")
nombre2 = input("Introduzca su segundo nombre, si no tiene deje este campo en blano y pulse intro :")
ape1 = input("Introduzca el primer apellido :")
ape2 = input("Introduzca el segundo apellido :")

# Realizamos los calculos
if nombre2 != "":
    iniciales = (nombre[0] + nombre2[0] + ape1[0] + ape2[0]).upper()
else:
    iniciales = (nombre[0] + ape1[0] + ape2[0]).upper()

# Mostrar resultados
print("Las iniciales son :", iniciales)
