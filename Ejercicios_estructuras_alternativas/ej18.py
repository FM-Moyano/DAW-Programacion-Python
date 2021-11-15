"""
Programa que pide el número de dia de la semana del 1 al 7 y nos lo devuelve
de lunes a domingo

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 24/10/2021

--------------------------------------------------
Algoritmo
--------------------------------------------------
1. Pedimos el número
2. Si no está entre 1 y 7 es erroneo
3. si es 1 -> Lunes
4. si es 2 -> Martes
5. si es 3 -> Miercoles
6. si es 4 -> Jueves
7. si es 5 -> Viernes
8. si es 6 -> Sabado
9. si es 7 -> Domingo
"""
print("-----------------------------------------")
print("Programa que nos dice el dia de la semana")
print("-----------------------------------------")

# Pedimos los datos
num = int(input("Introduce el número de día de la semana (1-7): "))

# Comprobamos y mostramos
if num > 7 or num < 1:
    print("El valor introducido es correcto")
else:
    if num == 1:
        print("Es Lunes")
    elif num == 2:
        print("Es Martes")
    elif num == 3:
        print("Es Miercoles")
    elif num == 4:
        print("Es Jueves")
    elif num == 5:
        print("Es Viernes")
    elif num == 6:
        print("Es Sábado")
    else:
        print("Es Domingo")
