"""
Propósito: Una compañía de transporte internacional tiene servicio en algunos países de América del Norte,
América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso
del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:

ZONA  UBICACIÓN	          COSTO/GRAMO
1	  América del Norte	  24.00 euros
2	  América Central	  20.00 euros
3	  América del Sur	  21.00 euros
4	  Europa	          10.00 euros
5	  Asia	              18.00 euros

Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados,
esto por cuestiones de logística y de seguridad. Realice un algoritmo para determinar el cobro por la entrega
de un paquete o, en su caso, el rechazo de la entrega.

----------------------------------------------------------------------------------------------------------------
Autor: Francisco Manuel Moyano Coleto
Fecha: 24/10/2021
----------------------------------------------------------------------------------------------------------------
Algoritmo:
1. Pedir el número de zona
2. Pedir el peso del paquete (Gramos)
3. Si el peso es mayor que 5000 rechazar la entrega
4. Si zona es igual a 1
5. El cobro es igual a peso multiplicado por 24
6. Etc.
7. Mostrar el cobro.
"""
print("===========================================================")
print("Este programa calcula el coste de la entrega de un paquete")
print("===========================================================")
print("ZONA  UBICACIÓN	          COSTO/GRAMO\n"
      "1.....América del Norte....24.00 euros\n"
      "2.....América Central......20.00 euros\n"
      "3.....América del Sur......21.00 euros\n"
      "4.....Europa...............10.00 euros\n"
      "5.....Asia.................18.00 euros")

zona = int(input("Introduce el número de la zona: "))

if zona < 1 or zona > 5:
    print("Dato erroneo, el valor introducido no es correcto")
else:
    peso = int(input("Introduce el peso del paquete (gramos): "))

    if peso > 5000:
        print("¡La entrega es imposible! Los paquetes con un peso superior a 5 kg no son transportados.")
    elif zona == 1:
        cobro = peso * 24
    elif zona == 2:
        cobro = peso * 20
    elif zona == 3:
        cobro = peso * 21
    elif zona == 4:
        cobro = peso * 10
    elif zona == 5:
        cobro = peso * 18
    if peso <= 5000 and 0 < zona < 6:
        print("La entrega costará:", cobro, " €")
