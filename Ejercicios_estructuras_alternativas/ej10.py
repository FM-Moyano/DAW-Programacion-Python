"""
programa que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique.

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 24/10/2021
___________________________________________________
Algoritmo
___________________________________________________
1. pedimos el centro (x1,y1) de la circunferencia y su radio r1.
2. Pedimos el centro (x2,y2) de la circunferencia y su radio r2.
3. calculamos la distancia entre los centros.
4. Si distancia>suma de los radios mostrar "Circunferencias exteriores"
5. Si distancia = suma de los radios mostrar "Tangentes exteriores"
6. Si distancia < suma de los radios Y distancia> que el valor absoluto de la resta de los radios mostrar "Circunferencias secante"
7. Si distancia = que el valor absoluto de la resta de los radios mostrar "Circunferencias tangentes interiores"
8. Si distancia >0 y distancia < que el valor absoluto de la resta de los radios mostrar "Circunferencias interiores"
9. Si distancia = 0  mostrar "Circunferencias concéntricas"
"""

import math

print("------------------------------------------------------------------------------------")
print("|Programa que pide los puntos centrales y los radios y clasifica en circunferencias|")
print("------------------------------------------------------------------------------------")


# Pedimos los datos
x1 = float(input("Introduce la coordenada x del centro de la primera circunferencia: "))
y1 = float(input("Introduce la coordenada y de la primera circunferencia: "))
r1 = float(input("Introduce el radio de la primera circunferencia: "))
x2 = float(input("Introduce la coordenada x del centro de la segunda circunferencia: "))
y2 = float(input("Introduce la coordenada y de la segunda circunferencia: "))
r2 = float(input("Introduce el radio de la segunda circunferencia: "))

# calculos
distancia_circunferencias = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

# Resultado

if distancia_circunferencias > (r1 + r2):
    print("Las circunferencias son exteriores")
elif (r1 + r2) > distancia_circunferencias > abs(r1 - r2):
    print("La circunferencia es secante")
elif 0 < distancia_circunferencias < abs(r1 - r2):
    print("Las circunferencias son interiores")
elif distancia_circunferencias == (r1 + r2):
    print("Las circunferencias son tangentes exteriores")
elif distancia_circunferencias == abs(r1 - r2):
    print("Las circunferencias son tangentes interiores")
elif distancia_circunferencias == 0:
    print("Las circunferencias son concéntricas")
else:
    print("Se ha dado un error")
