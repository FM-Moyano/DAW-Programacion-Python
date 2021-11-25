"""
Programa a que juegue al piedra/papel/tijera contra el ordenador, que usará
números aleatorios para realizar la tirada. Después de cada jugada pregunta al usuario si quiere
continuar, en caso negativo se muestra el número de partidas jugadas, las ganadas por cada jugador
y las empatadas.

- Autor: Francisco Manuel Moyano Coleto

======================================================================
Algoritmo
======================================================================
1. creamos una variable con un numero aleatorio desde 1 a 3, para ello importamos random
2. Pedimos al usuario un numero entre 1 y tres.
3. validamos que es cierto.
4. es empate cuando el usuario y el introducen el mismo número
5. el usuario gana si sale papel(2) y la maquina piedra(1), si saca tijeras(3) y la maquina papel(2) y si saca piedra(1) y la maquina tijeras(3)
6. se muestra el resultado y se pregunta si se quiere continuar.
7. si no se introduce correctamente se vuelve a preguntar hasta que sea S o N
"""

import random

print("Juego de piedra papel y tijera")
print("------------------------------")

jugador = int(input("¿Piedra (1), Papel (2) o Tijera (3)?: "))

maquina = random.randrange(2) + 1
seguimos_jugando = "s"
partidas_jugadas = 1
partidas_ganadas = 0
partidas_empatadas = 0
partidas_perdidas = 0
while seguimos_jugando == "s":

    while jugador > 3 or jugador < 1:
        print("No has introducido un numero correcto")
        jugador = int(input("¿Piedra (1), Papel (2) o Tijera (3)?: "))

    if jugador == maquina:
        if maquina == 1:
            print("Ordenador juega: Piedra")
            print("Empate")
        elif maquina == 2:
            print("Ordenador juega: Papel")
            print("Empate")
        else:
            print("Ordenador juega: Tijera")
            print("Empate")
        partidas_empatadas += 1
    elif jugador == 2 and maquina == 1 or jugador == 3 and maquina == 2 or jugador == 1 and maquina == 3:
        if maquina == 1:
            print("Ordenador juega: Piedra")
            print("¡¡¡Ganastes!!!")
        elif maquina == 2:
            print("Ordenador juega: Papel")
            print("¡¡¡Ganastes!!!")
        else:
            print("Ordenador juega: Tijera")
            print("¡¡¡Ganastes!!!")
        partidas_ganadas += 1

    else:
        if maquina == 1:
            print("Ordenador juega: Piedra")
            print("Ordenador Gana")
        elif maquina == 2:
            print("Ordenador juega: Papel")
            print("Ordenador Gana")
        else:
            print("Ordenador juega: Tijera")
            print("Ordenador Gana")
        partidas_perdidas += 1

    seguimos_jugando = input("¿Seguimos jugando? (S/N): ").lower()
    while seguimos_jugando != "n" and seguimos_jugando != "s":
        print("Introduce (S/N)")
        seguimos_jugando = input("¿Seguimos jugando? (S/N): ").lower()

    if seguimos_jugando == "s":
        jugador = int(input("¿Piedra (1), Papel (2) o Tijera (3)?: "))
        partidas_jugadas += 1
    elif seguimos_jugando == "n":
        break

print()
print("Partidas jugadas: ", partidas_jugadas)
print("Partidas ganadas: ", partidas_ganadas)
print("Partidas perdidas: ", partidas_perdidas)
print("Partidas empatadas: ", partidas_empatadas)
