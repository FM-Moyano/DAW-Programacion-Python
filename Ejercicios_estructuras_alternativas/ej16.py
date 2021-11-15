"""
Programa que calcula el costo de las llamadas según su duración

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 24/10/2021

--------------------------------------------------
Algoritmo
--------------------------------------------------
1 . preguntamos la duracion de la llamada.
2. preguntamos si la llamda es en domingo
y si lo es preguntar si es de mañana o de tarde.
3. Si tiempo <5 coste=tiempo*100
4. Si tiempo<8 coste=(tiempo-5)*80 + 500
5. Si tiempo<10 coste=(tiempo-8)*70 + 240 + 500
6. Si tiempo>10 coste=(tiempo-10)*50 + 140 + 240 + 500
7. Si la llamada es en domingo coste = coste + 3%
8. Si la llamada es otro día por la mañana coste = coste + 15%
9. Si la llamada es otro día por la mañana coste = coste + 10%
10. Mostrar coste final en euros
"""

print("--------------------------------------------")
print("Programa que calcula es costo de una llamada")
print("--------------------------------------------")

# Pedimos los datos
duracion = int(input("Introduce la duración de la llamada: "))
dia = input("¿ la llamda fue realizada un Domingo? S/N: ").upper()
if dia == "N":
    turno = input("¿Qué turno realizo la llamada? M/T: ").upper()

# Comparaciones

if duracion <= 5:
    coste = duracion * 100
elif duracion <= 8:
    coste = (duracion - 5) * 80 + 500
elif duracion <= 10:
    coste = (duracion - 8) * 70 + 240 + 500
else:
    coste = (duracion - 10) * 50 + 140 + 240 + 500

# impuestos

if dia == "S":
    coste += coste * 0.03
elif turno == "M":
    coste += coste * 0.15
else:
    coste += coste * 0.10

# Salida
print("El coste de la llamada es ", coste/100, "€")


