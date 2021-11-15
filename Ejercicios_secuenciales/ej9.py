print("________________________________________________")
print("|vamos a calcular descuento total en una compra|")
print("------------------------------------------------")

# Pedimos los datos
compra = float(input("Introduce el total de la compra: "))

# Realizamos los calculos
descuento = compra * 0.15
total = compra - descuento

# Mostramos por pantalla
print("El total de tu compra era ", compra, ", pero con el decuento queda finalmente en ", total)
