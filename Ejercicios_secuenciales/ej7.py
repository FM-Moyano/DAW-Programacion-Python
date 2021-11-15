print("__________________________________")
print("|vamos a pasar de minutos a horas|")
print("----------------------------------")

# Pedimos los datos
num1 = int(input("Cualtos minutos son: "))

# Realizamos los calculos
horas = num1 // 60
minutos = num1 % 60

# mostramos por pantalla
print(horas, " horas y ", minutos, "minutos.")
