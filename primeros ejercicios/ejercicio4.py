#Escribir un programa que pida la edad y el sexo. Mostrar un mensaje si puede votar o no
#dependiendo si la edad es mayor o igual a 16 años. Ejemplo: "Usted es mujer y puede votar"

edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo M (masculino) o F (femenino): ").upper()

while sexo != "M" and sexo != "F":
    sexo = input("Sexo inválido. Ingrese M o F: ").upper()

if sexo == "F":
    genero = "femenino"
else:
    genero = "masculino"

if edad >= 16:
    print(f"Usted es {genero}, su edad es {edad} años y puede votar")
else:
    print(f"Usted es {genero}, su edad es {edad} años y no puede votar")
