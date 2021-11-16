"""
Programa que lee una cadena y convierte las mayusculas en minusculas y viceversa

- Autor: Francisco  Manuel Moyano Coleto

------------------------------------------------------------
ALgoritmo
------------------------------------------------------------
1. Pedimos la cadena
2. Creamos un bucle que va recorriendo la cadena.
3. Si es una mayuscula la convertimos en minuscula
4. si no la convertimos en mayuscula
"""

print("Programa que pide uan cadena y cambia las mayusculas por minisculas")

cadena = input("Introduce una cadena: ")
resultado = ""

for i in cadena:
    if i.isupper():
        i = i.lower()
        resultado += i
    else:
        i = i.upper()
        resultado += i
print(resultado)
