"""
Programa que calcula el valor de la uva según el tipo

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 24/10/2021

--------------------------------------------------
Algoritmo
1. pedimos el precio inicial.
2. pedimos el tipo de uva y el tamaño
3. comprobamos que se ha introducido los valores correctos.
4. si es A y tipo 1 el precio inicio le sumamos 0.2
5. si es A y tipo 2 el precio inicio le sumamos 0.3
6. si es B y tipo 1 el precio inicio le restamos 0.3
7. si es B y tipo 1 el precio inicio le restamos 0.5
--------------------------------------------------
"""

print("----------------------------------------------")
print(" Este programa calcula el precio final de uva")
print("----------------------------------------------")

precio_inicio = float(input("Introduce el precio inicial (€): "))
tipo_uva = input("Introduce el tipo de uva (A, B): ").upper()
tamaño_uva = int(input("Introduce el tamaño (1, 2): "))

if tipo_uva != "A" and tipo_uva != "B":
    print("El dato introducido no es correcto")

if tipo_uva == "A":
    if tamaño_uva != 1 and tamaño_uva != 2:
        print("Has introducido un tamaño incorrecto!")
    if tamaño_uva == 1:
        print(f"Precio final es: {precio_inicio + 0.2} €")
    if tamaño_uva == 2:
        print(f"Precio final es: {precio_inicio + 0.3} €")
if tipo_uva == "B":
    if tamaño_uva == 1:
        print(f"Precio final es: {precio_inicio - 0.3} €")
    if tamaño_uva == 2:
        print(f"Precio final es: {precio_inicio - 0.5} €")
