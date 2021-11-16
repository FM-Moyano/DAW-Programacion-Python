""""
Programa que pide dos números e imprime todos los numeros pares entre estos dos

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 05/11/2021

---------------------------------------------------------------
Algoritmo
---------------------------------------------------------------
1. Pedimos los 2 números
2. comprobamos que el primer número introducido es menor que el segundo,
si no cambiamos los valores
3. hacemos un bucle que va desde el 1º número hasta el 2º y va sumando el valor
de la variable a uno cada vez que se ejecuta
4. comprobamos si el valor de la variable es par, si lo es se muestra,
si no se suma a uno el valor

"""

print("==========================================================")
print("|programa que muestra los números pares entre dos números|")
print("==========================================================")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    num2, num1 = num1, num2
elif num2 == num1:
    print("Has introducido 2 números iguales")

for i in range(num1, num2 + 1, 1):
    if i % 2 == 0:
        print(i)
