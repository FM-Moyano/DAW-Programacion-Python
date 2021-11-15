print("__________________________________________________________")
print("|vamos a calcular el perimetro y el área de un rectangulo|")
print("----------------------------------------------------------")

# pedimos los datos al usuario
altura = float(input("Introduce la altura: "))
base = float(input("Introduuce la base: "))

# realizamos los calculos
perimetro = 2 * (base + altura)
area = base * altura

# sacamos el resultado
print("El área es", area, "y el perimetro es", perimetro)

