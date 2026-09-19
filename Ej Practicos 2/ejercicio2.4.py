#Escribir un programa que pida la edad y el sexo. Mostrar un mensaje si puede votar o no
#dependiendo si la edad es mayor o igual a 16 años. Ejemplo. “Usted es mujer y puede
#votar”

edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (M/F): ")
if edad >= 16:
    print("Usted es", "mujer" if sexo.upper() == "F" else "hombre", "y puede votar")
else:
    print("Usted es", "mujer" if sexo.upper() == "F" else "hombre", "y no puede votar")
