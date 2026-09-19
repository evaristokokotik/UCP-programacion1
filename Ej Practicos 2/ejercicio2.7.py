#Escribir un programa que calcule según un menú y elección del usuario realice:
#opción 1 - El perímetro y área de un círculo dado su radio.
#opción 2 - Escribir un programa que calcule el área y perímetro de un pentágono.
#opción 3 - Escribir un programa que calcule el perímetro y área de un rectángulo.

import math

print("Bienvenido al calculador de figuras geométricas, seleccione una opción:")
print("1. Círculo")
print("2. Pentágono")
print("3. Rectángulo")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    radio = float(input("Ingrese el radio del círculo: "))
    perimetro = 2 * math.pi * radio
    area = math.pi * radio ** 2
    print("Perímetro del círculo:", round(perimetro, 2))
    print("Área del círculo:", round(area, 2))
elif opcion == 2:
    lado = float(input("Ingrese el lado del pentágono: "))
    perimetro = 5 * lado
    area = (5 * lado ** 2) / (4 * math.tan(math.pi / 5))
    print("Perímetro del pentágono:", round(perimetro, 2))
    print("Área del pentágono:", round(area, 2))
elif opcion == 3:
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    perimetro = 2 * (base + altura)
    area = base * altura
    print("Perímetro del rectángulo:", round(perimetro, 2))
    print("Área del rectángulo:", round(area, 2))
else:
    print("Opción no válida.")