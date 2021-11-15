"""
Programa que pida un número entre 1- 12 (incluidis) y nos diga
el número de días que tiene ese mes

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 24/10/2021

--------------------------------------------------
Algoritmo
--------------------------------------------------
1. comprobar si el número está entre 1 y 12
2. si no está mostrar error
3. si es 1 -> 31 dias
4. si es 2 -> 28 dias
5. si es 3 -> 31 dias
6. si es 4 -> 30 dias
7. si es 5 -> 31 dias
8. si es 6 -> 30 dias
9. si es 7 -> 31 dias
10. si es 8 -> 31 dias
11. si es 9 -> 30 dias
12. si es 10 -> 31 dias
13. si es 11 -> 30 dias
14. si es 12 -> 31 dias

"""

print("-----------------------------------------------------------------------")
print("Programa que nos muestra el número de días que tiene el mes introducido")
print("-----------------------------------------------------------------------")

# Pedimos el dato
num = int(input("Introduce el número del mes (1-12)"))

# Comprobaos y mostramos

if num > 12 or num < 1:
    print("El número introducido es erroneo")
else:
    if num == 1:
        print("El mes ", num, "tiene 31 días")
    elif num == 2:
        print("El mes ", num, "tiene 28 días")
    elif num == 3:
        print("El mes ", num, "tiene 31 días")
    elif num == 4:
        print("El mes ", num, "tiene 30 días")
    elif num == 5:
        print("El mes ", num, "tiene 31 días")
    elif num == 6:
        print("El mes ", num, "tiene 30 días")
    elif num == 7:
        print("El mes ", num, "tiene 31 días")
    elif num == 8:
        print("El mes ", num, "tiene 31 días")
    elif num == 9:
        print("El mes ", num, "tiene 30 días")
    elif num == 10:
        print("El mes ", num, "tiene 31 días")
    elif num == 11:
        print("El mes ", num, "tiene 30 días")
    elif num == 12:
        print("El mes ", num, "tiene 31 días")
