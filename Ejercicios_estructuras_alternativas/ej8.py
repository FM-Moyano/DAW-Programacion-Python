"""
Programa que pide la nota, la edad y el sexo y si a nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 21/10/2021
___________________________________________________
Algoritmo
___________________________________________________

1. Pedimos los datos al usuario
2. comprobamos si la nota es mayor o igual que 5
3. Si se cumple comprobamos si la edad es igual a 18
4. si se cumple comprobamos si se ha introducido en el sexo M o F
5. si es M sacamos por pantalla 'posible' si sale F sacamos 'ACEPTADA'
6. si no se cumple alguna de estas sacamos ' NO ACEPTADA'
"""

print("-----------------------------------------------")
print("|comprobacion de datos credenciales personales|")
print("-----------------------------------------------")

# Introducción de datos
nota = float(input("Introduzca la nota: "))
edad = int(input("Introduce la edad "))
sexo = input("Introduce el sexo con 'M'/'F' :")

# Comprobaciones
if nota >= 5 and edad >= 18:
    if sexo == "F" or sexo == "f":
        print("ACEPTADA")
    elif sexo == "M" or sexo == "m":
        print("POSIBLE")
else:
    print("NO ACEPTADA")
