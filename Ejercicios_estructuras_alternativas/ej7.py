"""
programa que pide por pantalla la base y el exponente, para calcular la potencia

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 21/10/2021

-----------------------------------------
Algoritmo
__________________________________________
1. pedimos por pantalla el exponente y la base.
2. comprobamos si el exponente es positivo y si lo es calculamos la potencia.
3. si no comprobamos si el exponente es 0 y damos el resultado de la potencia igual a 0
4. si no damos realizamos 1/ potencia con exponente positivo y mostramos el resultado
"""

print("------------------------------------------------------------")
print("Programa que realiza la potencia dada la base y el exponente")
print("------------------------------------------------------------")

base = int(input("introduce la base: "))
exponente = int(input("introduce el exponente: "))

# comprobamos los valores

if exponente > 0:
    print("El resultado de la potencia es ", base ** exponente)
elif exponente == 0:
    print("El resultado de la potencia es 1")
else:
    print("El resultado de la potencia es", 1/base ** abs(exponente))
