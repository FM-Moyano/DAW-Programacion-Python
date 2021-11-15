print("_____________________________________________________________")
print("|vamos calcular el tiempo que el primer alcanzará al segundo|")
print("-------------------------------------------------------------")

# Pedir los datos al usurio
velocidad1 = float(input("Inserta la velocidad en Km/h del primer coche : "))
velocidad2 = float(input("Inserta la velocidad en Km/h del segundo coche : "))
distancia = float(input("Inserta la distancia en Km entre los dos coches : "))

# Realizamos los calculos
tiempo = 60 * distancia / (velocidad1 - velocidad2)

# Mostramos el resultado
print("El segundo coche alcanzará al primero en", tiempo, "min")
