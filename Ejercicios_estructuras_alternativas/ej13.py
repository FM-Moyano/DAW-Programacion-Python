"""
Programa que lee una cantidad de dinero y nos muestra cuantos billetes
de 500, 200, 100, 50, 20, 10 y 5 lo constituye y monedas de 2 y 1 €

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 24/10/2021
___________________________________________________
Algoritmo
___________________________________________________
1. Pedimos la cantidad de dinero
2. hacemos la división entera de el numero por 500
y le restamos al total 500 si cumple la condicón
3. hacemos la división entera de el numero por 200
y le restamos al total 200 si cumple la condicón
4. hacemos la división entera de el numero por 100
y le restamos al total 100 si cumple la condicón
5. hacemos la división entera de el numero por 50
y le restamos al total 50 si cumple la condicón
6. hacemos la división entera de el numero por 20
y le restamos al total 20 si cumple la condicón
7. hacemos la división entera de el numero por 10
y le restamos al total 10 si cumple la condicón
8. hacemos la división entera de el numero por 5
y le restamos al total 5 si cumple la condicón
9. hacemos la división entera de el numero por 2
y le restamos al total 2 si cumple la condicón
10. hacemos la división entera de el numero por 1
y le restamos al total 1 si cumple la condicón
"""

# Pedimos los datos
num = int(input("Introduce cuantos euros tienes: "))

# comprobamos
if num >= 500:
    b500 = num // 500
    num = num - b500 * 500
    print("Tenemos ", b500, "billetes de 500€")

if num >= 200:
    b200 = num // 200
    num = num - b200 * 200
    print("Tenemos ", b200, "billetes de 200€")

if num >= 100:
    b100 = num // 100
    num = num - b100 * 100
    print("Tenemos ", b100, "billetes de 100€")

if num >= 50:
    b50 = num // 50
    num = num - b50 * 50
    print("Tenemos ", b50, "billetes de 50€")

if num >= 20:
    b20 = num // 20
    num = num - b20 * 20
    print("Tenemos ", b20, "billetes de 20€")

if num >= 10:
    b10 = num // 10
    num = num - b10 * 10
    print("Tenemos ", b10, "billetes de 10€")

if num >= 5:
    b5 = num // 5
    num = num - b5 * 5
    print("Tenemos ", b5, "billetes de 5€")

if num >= 2:
    b2 = num // 2
    num = num - b2 * 2
    print("Tenemos ", b2, "monedas de 2€")

if num >= 1:
    b1 = num // 1

    print("Tenemos ", b1, "monedas de 1 €")
