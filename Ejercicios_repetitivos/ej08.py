"""
Programa que muestra un cronometro

- Autor : Francisco Manuel Moyano Coleto

--------------------------------------------------
Algoritmo
--------------------------------------------------
1. importamos el modulo time
2. bucle con la variable hora que tendrá rango 24
3. dentro bucle con la variable minuto que tendrá rango 60
4. dentro bucle con la varieble segundo que tendrá rango 60
5. imprimimos por pantalla.
6. usamos el metodo sleep valor a 1, para que dure un segundo
"""

print("Cronometro: ")

import os
import time

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            os.system("cls")
            print(f"{hora}:{minuto}:{segundo}")
            time.sleep(1)
