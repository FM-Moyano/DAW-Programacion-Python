"""
Programa que pide por teclado números y la cantida de números que se van a introducir
y el programa debe de informar de cuantoss número son iguales, menores y mayores que 0

- Autor: Francisco Manuel Moyano Coleto
- Fecha: 03/11/2021

------------------------------------------------------------
Algoritmo
_____________________________________________________________
1. creamos un contador que se iguale a 1 que será el que
controlará los números introducidos.
2. Pedimmos la cantidad de números que se van a introducir.
3. creamos tres variables de contador, una para los números menores que 0,
otra para los mayores que 0 y otra para los iguales a 0
4. comprobaremos que el contador no ha llegado a la cantidad
de números que se piden.
5. mientras esto anterior se cumple se va pidiendo números y comprobamos si
el número es igual a 0, si se cumple  aumentamos el contador de igual a 0,
si no comprobamos si es mayor que 0 y se aumenta en 1 el contador mayor que 0
y si no se aumenta en 1 el contador menor que 0.
6. cuando se terminen estas comprobaciones se aumenta en 1 el contador de
números introducidos.
7. cuando no se cumpla el bucle(variable contado de números introducidos mayor que
variable de números introducidos) se sale y se muestra los resultados.


"""

print("==================================================================================")
print("|Programa que pide la cantidad de números que se van a introducir y los comprueba|")
print("==================================================================================")

# Inicializamos las variables
contador_num = 1
mayor_que_0 = 0
menor_que_0 = 0
igual_que_0 = 0

total_numeros = int(input("Introduce la cantidad de números que se van a añadir: "))

while contador_num <= total_numeros:
    num = int(input("Introduce un número: "))
    if num == 0:
        igual_que_0 += 1
    elif num > 0:
        mayor_que_0 += 1
    else:
        menor_que_0 += 1
    contador_num += 1

print("Has introducido", igual_que_0, " números iguales que 0,", mayor_que_0, "números mayores que 0 y ", menor_que_0, "números menores que 0")
