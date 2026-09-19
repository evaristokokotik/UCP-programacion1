#Escribir un programa que calcule según un menú y elección del usuario realice:
#opción 1 - El perímetro y área de un círculo dado su radio.
#opción 2 - Escribir un programa que calcule el área y perímetro de un pentágono.
#opción 3 - Escribir un programa que calcule el perímetro y área de un rectángulo

print("Bienvenido al programa de cálculo de perímetro y área")
print("Seleccione una opción:")
print("1. Círculo")
print("2. Pentágono")
print("3. Rectángulo")

opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    radio = float(input("Ingrese el radio del círculo: "))
    perimetro = 2 * 3.14 * radio
    area = 3.14 * (radio ** 2)
    print(f"El perímetro del círculo es: {perimetro:.2f}")
    print(f"El área del círculo es: {area:.2f}")
elif opcion == 2:
    lado = float(input("Ingrese la longitud del lado del pentágono: "))
    perimetro = 5 * lado
    apotema = float(input("Ingrese la apotema del pentágono: "))
    area = (perimetro * apotema) / 2
    print(f"El perímetro del pentágono es: {perimetro:.2f}")
    print(f"El área del pentágono es: {area:.2f}")
elif opcion == 3:
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    perimetro = 2 * (base + altura)
    area = base * altura
    print(f"El perímetro del rectángulo es: {perimetro:.2f}")
    print(f"El área del rectángulo es: {area:.2f}")
else:
    print("Opción inválida. Por favor, seleccione una opción válida.")

