print("________________________________________________________________")
print("|vamos calcular la hora de llegada en bici de una ciudad a otra|")
print("----------------------------------------------------------------")

# vamos a pedir al usuario los datos
horaSalida = int(input("Introduzca la hora de salida :"))
minutosSalida = int(input("Introduzca los minutos de salida :"))
segundosSalida = int(input("Introduxca los segundos de salida :"))
viajeSegundos = int(input("Introduzca el tiempo que has tardado en segundos :"))

# Realizamos los calculos
todo_a_segundos = horaSalida * 3600 + minutosSalida * 60 + segundosSalida
total_en_segundos = todo_a_segundos + viajeSegundos
hora = total_en_segundos // 3600
minutos = (total_en_segundos % 3600) // 60
segundos = (total_en_segundos % 3600) % 60

# Mostrar por pantalla el resultado
print("La hora de llegada es : ", hora, ":", minutos, ":", segundos)
