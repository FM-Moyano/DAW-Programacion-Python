print("______________________________________________________")
print("|vamos a calcular la clasificación final de un alumno|")
print("------------------------------------------------------")

# pedimos datos
exa1 = float(input("Introduce la nota del primer examen: "))
exa2 = float(input("Introduce la nota del segundo examen: "))
exa3 = float(input("Introduce la nota del tercer examen: "))
exa_final = float(input("Introduce la nota del examen final: "))
trabajo = float(input("Introduce la nota del trabajo fnal: "))

# Realizamos los cálculos
nota_examenes = 0.55 * ((exa1 + exa2 + exa3) / 3)
nota_exafinal = 0.3 * exa_final
nota_trabajo = 0.15 * trabajo
final = nota_examenes + nota_exafinal + nota_trabajo

# Mostrar por pantalla
print("La nota final es ", final)
