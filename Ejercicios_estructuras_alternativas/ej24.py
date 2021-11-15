"""
Programa que, dado un número real que debe representar
la calificación numérica de un examen,proporcione la calificación cualitativa
correspondiente al número dado. La calificación cualitativa será una de las
siguientes: «Suspenso» (nota menor que 5), «Aprobado» (nota mayor o
igual que 5, pero menor que 7), «Notable» (nota mayor o igual que 7, pero
menor que 9), «Sobresaliente» (nota mayor o igual que 9, pero menor que 10),
«Matrícula de Honor» (nota 10).
----------------------------------------------------------------------------------------------------------------
Autor: Francisco Manuel Moyano Coleto
Fecha: 24/10/2021
----------------------------------------------------------------------------------------------------------------
Algoritmo:
1. Pedir la nota del examen;
2. Si nota es menor que 5: Suspenso;
3. Si nota mayor o igual a 5, pero menor que 7: Aprobado;
4. Si nota mayor o igual a 7, pero menor que 9: Notable;
5. Si nota mayor o igual a 9, pero menor que 10: Sobresaliente;
6. Si nota es igual a 10: Matrícula de Honor.
"""
print("===========================================================")
print("Programa que muestra la calificación numéricaa de un examen")
print("===========================================================")

nota = float(input("Introduce la nota del examen: "))

if nota < 5:
    print("Suspenso")
elif 5 <= nota < 7:
    print("Aprobado")
elif 7 <= nota < 9:
    print("Notable")
elif 9 <= nota < 10:
    print("Sobresaliente")
elif nota == 10:
    print("Matrícula de Honor")
